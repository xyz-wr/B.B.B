from django.db import models
from django.contrib.auth.models import User
import os
from uuid import uuid4
from django.utils import timezone

def date_upload_to(instance, filename):
    ymd_path = timezone.now().strftime('%Y/%m/%d')
    uuid_name = uuid4().hex
    extension = os.path.splitext(filename)[-1].lower()
    return '/'.join([ymd_path, uuid_name + extension])

# Create your models here.
class ReadingRecord(models.Model):
    category_list = (
        ("국내 도서", 
            (
                ("국내 가정 살림", "가정 살림"),
                ("국내 건강 취미","건강 취미"), 
                ("국내 경제 경영", "경제 경영"),
                ("국내 국어 외국어 사전", "국어 외국어 사전"),
                ("국내 대학교재", "대학교재"),
                ("국내 만화/라이트노벨", "만화/라이트노벨"),
                ("국내 사회 정치", "사회 정치"),
                ("국내 소설/시/희곡", "소설/시/희곡"),
                ("국내 수험서 자격증", "수험서 자격증"),
                ("국내 어린이", "어린이"),
                ("국내 에세이", "에세이"),
                ("국내 여행", "여행"),
                ("국내 역사","역사"),
                ("국내 예술", "예술"),
                ("국내 유아", "유아"),
                ("국내 인문", "인문"),
                ("국내 인물", "인물"),
                ("국내 자기계발", "자기계발"),
                ("국내 자연과학", "자연과학"),
                ("국내 잡지", "잡지"),
                ("국내 전집", "전집"),
                ("국내 종교", "종교"),
                ("국내 청소년", "청소년"),
                ("국내 IT 모바일", "IT 모바일"),
                ("국내 초등참고서", "초등참고서"),
                ("국내 중고등참고서", "중고등참고서"),
            )
        ),
        ("외국 도서",
            (
                ("외국 ELT 사전", "ELT 사전"),
                ("외국 문학 소설", "문학 소설"),
                ("외국 경제 경영", "경제 경영"),
                ("외국 인문 사회", "인문 사회"),
                ("외국 예술 대중문화", "예술 대중문화"),
                ("외국 취미 라이프스타일", "취미 라이프스타일"),
                ("외국 컴퓨터", "컴퓨터"),
                ("외국 자연과학", "자연과학"),
                ("외국 대학교재 전문서", "대학교재 전문서"),
                ("외국 해외잡지", "해외잡지"),
                ("외국 유아 어린이 청소년", "유아 어린이 청소년"),
                ("외국 캐릭터북", "캐릭터북"),
                ("외국 초등코스북", "초등코스북"),
                ("외국 학습서", "학습서"),
                ("외국 일본도서","일본도서"),
                ("외국 중국도서","중국도서"),
                ("외국 프랑스도서","프랑스도서"),
            )
        )
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

    rep_img = models.ImageField(upload_to=date_upload_to, blank = True, default = None)
    
    def __str__(self):
        return self.record_title


    def summary(self):
        return self.record_body[:400]