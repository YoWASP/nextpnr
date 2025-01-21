#!/bin/sh -ex

cd $(dirname $0)

PYTHON=${PYTHON:-python}

mkdir -p npmjs-nexus/share/nexus
cp -r nextpnr-build/share/nexus/* \
   npmjs-nexus/share/nexus

cd npmjs-nexus
${PYTHON} prepare.py nexus
npm install
npm run all

mkdir -p dist
npm pack --pack-destination dist
