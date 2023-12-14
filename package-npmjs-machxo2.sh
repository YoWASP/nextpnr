#!/bin/sh -ex

cd $(dirname $0)

PYTHON=${PYTHON:-python}

mkdir -p npmjs-machxo2/share/machxo2
cp nextpnr-build/machxo2/chipdb/*.bin \
   npmjs-machxo2/share/machxo2
mkdir -p npmjs-machxo2/share/trellis/database
cp -r prjtrellis-src/database/MachXO* \
   prjtrellis-src/database/devices.json \
   npmjs-machxo2/share/trellis/database

cd npmjs-machxo2
${PYTHON} prepare.py machxo2
npm install
npm run all

mkdir -p dist
npm pack --pack-destination dist
