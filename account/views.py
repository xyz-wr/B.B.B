from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages

# Create your views here.

def signup(request):
    if request.method == "POST":
        if request.POST["password"] == "" or request.POST["password"] == None:
            messages.error(request,"비밀번호를 입력해주세요.")
            return render(request, 'signup.html')
        elif request.POST["password"]  != request.POST["confirm password"]:
            messages.error(request, "비밀번호가 서로 다릅니다.")
            return render(request, 'signup.html')    
        elif len(request.POST["password"]) < 4:
            messages.error(request, "비밀번호가 너무 짧습니다.")
            return render(request, 'signup.html')  
        elif request.POST["password"]  == request.POST["confirm password"]:
            try:
                user = User.objects.create_user(
                    username = request.POST["username"], password = request.POST["password"])
                auth.login(request, user)
                return redirect('record_list')
            except:
                messages.error(request, "다른 사용자가 사용중인 username입니다.")
            return render(request, 'signup.html')
        return render(request, 'signup.html')

    return render(request, 'signup.html')

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username = username, password = password)
        if user is not None:
            auth.login(request, user)
            return redirect('record_list')
        else:
            messages.error(request, "username 혹은 password가 올바르지 않습니다.")
            return render(request, 'login.html', {'error': 'username or password is incorrect'})
    else:
        try:
            user = request.user
            auth.login(request, user)
            return redirect('record_list')
        except:
            pass
    return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')