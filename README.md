# PyppeSnap

[![Test](https://github.com/NatLee/PyppeSnap/actions/workflows/test.yml/badge.svg)](https://github.com/NatLee/PyppeSnap/actions/workflows/test.yml)[![Release](https://github.com/NatLee/PyppeSnap/actions/workflows/release.yml/badge.svg)](https://github.com/NatLee/PyppeSnap/actions/workflows/release.yml)

![screenshot](https://i.imgur.com/hgXl2l6.png)

This is a tool for getting snapshot with base64 encoding from a website.

As the first DEMO image you see, just need one URL input to function.

## Installation

```bash
pip install pyppesnap
```

## Usage

Common use with code below.

```python
from pyppesnap import get_snapshot_by_url

if __name__ == '__main__':
    url = 'https://www.google.com'
    print(get_snapshot_by_url(url))

```

> You need to give a valid URL like start with `http`, or Pyppeteer cannot navigate it.

It can be used with web framworks to get a snapshot, check it in `./example`.
