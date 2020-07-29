import sys
import wasmtime
try:
    from importlib import resources as importlib_resources
    try:
        importlib_resources.files # py3.9+ stdlib
    except AttributeError:
        import importlib_resources # py3.8- shim
except ImportError:
    import importlib_resources # py3.6- shim


def _run_wasm_app(wasm_filename, argv):
    wasm_cfg = wasmtime.Config()
    wasm_cfg.cache = True

    wasi_cfg = wasmtime.WasiConfig()
    wasi_cfg.argv = argv
    wasi_cfg.preopen_dir(str(importlib_resources.files(__package__) / "share"), "/share")
    wasi_cfg.preopen_dir("/", "/")
    wasi_cfg.preopen_dir(".", ".")
    wasi_cfg.inherit_stdin()
    wasi_cfg.inherit_stdout()
    wasi_cfg.inherit_stderr()

    store = wasmtime.Store(wasmtime.Engine(wasm_cfg))
    linker = wasmtime.Linker(store)
    wasi = linker.define_wasi(wasmtime.WasiInstance(store,
        "wasi_snapshot_preview1", wasi_cfg))
    app = linker.instantiate(wasmtime.Module(store.engine,
        importlib_resources.read_binary(__package__, wasm_filename)))
    try:
        app.exports["_start"]()
        return 0
    except wasmtime.ExitTrap as trap:
        return trap.code


def run_ecppll(argv):
    return _run_wasm_app("ecppll.wasm", ["yowasp-ecppll", *argv])


def _run_ecppll_argv():
    sys.exit(run_ecppll(sys.argv[1:]))


def run_ecpbram(argv):
    return _run_wasm_app("ecpbram.wasm", ["yowasp-ecpbram", *argv])


def _run_ecpbram_argv():
    sys.exit(run_ecpbram(sys.argv[1:]))


def run_ecpmulti(argv):
    return _run_wasm_app("ecpmulti.wasm", ["yowasp-ecpmulti", *argv])


def _run_ecpmulti_argv():
    sys.exit(run_ecpmulti(sys.argv[1:]))


def run_ecppack(argv):
    return _run_wasm_app("ecppack.wasm", ["yowasp-ecppack", *argv])


def _run_ecppack_argv():
    sys.exit(run_ecppack(sys.argv[1:]))


def run_ecpunpack(argv):
    return _run_wasm_app("ecpunpack.wasm", ["yowasp-ecpunpack", *argv])


def _run_ecpunpack_argv():
    sys.exit(run_ecpunpack(sys.argv[1:]))


def run_nextpnr_ecp5(argv):
    return _run_wasm_app("nextpnr-ecp5.wasm", ["yowasp-nextpnr-ecp5", *argv])


def _run_nextpnr_ecp5_argv():
    sys.exit(run_nextpnr_ecp5(sys.argv[1:]))
