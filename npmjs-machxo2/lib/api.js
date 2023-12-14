import { Application } from '@yowasp/runtime';
import { instantiate as instantiateEcppll } from '../gen/ecppll.js';
import { instantiate as instantiateEcpbram } from '../gen/ecpbram.js';
import { instantiate as instantiateEcpmulti } from '../gen/ecpmulti.js';
import { instantiate as instantiateEcppack } from '../gen/ecppack.js';
import { instantiate as instantiateEcpunpack } from '../gen/ecpunpack.js';
import { instantiate as instantiateNextpnrMachxo2 } from '../gen/nextpnr-machxo2.js';

export { Exit } from '@yowasp/runtime';

const resourceFileURL = new URL('./resources-nextpnr-machxo2.js', import.meta.url);

const ecppll = new Application(resourceFileURL, instantiateEcppll, 'yowasp-ecppll');
const runEcppll = ecppll.run.bind(ecppll);

const ecpbram = new Application(resourceFileURL, instantiateEcpbram, 'yowasp-ecpbram');
const runEcpbram = ecpbram.run.bind(ecpbram);

const ecpmulti = new Application(resourceFileURL, instantiateEcpmulti, 'yowasp-ecpmulti');
const runEcpmulti = ecpmulti.run.bind(ecpmulti);

const ecppack = new Application(resourceFileURL, instantiateEcppack, 'yowasp-ecppack');
const runEcppack = ecppack.run.bind(ecppack);

const ecpunpack = new Application(resourceFileURL, instantiateEcpunpack, 'yowasp-ecpunpack');
const runEcpunpack = ecpunpack.run.bind(ecpunpack);

const nextpnrMachxo2 = new Application(resourceFileURL, instantiateNextpnrMachxo2, 'yowasp-nextpnr-machxo2');
const runNextpnrMachxo2 = nextpnrMachxo2.run.bind(nextpnrMachxo2);

export {
    runEcppll,
    runEcpbram,
    runEcpmulti,
    runEcppack,
    runEcpunpack,
    runNextpnrMachxo2,
};

export const commands = {
    'ecppll': runEcppll,
    'ecpbram': runEcpbram,
    'ecpmulti': runEcpmulti,
    'ecppack': runEcppack,
    'ecpunpack': runEcpunpack,
    'nextpnr-machxo2': runNextpnrMachxo2,
};
