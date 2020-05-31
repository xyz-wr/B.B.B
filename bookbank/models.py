from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class ReadingRecord(models.Model):
    category_list = (
        ("krBook","국내 도서"),
        ("otherBook","국외 도서"),
        ("eBook","eBook"),
    )

    title = models.CharField(max_length = 200)          # 책 제목
    author = models.CharField(max_length= 100)          # 책 저자
    
    publisher = models.ForeignKey(User, on_delete=models.CASCADE)
    # publisher = models.CharField(max_length = 100)      # 독서 기록 작성자(FK로 변경 필요)
    record_title = models.CharField(max_length = 200)   # 독서 기록 제목
    read_at = models.DateTimeField()                    # 독서 기록 일자(사용자가 정한 날짜) 
    category = models.CharField(max_length = 100, choices = category_list) # 책 카테고리
    record_body = models.TextField()                    # 독서 기록 내용

    created_at = models.DateTimeField()                 # 독서 기록 최초 일자
    updated_at = models.DateTimeField()                 # 독서 기록 갱신 일자

    # rep_img = models.ImageField(upload_to=date_upload_to, blank = True, default = None)
    
    def __str__(self):
        return self.record_title


    def summary(self):
        return self.record_body[:400]