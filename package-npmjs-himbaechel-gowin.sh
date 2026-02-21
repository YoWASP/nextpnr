#!/bin/sh -ex

cd $(dirname $0)

PYTHON=${PYTHON:-python}

export APYCULA_WHEEL="$(cat apycula-meta/requirements.txt)"
rm -rf npmjs-himbaechel-gowin/share/python
mkdir -p npmjs-himbaechel-gowin/share/python
(cd npmjs-himbaechel-gowin/share/python && pip download --no-deps $APYCULA_WHEEL)

cd npmjs-himbaechel-gowin
${PYTHON} prepare.py himbaechel-gowin
npm install
npm run all

mkdir -p dist
npm pack --pack-destination dist
