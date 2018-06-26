# parse image
from urllib.request import urlopen
from html.parser import HTMLParser

# 클래스 처음쓰네? HTMLParser 상속받기~ (feed는 여기에 구현되어잇음)
# bs4 대신에 내부에 구현되어있는 HTML파서를 써보는 것임 ^^;
class ImageParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        # print(tag) # 구글의 html 태그들을 싸그리 읽어온다 ^^
        if tag != 'img':
            return
        if not hasattr(self, 'result') :# this안에 result라는 변수가 없으면 (not has attr), result라는 배열을 만들어라
            self.result = []
        for name, value in attrs:
            if name == 'src':
                print(value)

def parseImage(data):
    parser = ImageParser()
    parser.feed(data) # data를 줌...? >> result에 값이 담김
    dataset = set(x for x in parser.result) # parser.result들을 모두 트레이서해서 dataset에 set으로 담음
    print('\n'.join(sorted(dataset))) # 어디에 쓰는거지??

def main():
    url = 'http://www.google.co.kr'

    response = urlopen(url)
    charset = response.headers.get_content_charset()
    data = response.read().decode(charset)
    response.close()
    print('\n>>>>>>>>>>>>>>>>>> Fetch image from', url)
    parseImage(data)

if __name__ == '__main__':
    main()