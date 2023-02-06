import sys
import yowasp_runtime


def run_ecppll(argv):
    return yowasp_runtime.run_wasm(__package__, "ecppll.wasm",
        argv=["yowasp-ecppll", *argv])


def _run_ecppll_argv():
    sys.exit(run_ecppll(sys.argv[1:]))


def run_ecpbram(argv):
    return yowasp_runtime.run_wasm(__package__, "ecpbram.wasm",
        argv=["yowasp-ecpbram", *argv])


def _run_ecpbram_argv():
    sys.exit(run_ecpbram(sys.argv[1:]))


def run_ecpmulti(argv):
    return yowasp_runtime.run_wasm(__package__, "ecpmulti.wasm",
        argv=["yowasp-ecpmulti", *argv])


def _run_ecpmulti_argv():
    sys.exit(run_ecpmulti(sys.argv[1:]))


def run_ecppack(argv):
    return yowasp_runtime.run_wasm(__package__, "ecppack.wasm", resources=["share"],
        argv=["yowasp-ecppack", *argv])


def _run_ecppack_argv():
    sys.exit(run_ecppack(sys.argv[1:]))


def run_ecpunpack(argv):
    return yowasp_runtime.run_wasm(__package__, "ecpunpack.wasm", resources=["share"],
        argv=["yowasp-ecpunpack", *argv])


def _run_ecpunpack_argv():
    sys.exit(run_ecpunpack(sys.argv[1:]))


def run_nextpnr_ecp5(argv):
    return yowasp_runtime.run_wasm(__package__, "nextpnr-ecp5.wasm", resources=["share"],
        argv=["yowasp-nextpnr-ecp5", *argv])


def _run_nextpnr_ecp5_argv():
    sys.exit(run_nextpnr_ecp5(sys.argv[1:]))
