#!/bin/sh -ex

cd $(dirname $0)

PYTHON=${PYTHON:-python}

mkdir -p npmjs-ecp5/share/ecp5
cp nextpnr-build/ecp5/chipdb/*.bin \
   npmjs-ecp5/share/ecp5
mkdir -p npmjs-ecp5/share/trellis/database
cp -r prjtrellis-src/database/ECP5 \
   prjtrellis-src/database/devices.json \
   npmjs-ecp5/share/trellis/database

cd npmjs-ecp5
${PYTHON} prepare.py ecp5
npm install
npm run all

mkdir -p dist
npm pack --pack-destination dist
