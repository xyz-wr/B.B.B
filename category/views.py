from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from bookbank.models import ReadingRecord
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages

# Create your views here.

def category_records(request):
    original_records = ReadingRecord.objects.all()[::-1]
    category = request.GET.get('category') or ""

    records = []
    for i in original_records:
        if i.category == category:
            records.append(i)
    
    paginator = Paginator(records, 10)
    page= request.GET.get('page')
    if page == "" or page == None:
        page = 1
    records_page = paginator.get_page(page)
    start = max(int(page)-5, 1)
    end = min(int(page)+5, paginator.num_pages)
    
    return render(request, 'category_records.html', {'records':records, 'records_page' : records_page, 'range' : [i for i in range(start, end+1)], 'category': category})