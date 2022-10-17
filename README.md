YoWASP nextpnr packages
=======================

The YoWASP nextpnr suite of packages provides [nextpnr][] and related tools for several FPGA families built for [WebAssembly][]. See the [overview of the YoWASP project][yowasp] for details.

The supported FPGA families are:
  * Lattice iCE40 (via [Project IceStorm][icestorm]);
  * Lattice ECP5 (via [Project Trellis][trellis]);
  * Lattice Nexus (via [Project Oxide][oxide]);
  * Gowin GW1N (via [Project Apicula][apicula]).

[nextpnr]: https://github.com/YosysHQ/nextpnr/
[webassembly]: https://webassembly.org/
[yowasp]: https://yowasp.github.io/
[icestorm]: https://github.com/YosysHQ/icestorm/
[trellis]: https://github.com/YosysHQ/prjtrellis/
[oxide]: https://github.com/gatecat/prjoxide
[apicula]: https://github.com/YosysHQ/apicula

Building
--------

The primary build environment for this repository is the `ubuntu-latest` GitHub CI runner; packages are built on every push and automatically published from the `release` branch to PyPI.

To reduce maintenance overhead, the only development environment we will support for this repository is x86_64 Linux.

License
-------

This package is covered by the [ISC license](LICENSE.txt), which is the same as the [nextpnr license](https://github.com/YosysHQ/nextpnr/blob/master/COPYING).
