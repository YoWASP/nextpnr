#!/bin/sh -ex

cd $(dirname $0)

PYTHON=${PYTHON:-python}

PYTHON_LIBNAME=$(basename $(readlink -f apycula-prefix/bin/python))
rm -rf npmjs-himbaechel-gowin/share/python
mkdir -p npmjs-himbaechel-gowin/share/python/apycula
cp -r apycula-prefix/lib/${PYTHON_LIBNAME}/site-packages/apycula/*.py \
   npmjs-himbaechel-gowin/share/python/apycula
cp -r apycula-prefix/lib/${PYTHON_LIBNAME}/site-packages/apycula/*.pickle \
   npmjs-himbaechel-gowin/share/python/apycula
cp -r apycula-prefix/lib/${PYTHON_LIBNAME}/site-packages/crc/_crc.py \
   npmjs-himbaechel-gowin/share/python/crc.py

cd npmjs-himbaechel-gowin
${PYTHON} prepare.py himbaechel-gowin
npm install
npm run all

mkdir -p dist
npm pack --pack-destination dist
