# 웹서버 라이브러리 사용해보기...
# 참고) 파이썬 웹 서버 라이브러리를 사용해 작성하긴 보다는 웹 프레임워크를 사용하여 개발하는 경우가 많다
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs
import numpy as np
import matplotlib.pyplot as plt
from io import BytesIO

# http://localhost:9999/graph?a=10&b=20 을 요청하도록 구현해보자~
# 예상 출력 결과 (req_url): graph
PORT = 9999
class MyHTTPRequestHandler(BaseHTTPRequestHandler): # BaseHTTPRequestHandler에게 상속받음.
    def do_GET(self):
        # path slicing해서 graph 만 받아보자,
        # qindex = self.path.index('?')
        qindex = self.path.find('?')
        print("qindex:", qindex)
        req_url =  self.path[:len(self.path)] if qindex == -1 else self.path[:qindex]
        # if qindex == -1 :
        #     req_url = self.path[:len(self.path)]
        # else :
        #     req_url = self.path[:qindex+1]

        # http://localhost:9999/board 처럼 graph가 아닌 경로로 접근하는 경우 404 에러 출력
        print("req_url: ", req_url)
        if req_url != '/graph':
            self.send_error(404, 'Not Found')
            return

        # 내부에서 a에 해당하는 함수 찾는(?) 구문
        # print(MyHTTPRequestHandler.__dict__['ex'])


        # qs로 받은 ex의 값을 처리해보자
        # 1. http://192.168.56.1:9999/graph?ex=1 인 경우에 ex1()을 실행하면서, '안녕하세요'를 출력한다.
        # 2. http://192.168.56.1:9999/graph?ex=2 인 경우에, 그래프 이미지를 출력한다.
        handler_name = 'ex' + self.get_parameter('ex')
        if handler_name not in MyHTTPRequestHandler.__dict__:
            self.send_error(404, 'FileNot Found')
            return

        MyHTTPRequestHandler.__dict__[handler_name](self)


    def get_parameter(self, name):
        qindex = self.path.find('?')

        # queryString 가져오기
        # 예상 출력 결과 (qs): a=10&b=20
        qs = '' if qindex == -1 else self.path[qindex+1:]
        # if qs == -1:
        #     qs = ''
        # else :
        #     qs = self.path[qindex+1:]

        params = parse_qs(qs)
        values = params.get(name)

        return None if values is None else values.pop()

    def ex1(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write("<h1>안녕하세요</h1>".encode('utf-8'))

    def ex2(self):
        arr = np.random.normal(5, 3, 500)

        fig, subplots = plt.subplots(2, 1)
        subplots[0].plot(arr, color='red', linestyle='solid')
        subplots[1].hist(arr, bins=20, edgecolor='black', linewidth=1.2)

        buffer = BytesIO()
        plt.savefig(buffer, dpi=80, bbox_inches='tight')
        plt.clf()

        self.send_response(200)
        self.send_header('Content-Type', 'image/png')
        self.end_headers()
        self.wfile.write(buffer.getvalue())


# 서버 구동
httpd = HTTPServer(('', PORT), MyHTTPRequestHandler)
print('Server running on port', PORT)
httpd.serve_forever()
