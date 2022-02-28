from django.urls import path
from diary_main import views

app_name = 'diary_main'
# ROOT_URLConf
# 여기까지의 경로는 => http://127.0.0.1:8000/diary_main/
urlpatterns = [
                  path('list/',views.b_list, name = 'b_list'),
                  path('create/', views.b_create, name='b_create'),
              ]