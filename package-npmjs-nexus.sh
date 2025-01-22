#!/bin/sh -ex

cd $(dirname $0)

PYTHON=${PYTHON:-python}

cd npmjs-nexus
${PYTHON} prepare.py nexus
npm install
npm run all

mkdir -p dist
npm pack --pack-destination dist
