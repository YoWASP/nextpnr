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


def run_prjoxide(argv):
    return _run_wasm_app("prjoxide.wasm", ["yowasp-prjoxide", *argv])


def _run_prjoxide_argv():
    sys.exit(run_prjoxide(sys.argv[1:]))


def run_nextpnr_nexus(argv):
    return _run_wasm_app("nextpnr-nexus.wasm", ["yowasp-nextpnr-nexus", *argv])


def _run_nextpnr_nexus_argv():
    sys.exit(run_nextpnr_nexus(sys.argv[1:]))
