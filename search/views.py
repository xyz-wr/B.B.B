from django.shortcuts import render, redirect

from django.views.generic.edit import FormView
from search.forms import PostSearchForm
from django.db.models import Q

from bookbank.models import ReadingRecord
import pdb # pdb.set_trace() 사용해서 확인하기!

def search(request):
    q = request.GET.get('q') or ""
    
    post_list = ReadingRecord.objects.filter(
            Q(title__icontains=q) | Q(record_body__icontains=q) | Q(author__icontains=q)
             | Q(publisher__icontains=q) | Q(record_title__icontains=q)
        ).distinct()

    if q == "":
        post_list = []

    return render(request, 'searchPage.html', {"q": q, "object_list":post_list})