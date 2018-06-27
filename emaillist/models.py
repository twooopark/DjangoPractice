from django.db import models

# Create your models here.


# 테이블 정의 (emaillist/modes.py)
# ORM를 사용하여 테이블과 클래스를 매핑
# Emaillist 테이블 컬럼과 클래스 변수 간의 매핑
# https://docs.djangoproject.com/en/2.0/topics/db/models/
class Emaillist(models.Model) :
    # field 설정
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=200)

    def __str__(self):
        return "Emaillist(%s, %s, %s)" % (self.first_name, self.last_name, self.email)

