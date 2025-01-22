#!/bin/sh -ex

cd $(dirname $0)

PYTHON=${PYTHON:-python}

cd npmjs-ice40
${PYTHON} prepare.py ice40
npm install
npm run all

mkdir -p dist
npm pack --pack-destination dist
