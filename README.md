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
```python
import curlpy

req = curlpy("https://exapmple.com").X("GET")
# or req = curlpy("https://example.com").get()

req = curlpy("https://exapmple.com").X("POST")
# or req = curlpy("https://example.com").post()
```

## Contributions
Welcome your contribution!

It's tough to cover all the options. Send me a pull request if you don't see the options you need!  
Also, if you find a bug, send me an Issue or pull request!

## Author
taichi uchihara (contact@ucpr.dev)

## License
MIT
