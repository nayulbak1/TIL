from django.db import models

# Create your models here.
class Article(models.Model): # models.Model의 상속을 받음
    # id는 기본적으로 처음 테이블 생성 시 자동으로 만들어짐
    # id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)