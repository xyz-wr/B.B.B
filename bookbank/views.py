from django.shortcuts import render, redirect, get_object_or_404
from .models import ReadingRecord
from django.utils import timezone
from .form import RecordForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def record_list(request):
    records = ReadingRecord.objects.all()
    return render(request, 'record_list.html', {'records':records})

# def recoed_request(request, username):

@login_required(login_url='/account/login/')
def new(request):
    if request.method == "POST":
        form = RecordForm(request.POST) #request.FILES) ->  이미지 넣으면 필요:
        if form.is_valid():
            record = form.save(commit = False)
            record.created_at = timezone.datetime.now()
            record.updated_at = timezone.datetime.now()
            record.publisher = request.user.username
            record.save()
            return redirect('record_list')
    else:
        form = RecordForm()
        return render(request, 'new.html', {'form':form})

def detail(request, record_id):
    record = get_object_or_404(ReadingRecord, pk = record_id)
    return render(request, 'detail.html', {'record':record})


@login_required(login_url='/account/login/')
def edit(request, record_id):
    user = request.user
    if user.is_authenticated and ReadingRecord.objects.get(pk=record_id).publisher == user.username:
        form = RecordForm(instance = ReadingRecord.objects.get(pk = record_id))
        return render(request, 'edit.html', {'form':form, 'record_id':record_id})
    elif user.is_authenticated:
        return detail(request, record_id)
    else:
        return redirect("login")

@login_required(login_url='/account/login/')
def update(request, record_id):
    update_record = get_object_or_404(ReadingRecord, pk = record_id)
    update_record.title = request.POST['title']
    
    update_record.author = request.POST['author']
    update_record.record_title = request.POST['record_title']
    update_record.read_at = request.POST['read_at']
    update_record.category = request.POST['category']
    update_record.record_body = request.POST['record_body']
    update_record.updated_at = timezone.datetime.now()
    # try:
    #     update_record.rep_img = request.FILES['rep_img']
    # except:
    #     pass
    update_record.save()
    return redirect('record_detail', update_record.id)

def delete(request, record_id):
    user = request.user
    if user.is_authenticated and ReadingRecord.objects.get(pk=record_id).publisher == user.username:
        delete_record = get_object_or_404(ReadingRecord, pk = record_id)
        delete_record.delete()
        return redirect('/')
    elif user.is_authenticated:
        return detail(request, record_id)
    else:
        return redirect("login")