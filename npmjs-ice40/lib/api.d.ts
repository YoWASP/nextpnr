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

export const runIcepll: Command;
export const runIcebram: Command;
export const runIcemulti: Command;
export const runIcepack: Command;
export const runIceunpack: Command;
export const runNextpnrIce40: Command;

export const commands: {
    'icepll': Command,
    'icebram': Command,
    'icemulti': Command,
    'icepack': Command,
    'iceunpack': Command,
    'nextpnr-ice40': Command,
};
