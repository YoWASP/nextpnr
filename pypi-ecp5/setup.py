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


if "ALIAS" not in os.environ:
    setup_info = dict(
        name="yowasp-nextpnr-ecp5",
        version=version(),
        long_description=long_description(),
        long_description_content_type="text/markdown",
        install_requires=[
            "importlib_resources; python_version<'3.9'",
            "appdirs~=1.4",
            "wasmtime>=0.30,<2.0"
        ],
        packages=["yowasp_nextpnr_ecp5"],
        package_data={
            "yowasp_nextpnr_ecp5": [
                "*.wasm",
                "share/trellis/database/devices.json",
                "share/trellis/database/ECP5/tiledata/**/*",
                "share/trellis/database/ECP5/timing/**/*",
                "share/trellis/database/ECP5/LFE5*/*",
                "share/ecp5/chipdb-*.bin"
            ],
        },
        entry_points={
            "console_scripts": [
                "yowasp-ecppll = yowasp_nextpnr_ecp5:_run_ecppll_argv",
                "yowasp-ecpbram = yowasp_nextpnr_ecp5:_run_ecpbram_argv",
                "yowasp-ecpmulti = yowasp_nextpnr_ecp5:_run_ecpmulti_argv",
                "yowasp-ecppack = yowasp_nextpnr_ecp5:_run_ecppack_argv",
                "yowasp-ecpunpack = yowasp_nextpnr_ecp5:_run_ecpunpack_argv",
                "yowasp-nextpnr-ecp5 = yowasp_nextpnr_ecp5:_run_nextpnr_ecp5_argv",
            ],
        },
    )
else:
    setup_info = dict(
        name="yowasp-nextpnr-ecp5-{}".format(os.environ["ALIAS"]),
        version=version(),
        long_description="Transitional dummy package that depends on yowasp-nextpnr-ecp5.",
        long_description_content_type="text/markdown",
        install_requires=[
            "yowasp-nextpnr-ecp5=={}".format(version()),
        ]
    )


setup(
    author="whitequark",
    author_email="whitequark@whitequark.org",
    description="nextpnr-ecp5 FPGA place and route tool",
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
