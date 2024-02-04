# local-ip-bookkeeper

[![Build Status](https://github.com/psychonaute/local-ip-bookkeeper/workflows/test/badge.svg?branch=master&event=push)](https://github.com/psychonaute/local-ip-bookkeeper/actions?query=workflow%3Atest)
[![codecov](https://codecov.io/gh/psychonaute/local-ip-bookkeeper/branch/master/graph/badge.svg)](https://codecov.io/gh/psychonaute/local-ip-bookkeeper)
[![Python Version](https://img.shields.io/pypi/pyversions/local-ip-bookkeeper.svg)](https://pypi.org/project/local-ip-bookkeeper/)
[![wemake-python-styleguide](https://img.shields.io/badge/style-wemake-000000.svg)](https://github.com/wemake-services/wemake-python-styleguide)

Shares the current clipboard content by pushing it to the Gist. It make use of the [gist-storage](https://github.com/psychonaute/gist-storage) package

## Features

- Fully typed with annotations and checked with mypy, [PEP561 compatible](https://www.python.org/dev/peps/pep-0561/)

## Installation

```bash
poetry add git+https://git@github.com:psychonaute/share-android-clipboard.git
```

## Usage

`GITHUB_GIST_TOKEN` environement variable needs to be defined with your githun token CF: [gist-storage doc](https://github.com/psychonaute/gist-storage)

`your-gist-hash` and `your-file.json` from the gist you manually created, which can be secret (private). Also CF: [gist-storage doc](https://github.com/psychonaute/gist-storage)

```python
from local_ip_bookkeeper.tracker import IPTracker

share_clip_ = ShareClipboard(
    'your-gist-hash',
    'your-file.json',
)
share_clip_.share()
```

## License

[MIT](https://github.com/psychonaute/local-ip-bookkeeper/blob/master/LICENSE)

## Credits

This project was generated with [`wemake-python-package`](https://github.com/wemake-services/wemake-python-package). Current template version is: [de5779cdb74d1f42b95f55e9ce6b80ebc5fe7c01](https://github.com/wemake-services/wemake-python-package/tree/de5779cdb74d1f42b95f55e9ce6b80ebc5fe7c01). See what is [updated](https://github.com/wemake-services/wemake-python-package/compare/de5779cdb74d1f42b95f55e9ce6b80ebc5fe7c01...master) since then.
