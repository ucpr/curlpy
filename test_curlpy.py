from curlpy import Curlpy


def test_url():
    r = Curlpy().url("https://example.com")


def test_method():
    r = Curlpy("https://example.com").X("GET")
    assert "GET" == r._method

    r = Curlpy("https://example.com").X("POST")
    assert "POST" == r._method


def test_get():
    r = Curlpy().url("https://example.com").get()
    assert "GET" == r._method


def test_post():
    r = Curlpy().url("https://example.com").post()
    assert "POST" == r._method


def test_header():
    r = Curlpy().url("https://example.com").header({"Content-Type": "text"}).H({"X-test": "hoge"})
    assert r._headers["Content-Type"] == "text"
    assert r._headers["X-test"] == "hoge"


def test_fetch_body():
    # r = Curlpy().url("https://example.com").get().fetch().o("./hoge.txt")
    # print(r.body.decode("utf-8"))
    pass
