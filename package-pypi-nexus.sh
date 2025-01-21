#!/bin/sh -ex

PYTHON=${PYTHON:-python}

cd $(dirname $0)

mkdir -p pypi-nexus/yowasp_nextpnr_nexus/bin/
cp prjoxide-build/wasm32-wasip1/release/prjoxide.wasm \
   nextpnr-build/nextpnr-nexus.wasm \
   pypi-nexus/yowasp_nextpnr_nexus/
mkdir -p pypi-nexus/yowasp_nextpnr_nexus/share/nexus
cp -r nextpnr-build/share/nexus/* \
   pypi-nexus/yowasp_nextpnr_nexus/share/nexus

cd pypi-nexus
rm -rf build && ${PYTHON} -m build -w
sha256sum dist/*.whl
