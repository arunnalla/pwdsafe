<div align="center">
  <h2>pwdsafe</h2>
</div>

Python package to check if a given password is safe to use.

pwdsafe is a thin wrapper around [have i been pwned](https://haveibeenpwned.com/) that checks if a given password is compromised.

### Install

```sh
pip install pwdsafe
```

### Usage

```python
from pwdsafe import is_safe

is_pwd_safe = is_safe("password")
```
