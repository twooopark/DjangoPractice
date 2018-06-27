# 웹서버 라이브러리 사용해보기...
# 참고) 파이썬 웹 서버 라이브러리를 사용해 작성하긴 보다는 웹 프레임워크를 사용하여 개발하는 경우가 많다
from http.server import BaseHTTPRequestHandler, HTTPServer

PORT = 9999
class MyHTTPRequestHandler(BaseHTTPRequestHandler): # BaseHTTPRequestHandler에게 상속받음.
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write("<h1>안녕하세요</h1>".encode('utf-8'))

# 서버 구동
httpd = HTTPServer(('', PORT), MyHTTPRequestHandler)
print('Server running on port', PORT)
httpd.serve_forever()
