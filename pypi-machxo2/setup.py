import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "pypi-common"))

from setuptools import setup
from yowasp_nextpnr_version import version


setup(
    version=version(),
)
