****
1. django, emaillist 설정 및 셋팅

#### 1.1 django 설치
  ```  pip install django ```

#### 1.2 django project 생성 (Python_web)
  ``` (venv) D:\pythonPycharm\web>django-admin startproject Python_web ```

#### 1.3 app 생성 (emaillist)
  ``` (venv) D:\pythonPycharm\web\Python_web>python manage.py startapp emaillist ```

#### 1.4 경로 변경 (처음에 이미 생성한 pycharm 프로젝트안에 django 프로젝트를 생성해서...)
```
다음엔 django 프로젝트만 생성...? venv(지역라이브러리(?))를 사용중이라 어려울 듯.
django를 전역라이브러리로 사용하고 있다면, 경로 변경해줄 필요 없을듯
```
#### 1.5 기본 시간과 사용할 데이터베이스 설정 (setting.py)
  ```
TIME_ZONE = 'Asia/Seoul'
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',##
        # 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'NAME' : 'django_db',
        'USER' : 'django_user',
        'PASSWORD' : 'manager',
        'HOST' : '127.0.0.1',
        'PORT' : '3306'
    }
}
```

#### 1.6 mysql을 사용하려면 mysqlclient를 설치해야한다. ( 아래는 안했을 때, 오류메세지 )
```
django.core.exceptions.ImproperlyConfigured: Error loading MySQLdb module.
Did you install mysqlclient?
```
#### 1.7 설치
```
pip install mysqlclient
```

#### 1.8 데이터베이스와 관련된 변경 사항은 장고에 반드시 반영해 주어야 한다
```
(venv) D:\pythonPycharm\web>python manage.py migrate
```

#### 1.9 서버 실행
```
(venv) D:\pythonPycharm\web>python manage.py runserver 0.0.0.0:8000
```

#### 1.10 TEST
```
http://127.0.0.1:8000/
 http://127.0.0.1:8000/admin
 접속 가능
```

#### 1.11 계정 생성
```
(venv) D:\pythonPycharm\web>python manage.py createsuperuser
Username (leave blank to use 'bit-user'): admin
Email address: twooo.park@gmail.com
Password:
Password (again):
Superuser created successfully.
```

#### 1.12 설치한 앱 등록
```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'emaillist'##
]
```

#### 1.13 모델을 등록시켜야 제대로 makemigrations 된다. (emaillist/admin.py)
```
from emaillist.models import Emaillist
admin.site.register(Emaillist)
```

#### 1.14 models.py에서 적용한 변경사항이나 추가된 혹은 삭제된 사항들을 감지하여 파일로 생성 (0001_initial.py)
```
(venv) D:\pythonPycharm\web>python manage.py makemigrations
Migrations for 'emaillist':
  emaillist\migrations\0001_initial.py
    - Create model Emaillist
```

#### 1.15 적용되지 않은 migrations들을(설정값들을) 적용시킨다.
```
(venv) D:\pythonPycharm\web>python manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, emaillist, sessions
Running migrations:
  Applying emaillist.0001_initial... OK
```

#### 1.16 http://127.0.0.1:8000/admin/emaillist/emaillist/ 에서 확인
```
urls.py, views.py --> mapping
```


****
2. GUESTBOOK 설정 및 세팅

#### 2.1 templates 경로 수정

#### 2.2 guestbook app 추가
```
(venv) D:\pythonPycharm\web>python manage.py startapp guestbook
```

#### 2.3 Guestbook 클래스 추가 (models.py)

#### 2.4 모델 등록 (admin.py)

#### 2.5 makemigrations : models.py에서 적용한 변경사항이나 추가된 혹은 삭제된 사항들을 감지하여 파일로 생성
```
(venv) D:\pythonPycharm\web>python manage.py makemigrations
```

#### 2.6 migrate : 적용되지 않은 migrations들을(설정값들을) 적용시키는 역할
```
(venv) D:\pythonPycharm\web>python manage.py migrate
```

#### 2.7 mapping (urls.py, views.py, templates/....html)

#### 2.8 서버 실행
```
(venv) D:\pythonPycharm\web>python manage.py runserver 0.0.0.0:8000
```

#### 2.9 뷰와 탬플릿 연결,

#### 2.10 sub를 사용하기 위해, 탬플릿 필터(django-mathfilters) 설치 및 추가 (index.html, setting.py)
```
{{ guestbook_list.count|add:1|sub:forloop.counter }}
```

#### 2.11 탬플릿 필터 import (index.html)
```
{% load mathfilters %}
```

----------------------------------
3. MTV 패턴 (django)

#### 3.1 Model – 데이터베이스 CRUD
  - 사용될 데이터의 정의를 담고 있는 장고의 클래스
  - ORM를 사용하여 테이블과 클래스를 매핑
  - 보통 models.py 파일에 정의한다.
  - 장고는 테이블 및 컬럼을 자동으로 생성하기 위해 많은 규칙을 가지고 있다.
https://docs.djangoproject.com/en/2.0/topics/db/models/
  - CRUD를 위한 여러 기능을 지원한다.

#### 3.2 Template – 화면 UI 설계
  - 자체 템플릿 시스템을 가지고 있다.
  - 디자이너와 개발간에 업무가 완전 분리
  - 템플릿에서도 파이썬 코드를 직접 사용할 수 있다. (템플릿 자체 문법에 맞게 작성)
  - 템플릿 파일은 *.html 확장자를  가지며  적절한  디렉토리에  위치해  있어야  한다.
     	장고는 템플릿 파일을 찾을 때,  settings.py에 지정되어 있는 TEMPATE_DIRS 및 INSTALLED_APP 의 디렉토리를 검색한다.

#### 3.3 View – 로직 설계
  - 웹 요청을 받아  데이터베이스 CRUD등 비지니스 로직을 수행한다.
  - 그리고 그 결과 데이터를 HTML로 변환하기 위해 템플릿 처리를 한다.
  - 렌더링 된 HTML을 웹 클라이언트, 브라우저로 응답하게 된다.
  - 장고에서는 뷰는 함수 또는 클래스 메소드로 작성된다.
  - 응답은 HTML, 404 에러, 리다이렉트 등 다양한 응답이 가능하다.
  - 보통, views.py에 작성되지 만 다른 파일에 작성하는 것도 가능하다.

<img src="https://github.com/twooopark/DjangoPractice/blob/master/dataflow.JPG" width="700px" height="600px" />
