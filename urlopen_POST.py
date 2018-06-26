# POST 방식으로 웹 서버에 요청 보내기
from urllib.request import urlopen, Request
from urllib.parse import urlencode, urlparse

url = 'http://www.python.org:80/?'
data = urlencode({'a':10, 'b':20, 'name':'둘리'})

# 참고 > a=10&b=20&name=%EB%91%98%EB%A6%AC

# 만약 str으로 넣으면 data.encode('utf-8')을 해줘야 한다.
# data = 'a=10&b=20&name=둘리'
# data=data.encode('utf-8')

request = Request(url, data.encode('utf-8'))
# request 객체를 사용한 요청 헤더 변경
request.add_header('Content-Type', 'text/html')



f = urlopen(request)
print(f.read())