import { Application } from '@yowasp/runtime';
import { instantiate as instantiateIcepll } from '../gen/icepll.js';
import { instantiate as instantiateIcebram } from '../gen/icebram.js';
import { instantiate as instantiateIcemulti } from '../gen/icemulti.js';
import { instantiate as instantiateIcepack } from '../gen/icepack.js';
import { instantiate as instantiateNextpnrIce40 } from '../gen/nextpnr-ice40.js';

export { Exit } from '@yowasp/runtime';

const resources = () => import('./resources-nextpnr-ice40.js');

const icepll = new Application(resources, instantiateIcepll, 'yowasp-icepll');
const runIcepll = icepll.run.bind(icepll);

const icebram = new Application(resources, instantiateIcebram, 'yowasp-icebram');
const runIcebram = icebram.run.bind(icebram);

const icemulti = new Application(resources, instantiateIcemulti, 'yowasp-icemulti');
const runIcemulti = icemulti.run.bind(icemulti);

const icepack = new Application(resources, instantiateIcepack, 'yowasp-icepack');
const runIcepack = icepack.run.bind(icepack);

const iceunpack = new Application(resources, instantiateIcepack, 'yowasp-iceunpack');
const runIceunpack = iceunpack.run.bind(iceunpack);

const nextpnrIce40 = new Application(resources, instantiateNextpnrIce40, 'yowasp-nextpnr-ice40');
const runNextpnrIce40 = nextpnrIce40.run.bind(nextpnrIce40);

export {
    runIcepll,
    runIcebram,
    runIcemulti,
    runIcepack,
    runIceunpack,
    runNextpnrIce40,
};

export const commands = {
    'icepll': runIcepll,
    'icebram': runIcebram,
    'icemulti': runIcemulti,
    'icepack': runIcepack,
    'iceunpack': runIceunpack,
    'nextpnr-ice40': runNextpnrIce40,
};
