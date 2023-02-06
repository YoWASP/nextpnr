import sys
import yowasp_runtime


def run_prjoxide(argv):
    return yowasp_runtime.run_wasm(__package__, "prjoxide.wasm",
        argv=["yowasp-prjoxide", *argv])


def _run_prjoxide_argv():
    sys.exit(run_prjoxide(sys.argv[1:]))


def run_nextpnr_nexus(argv):
    return yowasp_runtime.run_wasm(__package__, "nextpnr-nexus.wasm", resources=["share"],
        argv=["yowasp-nextpnr-nexus", *argv])


def _run_nextpnr_nexus_argv():
    sys.exit(run_nextpnr_nexus(sys.argv[1:]))
