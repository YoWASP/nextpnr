import sys
import yowasp_runtime


def run_icepll(argv):
    return yowasp_runtime.run_wasm(__package__, "icepll.wasm",
        argv=["yowasp-icepll", *argv])


def _run_icepll_argv():
    sys.exit(run_icepll(sys.argv[1:]))


def run_icebram(argv):
    return yowasp_runtime.run_wasm(__package__, "icebram.wasm",
        argv=["yowasp-icebram", *argv])


def _run_icebram_argv():
    sys.exit(run_icebram(sys.argv[1:]))


def run_icemulti(argv):
    return yowasp_runtime.run_wasm(__package__, "icemulti.wasm",
        argv=["yowasp-icemulti", *argv])


def _run_icemulti_argv():
    sys.exit(run_icemulti(sys.argv[1:]))


def run_icepack(argv):
    return yowasp_runtime.run_wasm(__package__, "icepack.wasm",
        argv=["yowasp-icepack", *argv])


def _run_icepack_argv():
    sys.exit(run_icepack(sys.argv[1:]))


def run_iceunpack(argv):
    # same binary as icepack, operation distinguished with argv[0]
    return yowasp_runtime.run_wasm(__package__, "icepack.wasm",
        argv=["yowasp-iceunpack", *argv])


def _run_iceunpack_argv():
    sys.exit(run_iceunpack(sys.argv[1:]))


def run_nextpnr_ice40(argv):
    return yowasp_runtime.run_wasm(__package__, "nextpnr-ice40.wasm", resources=["share"],
        argv=["yowasp-nextpnr-ice40", *argv])


def _run_nextpnr_ice40_argv():
    sys.exit(run_nextpnr_ice40(sys.argv[1:]))
