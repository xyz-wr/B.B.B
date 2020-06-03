from django.shortcuts import render
from bookbank.models import ReadingRecord
from django.core.paginator import Paginator
# Create your views here.
def user_page(request):
    username = request.GET.get('username')
    if username == None or username == "":
        username = request.user.username
    records = ReadingRecord.objects.all()

    result = []
    for record in records:
        if record.publisher.username == username:
            result.append(record)
    
    paginator = Paginator(result, 10)
    page = request.GET.get('page')

    if page == None or page == "":
        page = 1
    pages = paginator.get_page(page)
    left = 10 - len(pages)

    start = max(int(page)-5, 1)
    end = min(int(page)+5, paginator.num_pages)
    
    return render(request, 'my_page.html', {'result':result, 'username':username, 'pages':pages, 'left': range(left), 'range':[i for i in range(start, end+1)] })