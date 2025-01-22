// This file duplicates a *lot* of code from `@yowasp/runtime`, but since it is only useful for
// Gowin tools, this is likely fine. If more Python-based tools are added then this should be
// moved to `YoWASP/runtime-js` repository.

import { Exit } from '@yowasp/runtime';
import { lineBuffered } from '@yowasp/runtime/util';

let fetch;
if (typeof process === 'object' && process.release?.name === 'node') {
    // Node doesn't have a usable `fetch()`.
    fetch = async function(url, options) {
        if (url.protocol === 'file:') {
            const { readFile } = await import('fs/promises');
            let contentType = 'application/octet-stream';
            if (url.pathname.endsWith('.wasm'))
                contentType = 'application/wasm';
            return new Response(await readFile(url), { headers: { "Content-Type": contentType } });
        } else {
            return globalThis.fetch(url, options);
        }
    };
} else {
    fetch = globalThis.fetch;
}

function writeTree(FS, tree, path = '/') {
    path = path.endsWith('/') ? path : `${path}/`;

    for(const [filename, data] of Object.entries(tree)) {
        const filepath = `${path}${filename}`;
        if (typeof data === 'string' || data instanceof Uint8Array) {
            FS.writeFile(filepath, data);
        } else {
            FS.mkdir(filepath);
            writeTree(FS, data, `${filepath}/`);
        }
    }
}

function readTree(FS, path = '/') {
    path = path.endsWith('/') ? path : `${path}/`;

    const tree = {};
    for (const filename of FS.readdir(path)) {
        const filepath = `${path}${filename}`;
        if (filename === '.' || filename === '..')
            continue;
        if (['/tmp', '/dev', '/proc'].includes(filepath))
            continue;
        const stat = FS.stat(filepath);
        if (FS.isFile(stat.mode)) {
            tree[filename] = FS.readFile(filepath, { encoding: 'binary' });
        } else if (FS.isDir(stat.mode)) {
            tree[filename] = readTree(FS, `${filepath}/`);
        }
    }
    return tree;
}

async function fetchObject(obj, fetchFn) {
    // Mutate the object being fetched, to avoid re-fetches within the same session.
    // Do this in parallel to avoid head-of-line blocking.
    const promises = [];
    for (const [key, value] of Object.entries(obj)) {
        if (typeof value === "string" || value instanceof Uint8Array) {
            promises.push(Promise.resolve([key, value]));
        } else if (value instanceof URL) {
            promises.push(fetchFn(value).then((fetched) => [key, fetched]));
        } else {
            promises.push(fetchObject(value, fetchFn).then((fetched) => [key, fetched]));
        }
    }
    for (const [key, value] of await Promise.all(promises))
        obj[key] = value;
    return obj;
}

function fetchUint8Array(url) {
    return fetch(url).then((resp) => resp.arrayBuffer()).then((buf) => new Uint8Array(buf));
}

function fetchResources({ filesystem }) {
    return Promise.all([
        fetchObject(filesystem, fetchUint8Array)
    ]).then(([filesystem]) => {
        return { filesystem };
    });
}

export class PythonApplication {
    constructor(resources, execute, argv0) {
        this.resources = resources;
        this.resourceData = null;
        this.execute = execute;
        this.argv0 = argv0;
    }

    async run(args = null, files = {}, options = {}) {
        if (options.synchronously)
            throw new Error("Cannot run a Python application synchronously");

        if (this.resourceData === null) {
            this.resourceData = await this.resources().then(fetchResources);
        }

        const loadPyodide = options.loadPyodide ?? (await import('pyodide')).loadPyodide;
        const pyodide = await loadPyodide({ args: [this.argv0, ...args ?? []] });

        if (args === null)
            return; // prefetch resources, but do not actually run

        const lineBufferedConsole = lineBuffered(options.printLine ?? console.log);
        const makeWriter = (output) => {
            return { write(buffer) { output(buffer); return buffer.length; } }
        };
        pyodide.setStdout(makeWriter(options.stdout === undefined ? lineBufferedConsole : options.stdout));
        pyodide.setStderr(makeWriter(options.stderr === undefined ? lineBufferedConsole : options.stderr));

        writeTree(pyodide.FS, this.resourceData.filesystem);
        writeTree(pyodide.FS, {root: files});
        pyodide.FS.chdir('/root');

        let error;
        try {
            this.execute(pyodide, this.argv0);
        } catch (e) {
            if (e instanceof pyodide.ffi.PythonError) {
                error = e;
            } else {
                throw e;
            }
        }

        let exitCode = 0;
        if (error !== undefined) {
            if (error.type === 'SystemExit') {
                exitCode = pyodide.pyimport('sys').last_value.code;
            } else {
                exitCode = 2;
            }
        }

        const filesOut = readTree(pyodide.FS, '/root');
        console.log(exitCode);
        if (exitCode == 0) {
            return filesOut;
        } else {
            throw new Exit(exitCode, filesOut)
        }
    }
}
