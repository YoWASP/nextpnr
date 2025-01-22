import sys
import yowasp_runtime


def run_nextpnr_himbaechel_gowin(argv):
    return yowasp_runtime.run_wasm(__package__, "nextpnr-himbaechel-gowin.wasm", resources=["share"],
        argv=["yowasp-nextpnr-himbaechel-gowin", *argv])


def _run_nextpnr_himbaechel_gowin_argv():
    sys.exit(run_nextpnr_himbaechel_gowin(sys.argv[1:]))
