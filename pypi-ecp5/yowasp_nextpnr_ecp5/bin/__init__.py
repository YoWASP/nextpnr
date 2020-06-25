import os
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
    wasi_cfg.argv = (os.path.basename(argv[0]), *argv[1:])
    wasi_cfg.preopen_dir(str(importlib_resources.files(__package__).parent / "share"), "/share")
    wasi_cfg.preopen_dir("/", "/")
    wasi_cfg.preopen_dir(".", ".")
    wasi_cfg.inherit_stdin()
    wasi_cfg.inherit_stdout()
    wasi_cfg.inherit_stderr()

    store = wasmtime.Store(wasmtime.Engine(wasm_cfg))
    linker = wasmtime.Linker(store)
    wasi = linker.define_wasi(wasmtime.WasiInstance(store,
        "wasi_snapshot_preview1", wasi_cfg))
    app = linker.instantiate(wasmtime.Module(store,
        importlib_resources.read_binary(__package__, wasm_filename)))
    try:
        app.exports["_start"]()
        return 0
    except wasmtime.ExitTrap as trap:
        return trap.code


def run_ecppll(argv=sys.argv):
    sys.exit(_run_wasm_app("ecppll.wasm", argv))


def run_ecpbram(argv=sys.argv):
    sys.exit(_run_wasm_app("ecpbram.wasm", argv))


def run_ecpmulti(argv=sys.argv):
    sys.exit(_run_wasm_app("ecpmulti.wasm", argv))


def run_ecppack(argv=sys.argv):
    sys.exit(_run_wasm_app("ecppack.wasm", argv))


def run_ecpunpack(argv=sys.argv):
    sys.exit(_run_wasm_app("ecpunpack.wasm", argv))


def run_nextpnr_ecp5(argv=sys.argv):
    sys.exit(_run_wasm_app("nextpnr-ecp5.wasm", argv))
