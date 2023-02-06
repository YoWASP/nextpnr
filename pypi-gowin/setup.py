from setuptools import setup, find_packages
from setuptools_scm.git import parse as parse_git
import importlib.metadata


def version():
    upstream_git = parse_git("../nextpnr-src")
    if upstream_git.exact:
        nextpnr_version = upstream_git.format_with("{tag}")
    else:
        nextpnr_version = upstream_git.format_with("{tag}.post{distance}")

    package_git = parse_git("..")
    if not package_git.dirty:
        package_version = package_git.format_with(".dev{distance}")
    else:
        package_version = package_git.format_with(".dev{distance}+dirty")

    return nextpnr_version + package_version


setup(
    version=version(),
    install_requires=[
        "yowasp-runtime~=1.1",
        "Apycula=={}".format(importlib.metadata.version("apycula"))
    ],
)
