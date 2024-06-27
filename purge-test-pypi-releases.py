# If TestPyPI complains about size of packages reaching the quota, use Developer Tools to find out
# the session ID (in `Cookie:` header) and CSRF token (in any form submission), and use this script
# to trim old files. THIS OPERATION CANNOT BE UNDONE.

session_id = "<insert-session-id-here>"
csrf_token = "<insert-csrf-token-here>"

projects = []
versions = []

import urllib.parse
import urllib.request

for version in versions:
    for project in projects:
        request = urllib.request.Request(
            f"https://test.pypi.org/manage/project/{project}/release/{version}/",
            method="POST",
            headers={
                "Cookie": f"session_id={session_id}",
                "Origin": "https://test.pypi.org",
            },
            data=urllib.parse.urlencode({
                "csrf_token": csrf_token,
                "confirm_delete_version": version,
            }).encode()
        )
        urllib.request.urlopen(request)
        print(f"deleted {project} {version}")
