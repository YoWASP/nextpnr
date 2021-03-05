import os
import sys
import wasmtime
import pathlib
import hashlib
import appdirs
try:
    from importlib import resources as importlib_resources
    try:
        importlib_resources.files # py3.9+ stdlib
    except AttributeError:
        import importlib_resources # py3.8- shim
except ImportError:
    import importlib_resources # py3.6- shim


def _run_wasm_app(wasm_filename, argv):
    module_binary = importlib_resources.read_binary(__package__, wasm_filename)
    module_digest = hashlib.sha1(module_binary).digest()

    wasi_cfg = wasmtime.WasiConfig()
    wasi_cfg.argv = argv
    wasi_cfg.preopen_dir(str(importlib_resources.files(__package__) / "share"), "/share")
    wasi_cfg.preopen_dir("/", "/")
    wasi_cfg.preopen_dir(".", ".")
    wasi_cfg.inherit_stdin()
    wasi_cfg.inherit_stdout()
    wasi_cfg.inherit_stderr()

    engine = wasmtime.Engine()
    cache_path = pathlib.Path(os.getenv("YOWASP_CACHE_DIR", appdirs.user_cache_dir("yowasp")))
    cache_path.mkdir(parents=True, exist_ok=True)
    cache_filename = (cache_path / "{}-cache".format(wasm_filename))
    digest_filename = (cache_path / "{}-digest".format(wasm_filename))
    try:
        with digest_filename.open("rb") as digest_file:
            if digest_file.read() != module_digest:
                raise Exception("cache miss")
        with cache_filename.open("rb") as cache_file:
            module = wasmtime.Module.deserialize(engine, cache_file.read())
    except:
        print("Preparing to run {}. This might take a while...".format(argv[0]), file=sys.stderr)
        module = wasmtime.Module(engine, module_binary)
        with cache_filename.open("wb") as cache_file:
            cache_file.write(module.serialize())
        with digest_filename.open("wb") as digest_file:
            digest_file.write(module_digest)

    store = wasmtime.Store(engine)
    linker = wasmtime.Linker(store)
    wasi = linker.define_wasi(wasmtime.WasiInstance(store,
        "wasi_snapshot_preview1", wasi_cfg))
    app = linker.instantiate(module)
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
