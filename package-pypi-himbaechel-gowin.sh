#!/bin/sh -ex

PYTHON=${PYTHON:-python}

cd $(dirname $0)

cd pypi-himbaechel-gowin
rm -rf build && ${PYTHON} -m build -w
sha256sum dist/*.whl
