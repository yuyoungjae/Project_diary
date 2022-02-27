from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
import tkinter.messagebox





# 장고가 가지고 있는 인증 기능
from django.contrib.auth import authenticate

# logout 이름이 겹치기 때문에 모듈 이름을 다르게 가져옴
from django.contrib.auth import logout as django_logout

# login 이름이 겹치기 때문에 모듈 이름을 다르게 가져옴
from django.contrib.auth import login as django_login

# 만든 loginForm 불러오기
from users.forms import LoginForm

#함수 선언
# alert_js ='''
# function new_post() {
#     alert('실패했습니다!');
# }
# '''




# Create your views here.
# 함수명과 장고가 제공해주는 모듈이름이 겹침 주의
# render : templates을 불러옴
# redirect : URL로 이동 => 이동하는 URL에 맞는 view가 다시 실행되고, render할지/redirect할지 결정
def login(request):
    login_form = LoginForm()
    context = {
        "my_form": login_form
    }
    return render(request, 'users/login.html', context)


def logout(request):
    # 장고가 제공해주는 logout기능 사용
    django_logout(request)
    return redirect('home')


def login_process(request, messagebox):
    # 사용자가 request를 보내는데, 그 방식이 POST 방식이라면
    if request.method == 'POST':
        # 사용자가 보낸 request안에 POST 형식으로 보낸 정보가 들어감
        login_form = LoginForm(request.POST)
        username = login_form.data['username']
        password = login_form.data['password']

        # 로그인 인증처리
        user = authenticate(username=username,
                            password=password)

        # 유저 객체가 있다면
        if user is not None:
            django_login(request, user)  # 로그인 처리
            return redirect('home')  # 하고 홈으로 보냄

        # 유저 객체가 없다면
        else:
            # tkinter.messagebox.showinfp("메세지", "오류")
            # messages.error(self.request, '사용자를 찾을 수 없습니다 !_!')
            # return HttpResponse('사용자를 찾을 수 없습니다 !_!')
            # return redirect('home')
            # return



