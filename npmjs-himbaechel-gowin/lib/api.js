import { Application } from '@yowasp/runtime';
import { PythonApplication } from './pyodide.js';
import { instantiate as instantiateNextpnrHimbaechelGowin } from '../gen/nextpnr-himbaechel-gowin.js';

export { Exit } from '@yowasp/runtime';

const resources = () => import('./resources-nextpnr-himbaechel-gowin.js');

const executeApycula = (pyodide, argv0) => pyodide.runPython(`
import sys; sys.path.append('/share/python')
from apycula.${argv0} import main; main()
`);

const gowinPll = new PythonApplication(resources, executeApycula, 'gowin_pll');
const runGowinPll = gowinPll.run.bind(gowinPll);

const gowinPack = new PythonApplication(resources, executeApycula, 'gowin_pack');
const runGowinPack = gowinPack.run.bind(gowinPack);

const gowinUnpack = new PythonApplication(resources, executeApycula, 'gowin_unpack');
const runGowinUnpack = gowinUnpack.run.bind(gowinUnpack);

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

export const version = VERSION;
