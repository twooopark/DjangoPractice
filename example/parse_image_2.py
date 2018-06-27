# parse image
# http.client.HTTPConnection 을 사용한 GET 방식 요청
from html.parser import HTMLParser
from http.client import HTTPConnection

class ImageParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        if tag != 'img':
            return
        if not hasattr(self, 'result') :
            self.result = []
        for name, value in attrs:
            if name == 'src':
                print(value)

def parseImage(data):
    parser = ImageParser()
    parser.feed(data)

def main():
    url = 'www.google.co.kr'
    conn = HTTPConnection(url)
    conn.request('GET', '/')
    result = conn.getresponse()
    print( result.status, result.reason )
    data = str(result.read())
    print('\n>>>>>>>>>>>>>>>>>> Fetch image from', url)
    parseImage(data)

if __name__ == '__main__':
    main()