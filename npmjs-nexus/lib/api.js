import { Application } from '@yowasp/runtime';
import { instantiate as instantiatePrjoxide } from '../gen/prjoxide.js';
import { instantiate as instantiateNextpnrNexus } from '../gen/nextpnr-nexus.js';

export { Exit } from '@yowasp/runtime';

const resourceFileURL = new URL('./resources-nextpnr-nexus.js', import.meta.url);

const prjoxide = new Application(resourceFileURL, instantiatePrjoxide, 'yowasp-prjoxide');
const runPrjoxide = prjoxide.run.bind(prjoxide);

const nextpnrNexus = new Application(resourceFileURL, instantiateNextpnrNexus, 'yowasp-nextpnr-nexus');
const runNextpnrNexus = nextpnrNexus.run.bind(nextpnrNexus);

export {
    runPrjoxide,
    runNextpnrNexus,
};

export const commands = {
    'prjoxide': runPrjoxide,
    'nextpnr-nexus': runNextpnrNexus,
};
