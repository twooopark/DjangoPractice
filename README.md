설치 세팅 >> Command

MTV 패턴 (django)

1) Model – 데이터베이스 CRUD
  - 사용될 데이터의 정의를 담고 있는 장고의 클래스
  - ORM를 사용하여 테이블과 클래스를 매핑
  - 보통 models.py 파일에 정의한다.
  - 장고는 테이블 및 컬럼을 자동으로 생성하기 위해 많은 규칙을 가지고 있다.
https://docs.djangoproject.com/en/2.0/topics/db/models/
  - CRUD를 위한 여러 기능을 지원한다.

2) Template – 화면 UI 설계
  - 자체 템플릿 시스템을 가지고 있다.
  - 디자이너와 개발간에 업무가 완전 분리
  - 템플릿에서도 파이썬 코드를 직접 사용할 수 있다. (템플릿 자체 문법에 맞게 작성)
  - 템플릿 파일은 *.html 확장자를  가지며  적절한  디렉토리에  위치해  있어야  한다.
     	장고는 템플릿 파일을 찾을 때,  settings.py에 지정되어 있는 TEMPATE_DIRS 및 INSTALLED_APP 의 디렉토리를 검색한다.

3) View – 로직 설계
  - 웹 요청을 받아  데이터베이스 CRUD등 비지니스 로직을 수행한다.
  - 그리고 그 결과 데이터를 HTML로 변환하기 위해 템플릿 처리를 한다.
  - 렌더링 된 HTML을 웹 클라이언트, 브라우저로 응답하게 된다.
  - 장고에서는 뷰는 함수 또는 클래스 메소드로 작성된다.
  - 응답은 HTML, 404 에러, 리다이렉트 등 다양한 응답이 가능하다.
  - 보통, views.py에 작성되지 만 다른 파일에 작성하는 것도 가능하다.


<img src="https://github.com/twooopark/DjangoPractice/blob/master/dataflow.JPG" width="700px" height="600px" />
