# Sync Android Clipboard

[![Build Status](https://github.com/codekoriko/local-ip-bookkeeper/workflows/test/badge.svg?branch=master&event=push)](https://github.com/codekoriko/local-ip-bookkeeper/actions?query=workflow%3Atest)
[![codecov](https://codecov.io/gh/codekoriko/local-ip-bookkeeper/branch/master/graph/badge.svg)](https://codecov.io/gh/codekoriko/local-ip-bookkeeper)
[![Python Version](https://img.shields.io/pypi/pyversions/local-ip-bookkeeper.svg)](https://pypi.org/project/local-ip-bookkeeper/)
[![wemake-python-styleguide](https://img.shields.io/badge/style-wemake-000000.svg)](https://github.com/wemake-services/wemake-python-styleguide)

Sync the clipboard content between device. It uses encryption a Gist files thanks to the [gist-storage](https://github.com/codekoriko/gist-storage) package

## Features

- Bidirectional sync of device and remote clipboard
- Don't require to be on the same network
- Clipboard content is saved to gist encrypted
- Fully typed with annotations and checked with mypy, [PEP561 compatible](https://www.python.org/dev/peps/pep-0561/)

## Installation

```bash
poetry add git+https://github.com/codeCoRepo/sync-android-clipboard#master
```

## Usage

`GITHUB_GIST_TOKEN` environement variable needs to be defined with your githun token CF: [gist-storage doc](https://github.com/codekoriko/gist-storage)

create a gist and copy `your-gist-hash`. Inside that gist create 2 files `my-local-clipboard` and `my-remote-clipboard`. Gist can be set to `secret` (private). Also CF: [gist-storage doc](https://github.com/codekoriko/gist-storage)

```python
from dotenv import load_dotenv, find_dotenv
from sync_android_clipboard.sync import SyncClipboard


load_dotenv(find_dotenv())

sync_clip= SyncClipboard(
    'your-gist-hash',
    'my-phone-clipboard-encrypted-file',
)
sync_clip.push()
sync_clip.fetch()
```

## License

[MIT](https://github.com/codekoriko/local-ip-bookkeeper/blob/master/LICENSE)

## Credits

This project was generated with [`wemake-python-package`](https://github.com/wemake-services/wemake-python-package). Current template version is: [de5779cdb74d1f42b95f55e9ce6b80ebc5fe7c01](https://github.com/wemake-services/wemake-python-package/tree/de5779cdb74d1f42b95f55e9ce6b80ebc5fe7c01). See what is [updated](https://github.com/wemake-services/wemake-python-package/compare/de5779cdb74d1f42b95f55e9ce6b80ebc5fe7c01...master) since then.
