# PyppeSnap

[![Test](https://github.com/NatLee/PyppeSnap/actions/workflows/test.yml/badge.svg)](https://github.com/NatLee/PyppeSnap/actions/workflows/test.yml)[![Release](https://github.com/NatLee/PyppeSnap/actions/workflows/release.yml/badge.svg)](https://github.com/NatLee/PyppeSnap/actions/workflows/release.yml)

![image](https://i.imgur.com/hgXl2l6.png)

![pdf](https://i.imgur.com/JLe9bYi.png)

This is a tool for getting snapshot with base64 encoding from a website.

As DEMO image you see, just need one URL input to function.

This package support `image` and `pdf` with encoded base64.

## Installation

```bash
pip install pyppesnap
```

Check it on [Pypi](https://pypi.org/project/PyppeSnap/).

## Usage

Common use with code below.

- Get image

```python
from pyppesnap import get_image_snapshot_by_url
url = 'https://www.google.com'
print(get_image_snapshot_by_url(url))
```

- Get PDF

```python
from pyppesnap import get_pdf_snapshot_by_url
url = 'https://www.google.com'
print(get_pdf_snapshot_by_url(url))
```

> You need to give a valid URL like start with `http`, or Pyppeteer cannot navigate it.

It can be used with web framworks to get a snapshot, check details in [./example](https://github.com/NatLee/PyppeSnap/tree/main/example).
