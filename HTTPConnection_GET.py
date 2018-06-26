# http.client.HTTPConnection 을 사용한 GET 방식 요청

from http.client import HTTPConnection

conn = HTTPConnection('www.example.com')
conn.request('GET', '/') # '/~~'
# conn.request('GET', '/adsf3311test11') # 오류 발생!! 404 Not Found

result = conn.getresponse()
print( result.status, result.reason )

