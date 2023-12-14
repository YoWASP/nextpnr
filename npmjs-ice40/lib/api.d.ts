export type Tree = {
    [name: string]: Tree | string | Uint8Array
};

export class Exit extends Error {
    code: number;
    files: Tree;
}

export type Command = (args?: string[], files?: Tree, options?: {
    printLine?: (line: string) => void,
    decodeASCII?: boolean
}) => Promise<Tree>;


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
