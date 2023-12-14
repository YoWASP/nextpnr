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


export const runPrjoxide: Command;
export const runNextpnrNexus: Command;

export const commands: {
    'prjoxide': Command,
    'nextpnr-nexus': Command,
};
