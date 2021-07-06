import os
from setuptools import setup, find_packages
from setuptools_scm.git import parse as parse_git


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


def long_description():
    with open("../README.md") as f:
        return f.read()


setup_info = dict(
    name="yowasp-nextpnr-nexus",
    version=version(),
    install_requires=[
        "importlib_resources; python_version<'3.9'",
        "appdirs~=1.4",
        "wasmtime>=0.20,<0.28"
    ],
    packages=["yowasp_nextpnr_nexus"],
    package_data={
        "yowasp_nextpnr_nexus": [
            "*.wasm",
            "share/nexus/chipdb-*.bin",
        ],
    },
    entry_points={
        "console_scripts": [
            "yowasp-prjoxide = yowasp_nextpnr_nexus:_run_prjoxide_argv",
            "yowasp-nextpnr-nexus = yowasp_nextpnr_nexus:_run_nextpnr_nexus_argv",
        ],
    },
)


setup(
    author="whitequark",
    author_email="whitequark@whitequark.org",
    description="nextpnr-nexus FPGA place and route tool",
    long_description=long_description(),
    long_description_content_type="text/markdown",
    license="ISC", # same as Yosys
    python_requires="~=3.5",
    setup_requires=["setuptools_scm", "wheel"],
    **setup_info,
    project_urls={
        "Homepage": "https://yowasp.github.io/",
        "Source Code": "https://github.com/YoWASP/nextpnr",
        "Bug Tracker": "https://github.com/YoWASP/nextpnr/issues",
    },
    classifiers=[
        "License :: OSI Approved :: ISC License (ISCL)",
    ],
)
