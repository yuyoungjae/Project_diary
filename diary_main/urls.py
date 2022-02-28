from django.urls import path
from diary_main import views

# namespace 생성
app_name = 'diary_main'
# bbs의 application의 URLConf
# 여기까지의 경로는 -> http://127.0.0.1:8000/bbs/

urlpatterns = [
    path('list/', views.b_list, name='b_list'),
    path('create/', views.b_create, name='b_create'),
    path('<int:board_id>/detail/', views.b_detail, name='b_detail')
]
