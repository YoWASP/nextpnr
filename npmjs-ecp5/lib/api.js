import { Application } from '@yowasp/runtime';
import { instantiate as instantiateEcppll } from '../gen/ecppll.js';
import { instantiate as instantiateEcpbram } from '../gen/ecpbram.js';
import { instantiate as instantiateEcpmulti } from '../gen/ecpmulti.js';
import { instantiate as instantiateEcppack } from '../gen/ecppack.js';
import { instantiate as instantiateEcpunpack } from '../gen/ecpunpack.js';
import { instantiate as instantiateNextpnrEcp5 } from '../gen/nextpnr-ecp5.js';

export { Exit } from '@yowasp/runtime';

const resources = () => import('./resources-nextpnr-ecp5.js');

const ecppll = new Application(resources, instantiateEcppll, 'yowasp-ecppll');
const runEcppll = ecppll.run.bind(ecppll);

const ecpbram = new Application(resources, instantiateEcpbram, 'yowasp-ecpbram');
const runEcpbram = ecpbram.run.bind(ecpbram);

const ecpmulti = new Application(resources, instantiateEcpmulti, 'yowasp-ecpmulti');
const runEcpmulti = ecpmulti.run.bind(ecpmulti);

const ecppack = new Application(resources, instantiateEcppack, 'yowasp-ecppack');
const runEcppack = ecppack.run.bind(ecppack);

const ecpunpack = new Application(resources, instantiateEcpunpack, 'yowasp-ecpunpack');
const runEcpunpack = ecpunpack.run.bind(ecpunpack);

const nextpnrEcp5 = new Application(resources, instantiateNextpnrEcp5, 'yowasp-nextpnr-ecp5');
const runNextpnrEcp5 = nextpnrEcp5.run.bind(nextpnrEcp5);

export {
    runEcppll,
    runEcpbram,
    runEcpmulti,
    runEcppack,
    runEcpunpack,
    runNextpnrEcp5,
};

export const commands = {
    'ecppll': runEcppll,
    'ecpbram': runEcpbram,
    'ecpmulti': runEcpmulti,
    'ecppack': runEcppack,
    'ecpunpack': runEcpunpack,
    'nextpnr-ecp5': runNextpnrEcp5,
};
