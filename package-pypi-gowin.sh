#!/bin/sh -ex

PYTHON=${PYTHON:-python}

cd $(dirname $0)

mkdir -p pypi-gowin/yowasp_nextpnr_gowin/bin/
cp nextpnr-build/nextpnr-gowin.wasm \
   pypi-gowin/yowasp_nextpnr_gowin/
mkdir -p pypi-gowin/yowasp_nextpnr_gowin/share/gowin
cp nextpnr-build/gowin/chipdb/*.bin \
   pypi-gowin/yowasp_nextpnr_gowin/share/gowin

cd pypi-gowin
rm -rf build && ${PYTHON} -m build -w
sha256sum dist/*.whl
