from curlpy import Curlpy


req = (
    Curlpy("https://httpbin.org/image/png")
    .H({"accept": "image/png"})
    .fetch()
    .o("hoge.png", binary=True)
)
