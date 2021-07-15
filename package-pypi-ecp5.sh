#!/bin/sh -ex

PYTHON=${PYTHON:-python}

mkdir -p pypi-ecp5/yowasp_nextpnr_ecp5/bin/
cp prjtrellis-build/ecppll.wasm \
   prjtrellis-build/ecpbram.wasm \
   prjtrellis-build/ecpmulti.wasm \
   prjtrellis-build/ecppack.wasm \
   prjtrellis-build/ecpunpack.wasm \
   nextpnr-build/nextpnr-ecp5.wasm \
   pypi-ecp5/yowasp_nextpnr_ecp5/
mkdir -p pypi-ecp5/yowasp_nextpnr_ecp5/share/ecp5
cp nextpnr-build/ecp5/chipdb/*.bin \
   pypi-ecp5/yowasp_nextpnr_ecp5/share/ecp5
mkdir -p pypi-ecp5/yowasp_nextpnr_ecp5/share/trellis/database
cp -r prjtrellis-src/database/ECP5 \
   prjtrellis-src/database/devices.json \
   pypi-ecp5/yowasp_nextpnr_ecp5/share/trellis/database

cd pypi-ecp5
rm -rf build && ${PYTHON} setup.py bdist_wheel
rm -rf build && ALIAS=25k ${PYTHON} setup.py bdist_wheel
rm -rf build && ALIAS=45k ${PYTHON} setup.py bdist_wheel
rm -rf build && ALIAS=85k ${PYTHON} setup.py bdist_wheel
rm -rf build && ALIAS=all ${PYTHON} setup.py bdist_wheel
sha256sum dist/*.whl
