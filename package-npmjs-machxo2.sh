#!/bin/sh -ex

cd $(dirname $0)

PYTHON=${PYTHON:-python}

cd npmjs-machxo2
${PYTHON} prepare.py machxo2
npm install
npm run all

mkdir -p dist
npm pack --pack-destination dist
