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
    name="yowasp-nextpnr-ice40",
    version=version(),
    long_description=long_description(),
    long_description_content_type="text/markdown",
    install_requires=[
        "yowasp-runtime~=1.1"
    ],
    packages=["yowasp_nextpnr_ice40"],
    package_data={"yowasp_nextpnr_ice40": [
        "*.wasm",
        "share/ice40/chipdb-*.bin"
    ]},
    entry_points={
        "console_scripts": [
            "yowasp-icepll = yowasp_nextpnr_ice40:_run_icepll_argv",
            "yowasp-icebram = yowasp_nextpnr_ice40:_run_icebram_argv",
            "yowasp-icemulti = yowasp_nextpnr_ice40:_run_icemulti_argv",
            "yowasp-icepack = yowasp_nextpnr_ice40:_run_icepack_argv",
            "yowasp-iceunpack = yowasp_nextpnr_ice40:_run_iceunpack_argv",
            "yowasp-nextpnr-ice40 = yowasp_nextpnr_ice40:_run_nextpnr_ice40_argv",
        ],
    },
)


setup(
    author="whitequark",
    author_email="whitequark@whitequark.org",
    description="nextpnr-ice40 FPGA place and route tool",
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
