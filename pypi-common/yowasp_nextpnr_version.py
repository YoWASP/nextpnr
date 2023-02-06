from setuptools_scm.git import parse as parse_git


def version():
    upstream_git = parse_git("../nextpnr-src")
    package_git  = parse_git("..")
    
    version = f"{upstream_git.tag.major}.{upstream_git.tag.minor}.{upstream_git.tag.micro}"
    if upstream_git.exact: # release
        version += f".0"
    else: # snapshot
        version += f".{upstream_git.distance}"
    version += f".post{package_git.distance}"
    if not upstream_git.exact: # snapshot
        version += f".dev"
    if upstream_git.dirty or package_git.dirty:
        version += f"+dirty"
    return version
