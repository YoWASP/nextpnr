#!/bin/sh -ex

PYTHON=${PYTHON:-python}

cd $(dirname $0)

mkdir -p pypi-machxo2/yowasp_nextpnr_machxo2/bin/
cp prjtrellis-build/ecppll.wasm \
   prjtrellis-build/ecpbram.wasm \
   prjtrellis-build/ecpmulti.wasm \
   prjtrellis-build/ecppack.wasm \
   prjtrellis-build/ecpunpack.wasm \
   nextpnr-build/nextpnr-machxo2.wasm \
   pypi-machxo2/yowasp_nextpnr_machxo2/
mkdir -p pypi-machxo2/yowasp_nextpnr_machxo2/share/machxo2
cp nextpnr-build/machxo2/chipdb/*.bin \
   pypi-machxo2/yowasp_nextpnr_machxo2/share/machxo2
mkdir -p pypi-machxo2/yowasp_nextpnr_machxo2/share/trellis/database
cp -r prjtrellis-src/database/MachXO* \
   prjtrellis-src/database/devices.json \
   pypi-machxo2/yowasp_nextpnr_machxo2/share/trellis/database

cd pypi-machxo2
rm -rf build && ${PYTHON} -m build -w
sha256sum dist/*.whl
