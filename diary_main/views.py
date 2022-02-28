from django.shortcuts import render, redirect
from diary_main.models import Board
from diary_main.forms import BoardForm, BoardDetailForm

# Create your views here.

def b_list(request):
    if request.user.is_authenticated:
        posts = Board.objects.all().order_by('-id')
        context = {
            "posts": posts
        }
        return render(request,'diary_main/list.html',context)
    else:
        return redirect('home')

def b_create(request):
    if request.method == 'GET':

        # 새글을 작성할 수 있는 화면을 클라이언트에게 전달.
        # 입력 양식인 ModelForm 객체를 하나 생성할거임
        board_form = BoardForm()

        context = {
            "my_form" : board_form
        }

        return render(request,'diary_main/create.html', context)

    else:
        # POST방식인 경우에는 이부분이 수행됨!
        # 클라이언트가 입력상자에 입력한 내용을 가지고 Database처리를 한다.
        board_form = BoardForm(request.POST) # 모델폼 객체긴한데 클라이언트가 입력한 데이터를 가지고 있는 모델폼

        if board_form.is_valid():  # board_form안에 제데로 처리됐으면을 의미
            board_form.save() # BoardForm 안에 있는 데이터를 이용해서 Board class의 객체를 생성
            #만약 입력 받은 값 이외에 테이블의  다른  컬럼의 값을 지정해서 사용하면?
            # new_post = board_form.save(commit=False) # 실제로 저장되지 않음! 대신 객체를 리턴 / 저장은 시키는데 바로 저장은 시키지 말라는 의미
            # new_post.b_like_count = 10
            # new_post.save()
            return redirect('bbs:b_list')