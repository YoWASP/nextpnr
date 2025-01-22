import { Application } from '@yowasp/runtime';
import { instantiate as instantiateNextpnrHimbaechelGowin } from '../gen/nextpnr-himbaechel-gowin.js';

export { Exit } from '@yowasp/runtime';

const resources = () => import('./resources-nextpnr-himbaechel-gowin.js');

const runGowinPll = () => { throw new Error("unimplemented") };
const runGowinPack = () => { throw new Error("unimplemented") };
const runGowinUnpack = () => { throw new Error("unimplemented") };

const nextpnrHimbaechelGowin = new Application(resources, instantiateNextpnrHimbaechelGowin, 'yowasp-nextpnr-himbaechel-gowin');
const runNextpnrHimbaechelGowin = nextpnrHimbaechelGowin.run.bind(nextpnrHimbaechelGowin);

export {
    runGowinPll,
    runGowinPack,
    runGowinUnpack,
    runNextpnrHimbaechelGowin,
};

export const commands = {
    'gowin_pll': runGowinPll,
    'gowin_pack': runGowinPack,
    'gowin_unpack': runGowinUnpack,
    'nextpnr-himbaechel-gowin': runNextpnrHimbaechelGowin,
};
