from django.shortcuts import render
from bookbank.models import ReadingRecord

# Create your views here.
def user_page(request):
    username = request.GET.get('username')
    records = ReadingRecord.objects.all()
    result = []
    for record in records:
        if record.publisher.username == username:
            result.append(record)
    return render(request, 'my_page.html', {'result':result, 'username':username})