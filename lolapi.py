import urllib.parse
import requests

class API(object):
    BASE = 'https://hogehogefugafuga.com'
    # Does this look like a token?
    TOKEN = '9da00f1f4b96fbe1d640afdb6c75c4157d6c613c'


    def __init__(self):
        self._s = requests.Session()
        self._s.headers.update({'token': self.TOKEN})

    def post(self, data):
        url = urllib.parse.urlparse(self.BASE, 'post')
        data = {'data': 'ithinkiwanttopostthisdatalol'}
        self._s.post(url, data=data)
