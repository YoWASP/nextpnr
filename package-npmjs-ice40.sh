#!/bin/sh -ex

cd $(dirname $0)

PYTHON=${PYTHON:-python}

mkdir -p npmjs-ice40/share/ice40
cp nextpnr-build/ice40/chipdb/*.bin \
   npmjs-ice40/share/ice40

cd npmjs-ice40
${PYTHON} prepare.py ice40
npm install
npm run all

mkdir -p dist
npm pack --pack-destination dist
