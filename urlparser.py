# urlparser

from urllib.parse import urlparse

url = 'http://www.python.org:80/guido/python.html:philosophy?a=10&b=20#here'

result = urlparse(url)
# 참고 > ParseResult(scheme='http', netloc='www.python.org:80', path='/guido/python.html:philosophy', params='', query='a=10&b=20', fragment='here')
print(result)