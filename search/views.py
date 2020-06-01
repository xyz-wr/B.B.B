from django.shortcuts import render

from django.views.generic.edit import FormView
from search.forms import PostSearchForm
from django.db.models import Q

from bookbank.models import ReadingRecord
from django.core.paginator import Paginator
import pdb # pdb.set_trace() 사용해서 확인하기!

def search(request):
    q = request.GET.get('q') or ""
    
    post_list = ReadingRecord.objects.filter(
            Q(title__icontains=q)
             #| Q(record_body__icontains=q) | Q(author__icontains=q) 
             #| Q(publisher__icontains=q) | Q(record_title__icontains=q)
        ).distinct() # 중복사항 제거
        # 일단은 title만 검색 가능하도록 주석처리. 이후, 콤보 박스를 통해 선택할 수 있도록 구현?
    paginator = Paginator(post_list, 2)
    page = request.GET.get('page')
    post_counts = paginator.get_page(page)

    if q == "":         # q가 작성되지 않았을 경우, post_list 비우기
        post_list = []

    return render(request, 'searchPage.html', {"q": q, "object_list":post_list, "post_counts":post_counts})