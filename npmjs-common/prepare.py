import os
import re
import sys
import json
import subprocess


arch = sys.argv[1]


nextpnr_version_raw = subprocess.check_output([
    "git", "-C", "../nextpnr-src", "describe", "--tags", "HEAD"
], encoding="utf-8").strip()

git_rev_list_raw = subprocess.check_output([
    "git", "rev-list", "HEAD"
], encoding="utf-8").split()

nextpnr_version = re.match(r"^nextpnr-(\d+).(\d+)(?:-(\d+)-)?", nextpnr_version_raw)
nextpnr_major   = int(nextpnr_version[1])
nextpnr_minor   = int(nextpnr_version[2])
nextpnr_node    = int(nextpnr_version[3] or "0")

distance = len(git_rev_list_raw) - 1

if os.environ.get("RELEASE_BRANCH", "false") in ("true", "1", "yes"):
    version = f"{nextpnr_major}.{nextpnr_minor}.{distance}"
else:
    version = f"{nextpnr_major}.{nextpnr_minor + 1}.{nextpnr_node}-dev.{distance}"
print(f"version {version}")


with open("package-local.json", "rt") as f:
    package_local = json.load(f)
with open("package-in.json", "rt") as f:
    package_json = json.load(f)
package_json["version"] = version
package_json["name"] = package_json["name"].replace("__ARCH__", arch)
package_json["description"] = package_json["description"].replace("__ARCH__", arch)
package_json["scripts"]["pack"] = package_json["scripts"]["pack"].replace("__ARCH__", arch)
transpile_commands = []
for transpile_file in package_local["scripts"]["transpile"]:
    transpile_commands.append(package_json["scripts"]["transpile"]
        .replace("__FILENAME__", transpile_file)
        .replace("__BASENAME__", os.path.basename(transpile_file)))
package_json["scripts"]["transpile"] = " && ".join(transpile_commands)
with open("package.json", "wt") as f:
    json.dump(package_json, f, indent=2)
