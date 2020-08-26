# curlpy
[![Actions Status](https://github.com/ucpr/curlpy/workflows/CI/badge.svg?branch=master)](https://github.com/ucpr/curlpy/actions)

## Description
curlpy can send an HTTP request like you would handle curl on the command line.  
The curl options are the same as the method names, so if you know how to use curl, you can use it in the same way.

## Motivation
I was finding it cumbersome to figure out how to use http library when writing small scripts.
So I thought that I want something that can be programmed to handle curl from the command line.

## Install
```
# pip install curlpy
```

## Examples

### Simple HTTP request

sending a GET request.

```bash
$ curl https://example.com
```

```python
from curlpy import Curlpy

req = curlpy("https://exapmple.com").fetch()

print(req.body)
```

sending a POST request.

```bash
$ curl -X POST https://example.com
```

```python
from curlpy import Curlpy

req = curlpy("https://example.com").X("POST").fetch()
```

### File Download

For example, use `/images/png` in httpbin.

```bash
$ curl -X GET "http://httpbin.org/image/png" -H  "accept: image/png" -o "hoge.png"
```

If you want to save the binary data, you need to pass the `binary` option to `True`.

```python
from curlpy import Curlpy

req = curlpy("https://httpbin.org/image/png").H({"accept": "image/png"}).fetch().o("hoge.png", binary=True)
```


## Contributions

Welcome your contribution!

It's tough to cover all the options. Send me a pull request if you don't see the options you need!  
Also, if you find a bug, send me an Issue or pull request!

## Author

taichi uchihara (contact@ucpr.dev)

## License
MIT
