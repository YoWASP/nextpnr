#!/bin/sh -ex

cd $(dirname $0)

PYTHON=${PYTHON:-python}

cd npmjs-ecp5
${PYTHON} prepare.py ecp5
npm install
npm run all

mkdir -p dist
npm pack --pack-destination dist
