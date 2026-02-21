export type Tree = {
    [name: string]: Tree | string | Uint8Array
};

export type InputStream =
    (byteLength: number) => Uint8Array | null;

export type OutputStream =
    (bytes: Uint8Array | null) => void;

export type ProgressCallback =
    (event: { source: Application, totalLength: number, doneLength: number }) => void;

export type RunOptions = {
    stdin?:  InputStream  | null;
    stdout?: OutputStream | null;
    stderr?: OutputStream | null;
    decodeASCII?: boolean;
    synchronously?: boolean;
    fetchProgress?: ProgressCallback;
};

export class Application {
    argv0: string;

    constructor(resources: () => Promise<any>, instantiate: any, argv0: string);

    run(args?: string[], files?: Tree, options?: RunOptions): Promise<Tree> | Tree | undefined;
}

export class Exit extends Error {
    code: number;
    files: Tree;
}

//--------8<--------8<--------8<--------8<--------8<--------8<--------8<--------8<--------8<--------

export const runNextpnrHimbaechelGowin: Command;

export const commands: {
    'gowin_pll': Command,
    'gowin_pack': Command,
    'gowin_unpack': Command,
    'nextpnr-himbaechel-gowin': Command,
};

export const version: string;
