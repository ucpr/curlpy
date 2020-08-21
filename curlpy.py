from io import BytesIO
import pycurl
from pycurl import Curl


class Curlpy:
    curl: Curl

    def __init__(self, url=""):
        self.curl: Curl = Curl()
        self.buffer: BytesIO = BytesIO()

        self.body: bytes = ""

        self.curl.setopt(pycurl.WRITEDATA, self.buffer)

    def url(self, url: str):
        self.curl.setopt(pycurl.URL, url)
        return self

    def X(self, method: str):
        self.curl.setopt(pycurl.CUSTOMREQUEST, method)
        return self

    def get(self):
        return self.X("GET")

    def fetch(self):
        self.curl.perform()
        self.curl.close()
        self.body = self.buffer.getvalue()
        return self
