export type Tree = {
    [name: string]: Tree | string | Uint8Array
};

export type OutputStream =
    (bytes: Uint8Array | null) => void;

export class Exit extends Error {
    code: number;
    files: Tree;
}

export type Command = (args?: string[], files?: Tree, options?: {
    stdout?: OutputStream | null,
    stderr?: OutputStream | null,
    decodeASCII?: boolean
}) => Promise<Tree>;


export const runEcppll: Command;
export const runEcpbram: Command;
export const runEcpmulti: Command;
export const runEcppack: Command;
export const runEcpunpack: Command;
export const runNextpnrMachxo2: Command;

export const commands: {
    'ecppll': Command,
    'ecpbram': Command,
    'ecpmulti': Command,
    'ecppack': Command,
    'ecpunpack': Command,
    'nextpnr-machxo2': Command,
};
