import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "pypi-common"))

from setuptools import setup
from yowasp_nextpnr_version import version
import importlib.metadata


setup(
    version=version(),
    install_requires=[
        "yowasp-runtime~=1.1",
        "Apycula=={}".format(importlib.metadata.version("apycula"))
    ],
)
