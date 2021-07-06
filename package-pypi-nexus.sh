#!/bin/sh -ex

PYTHON=${PYTHON:-python}

mkdir -p pypi-nexus/yowasp_nextpnr_nexus/bin/
cp prjoxide-build/wasm32-wasi/release/prjoxide.wasm \
   nextpnr-build/nextpnr-nexus.wasm \
   pypi-nexus/yowasp_nextpnr_nexus/
mkdir -p pypi-nexus/yowasp_nextpnr_nexus/share/nexus
cp nextpnr-build/nexus/chipdb/*.bin \
   pypi-nexus/yowasp_nextpnr_nexus/share/nexus

cd pypi-nexus
rm -rf build && ${PYTHON} setup.py bdist_wheel
sha256sum dist/*.whl
