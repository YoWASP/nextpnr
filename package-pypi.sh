#!/bin/sh -ex

PYTHON=${PYTHON:-python}

mkdir -p pypi/yowasp_nextpnr_ice40/bin/
cp icestorm-prefix/bin/icepll.wasm \
	icestorm-prefix/bin/icebram.wasm \
	icestorm-prefix/bin/icemulti.wasm \
	icestorm-prefix/bin/icepack.wasm \
	nextpnr-build/nextpnr-ice40.wasm \
	pypi/yowasp_nextpnr_ice40/bin/
mkdir -p pypi/yowasp_nextpnr_ice40/share/ice40
cp nextpnr-build/ice40/chipdb/*.bin \
	pypi/yowasp_nextpnr_ice40/share/ice40

cd pypi
${PYTHON} setup.py bdist_wheel
rm -rf build && DEVICE=384 ${PYTHON} setup.py bdist_wheel
rm -rf build && DEVICE=1k ${PYTHON} setup.py bdist_wheel
rm -rf build && DEVICE=5k ${PYTHON} setup.py bdist_wheel
rm -rf build && DEVICE=8k ${PYTHON} setup.py bdist_wheel
rm -rf build && DEVICE=u4k ${PYTHON} setup.py bdist_wheel
rm -rf build && DEVICE=384,1k,5k,8k,u4k ${PYTHON} setup.py bdist_wheel
sha256sum dist/*.whl
