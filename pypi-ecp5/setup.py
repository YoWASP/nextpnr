import os
from setuptools import setup, find_packages
from setuptools_scm.git import parse as parse_git


def version():
    upstream_git = parse_git("../nextpnr-src")
    if upstream_git.exact:
        yosys_version = upstream_git.format_with("{tag}")
    else:
        yosys_version = upstream_git.format_with("{tag}.post{distance}")

    package_git = parse_git("..")
    package_version = package_git.format_with(".dev{distance}")

    return yosys_version + package_version


def long_description():
    with open("../README.md") as f:
        return f.read()


if "DEVICE" not in os.environ:
    setup_info = dict(
        name="yowasp-nextpnr-ecp5",
        version=version(),
        install_requires=[
            "importlib_resources; python_version<'3.9'",
            "wasmtime~=0.18.2"
        ],
        packages=["yowasp_nextpnr_ecp5"],
        package_data={
            "yowasp_nextpnr_ecp5": [
                "*.wasm",
                "share/trellis/database/devices.json",
                "share/trellis/database/ECP5/tiledata/**/*",
                "share/trellis/database/ECP5/timing/**/*",
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
elif "," in os.environ["DEVICE"]:
    devices = os.environ["DEVICE"].split(",")
    setup_info = dict(
        name="yowasp-nextpnr-ecp5-all",
        version=version(),
        install_requires=[
            "yowasp-nextpnr-ecp5-{}=={}".format(device, version())
            for device in devices
        ]
    )
else:
    device = os.environ["DEVICE"]
    if device == "25k":
        trellis_data = [
            "share/trellis/database/ECP5/*-12F/*",
            "share/trellis/database/ECP5/*-25F/*",
        ]
    if device == "45k":
        trellis_data = ["share/trellis/database/ECP5/*-45F/*"]
    if device == "85k":
        trellis_data = ["share/trellis/database/ECP5/*-85F/*"]
    setup_info = dict(
        name="yowasp-nextpnr-ecp5-{}".format(device),
        version=version(),
        install_requires=["yowasp-nextpnr-ecp5=={}".format(version())],
        packages=["yowasp_nextpnr_ecp5"],
        package_data={
            "yowasp_nextpnr_ecp5": [
                "share/ecp5/chipdb-{}.bin".format(device),
                *trellis_data
            ],
        },
    )


setup(
    author="whitequark",
    author_email="whitequark@whitequark.org",
    description="nextpnr-ecp5 FPGA place and route tool",
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
