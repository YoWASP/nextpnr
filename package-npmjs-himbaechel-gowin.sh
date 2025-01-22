#!/bin/sh -ex

cd $(dirname $0)

PYTHON=${PYTHON:-python}

cd npmjs-himbaechel-gowin
${PYTHON} prepare.py himbaechel-gowin
npm install
npm run all

mkdir -p dist
npm pack --pack-destination dist
