from django.shortcuts import render, redirect
from django.contrib import auth, messages
from django.contrib.auth.models import User
from .models import *

# Create your views here.

def diary(request):
    if request.method == 'POST':
        title = request.POST['title']
        date = request.POST['date']
        score = request.POST['score']
        emotion = request.POST['emotion']
        other = request.POST['other']
        score = request.POST['score']
        detail = request.POST['detail']
        diary_info = Diary(title=title, date=date, emotion=emotion, other=other, score=score, detail=detail, author=request.user)
        diary_info.save()
        return redirect('diary')
    else:
        messages.add_message(request, messages.ERROR, '오류')
    return render(request, 'diary.html')

def home(request):
    userList = User.objects.all().filter(username=request.user)
    if userList:
        author = userList[0]
        diarys = Diary.objects.all().filter(author=author)
        return render(request, 'home.html', {'diarys':diarys}) 
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'home.html', {'error':'아이디 혹은 비밀번호가 맞지 않습니다.'})    
    return render(request, 'home.html')

def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(
                request.POST['username'], password=request.POST['password1']
            )
            auth.login(request, user)
            return redirect('home')
    return render(request, 'signup.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')
    return render(request, 'signup.html')

def reserve(request):
    if request.method == 'POST':
        user = request.user
        name = request.POST['name']
        sex = request.POST['sex']
        nick = request.POST['nick']
        diary_open = request.POST['diary']
        center_exp = request.POST['center_exp']
        about = request.POST['about']
        info = Reserve(user=user, name=name, sex=sex, nick=nick, diary_open=diary_open, center_exp=center_exp, about=about)
        info.save()
        age = request.POST['age']
        school = request.POST['school']
        school_others = request.POST['school_others']
        parent = request.POST.getlist('parent')
        reason = request.POST['reason']
        sibling = request.POST['sibling1'] + '남 ' + request.POST['sibling2'] + '녀 중 ' + request.POST['me'] + '째'
        print("---------"+sibling)
        marriage = request.POST['marriage']
        child = request.POST['child']
        child_num = request.POST['child_num']
        addtion_info = Additional(user=user, age=age, school=school, school_others=school_others, parent=parent, reason=reason, sibling=sibling, marriage=marriage, child=child, child_num=child_num)
        addtion_info.save()
        return redirect('home')
    else:
        return render(request, 'home.html', {'fault':'저장실패 혹은 오류'})
    

def socialLogin(request):
   login_request_uri = 'https://kauth.kakao.com/oauth/authorize?'
   client_id = '734408998612482f00ad4096fda15b12'
   redirect_uri = 'http://localhost:8000/accounts/oauth'
   login_request_uri += 'client_id=' + client_id
   login_request_uri += '&redirect_uri=' + redirect_uri
   login_request_uri += '&response_type=code'
   request.session['client_id'] = client_id
   request.session['redirect_uri'] = redirect_uri
   return redirect(login_request_uri)

def oauth(request):           
    code = request.GET['code']
    print('code = '+ str(code))
    
    client_id = request.session.get('client_id')
    redirect_uri = request.session.get('redirect_uri')

    access_token_request_uri = "https://kauth.kakao.com/oauth/token?grant_type=authorization_code&"
 
    access_token_request_uri += "client_id=" + client_id
    access_token_request_uri += "&redirect_uri=" + redirect_uri
    access_token_request_uri += "&code=" + code
 
    print(access_token_request_uri)
    
    return redirect('home')

def verification(request):
    if request.method == 'POST':
        messages.INFO(request, '인증완료')
        return render(request, 'home.html')
    return render(request, 'verification.html')
        
        
        
