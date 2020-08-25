from curlpy import Curlpy


def test_url():
    r = Curlpy().url("https://example.com")


def test_get():
    r = Curlpy().url("https://example.com").get()


def test_fetch_body():
    # r = Curlpy().url("https://example.com").get().fetch().o("./hoge.txt")
    # print(r.body.decode("utf-8"))
    pass
