export type Tree = {
    [name: string]: Tree | string | Uint8Array
};

export type InputStream =
    (byteLength: number) => Uint8Array | null;

export type OutputStream =
    (bytes: Uint8Array | null) => void;

export type RunOptions = {
    stdin?:  InputStream  | null;
    stdout?: OutputStream | null;
    stderr?: OutputStream | null;
    decodeASCII?: boolean;
    synchronously?: boolean;
};

export type Command =
    (args?: string[], files?: Tree, options?: RunOptions) => Promise<Tree> | Tree | undefined;

export class Exit extends Error {
    code: number;
    files: Tree;
}

//--------8<--------8<--------8<--------8<--------8<--------8<--------8<--------8<--------8<--------

export const runEcppll: Command;
export const runEcpbram: Command;
export const runEcpmulti: Command;
export const runEcppack: Command;
export const runEcpunpack: Command;
export const runNextpnrEcp5: Command;

export const commands: {
    'ecppll': Command,
    'ecpbram': Command,
    'ecpmulti': Command,
    'ecppack': Command,
    'ecpunpack': Command,
    'nextpnr-ecp5': Command,
};
