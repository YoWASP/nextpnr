import sys
import yowasp_runtime


def run_nextpnr_gowin(argv):
    return yowasp_runtime.run_wasm(__package__, "nextpnr-gowin.wasm", resources=["share"],
        argv=["yowasp-nextpnr-gowin", *argv])


def _run_nextpnr_gowin_argv():
    sys.exit(run_nextpnr_gowin(sys.argv[1:]))
