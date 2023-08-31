YoWASP nextpnr packages
=======================

The YoWASP nextpnr suite of packages provides [nextpnr][] and related tools for several FPGA families built for [WebAssembly][]. See the [overview of the YoWASP project][yowasp] for details.

The supported FPGA families are:
  * Lattice iCE40 (via [Project IceStorm][icestorm]);
  * Lattice ECP5 (via [Project Trellis][trellis]);
  * Lattice MachXO2 (via [Project Trellis][trellis]; **experimental**);
  * Lattice Nexus (via [Project Oxide][oxide]; **experimental**);
  * Gowin GW1N (via [Project Apicula][apicula]; **experimental**).

[nextpnr]: https://github.com/YosysHQ/nextpnr/
[webassembly]: https://webassembly.org/
[yowasp]: https://yowasp.github.io/
[icestorm]: https://github.com/YosysHQ/icestorm/
[trellis]: https://github.com/YosysHQ/prjtrellis/
[oxide]: https://github.com/gatecat/prjoxide
[apicula]: https://github.com/YosysHQ/apicula


Notes
-----

For technical reasons, the `ecppack`, `ecpunpack`, `ecpbram`, `ecppll`, and `ecpmulti` tools from the MachXO2 toolchain shipped in the `yowasp-nextpnr-machxo2` PyPI package are installed under the names `yowasp-xo2pack`, `yowasp-xo2unpack`, `yowasp-xo2bram`, `yowasp-xo2pll`, and `yowasp-xo2multi` respectively. These commands run bit-for-bit identical code as their `yowasp-ecp*` prefixed brethren from the `yowasp-nextpnr-ecp5` PyPI package of the same version.


Versioning
----------

The version of this package is derived from the upstream nextpnr package version in the ``X.Y[.Z]`` format, and is comprised of five or six parts in a ``X.Y.Z.N.postM[.dev]`` format:

1. ``X``: nextpnr major version
2. ``Y``: nextpnr minor version
3. ``Z``: nextpnr patch version; reserved as nextpnr currently does not do patch releases
4. ``N``: zero for packages built from nextpnr releases, ``N`` for packages built from unreleased nextpnr snapshots; ``N`` is the amount of commits since the latest release
5. ``postM``: package build version; disambiguates different builds produced from the same nextpnr source tree
6. ``dev``: present only for packages built from unreleased nextpnr snapshots; marks these packages as pre-releases

With this scheme, there is a direct correspondence between upstream versions and [PEP 440][pep440] Python package versions. Packages built from unreleased snapshots are ignored by pip by default, but can be still installed explicitly. (These packages are uploaded daily to [TestPyPI][], but only occasionally to [PyPI][].)

A different versioning scheme was used earlier, where the package build version was denoted by a ``.devM`` suffix. This scheme did not work well with [PEP 440 version specifiers][pep440-vs] and was retired.

[testpypi]: https://test.pypi.org/
[pypi]: https://pypi.org/
[pep440]: https://peps.python.org/pep-0440/
[pep440-vs]: https://peps.python.org/pep-0440/#version-specifiers


Configuration
-------------

See the documentation for [yowasp-runtime](https://github.com/YoWASP/runtime#configuration).


License
-------

This package is covered by the [ISC license](LICENSE.txt), which is the same as the [nextpnr license](https://github.com/YosysHQ/nextpnr/blob/master/COPYING).
