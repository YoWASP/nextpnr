#!/bin/sh -ex

PYTHON=${PYTHON:-python}

mkdir -p pypi-ice40/yowasp_nextpnr_ice40/bin/
cp icestorm-prefix/bin/icepll.wasm \
   icestorm-prefix/bin/icebram.wasm \
   icestorm-prefix/bin/icemulti.wasm \
   icestorm-prefix/bin/icepack.wasm \
   nextpnr-build/nextpnr-ice40.wasm \
   pypi-ice40/yowasp_nextpnr_ice40/
mkdir -p pypi-ice40/yowasp_nextpnr_ice40/share/ice40
cp nextpnr-build/ice40/chipdb/*.bin \
   pypi-ice40/yowasp_nextpnr_ice40/share/ice40

cd pypi-ice40
rm -rf build && ${PYTHON} -m build -w
sha256sum dist/*.whl
