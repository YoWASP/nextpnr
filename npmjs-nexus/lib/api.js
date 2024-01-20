import { Application } from '@yowasp/runtime';
import { instantiate as instantiatePrjoxide } from '../gen/prjoxide.js';
import { instantiate as instantiateNextpnrNexus } from '../gen/nextpnr-nexus.js';

export { Exit } from '@yowasp/runtime';

const resources = () => import('./resources-nextpnr-nexus.js');

const prjoxide = new Application(resources, instantiatePrjoxide, 'yowasp-prjoxide');
const runPrjoxide = prjoxide.run.bind(prjoxide);

const nextpnrNexus = new Application(resources, instantiateNextpnrNexus, 'yowasp-nextpnr-nexus');
const runNextpnrNexus = nextpnrNexus.run.bind(nextpnrNexus);

export {
    runPrjoxide,
    runNextpnrNexus,
};

export const commands = {
    'prjoxide': runPrjoxide,
    'nextpnr-nexus': runNextpnrNexus,
};
