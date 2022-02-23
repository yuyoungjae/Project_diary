from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from users.models import Member


class Member(AbstractUser):
    mobile = models.CharField(max_length=20)
    image = models.ImageField(upload_to=settings.MEDIA_ROOT,
                              blank=True,
                              null=True)
    nickname = models.CharField(max_length=20,
                               unique=True)

class Board(models.Model):
    b_title = models.CharField(max_length=50)  # 글 제목
    # b_author = models.CharField(max_length=20)  # 글 작성자
    # Foreign Key 설정
    b_author = models.ForeignKey(Member,
                                 on_delete=models.CASCADE)
    b_content = models.CharField(max_length=200)  # 글 내용
    b_date = models.DateTimeField(auto_now=True)  # 글 작성 시간
    # auto_now=True => 현재 시간이 자동으로 삽입
    b_comment_count = models.IntegerField(default=0)  # 댓글 개수
    b_like_count = models.IntegerField(default=0)  # 좋아요 개수

    def __str__(self):
        return self.b_title

    class Comment(models.Model):
        # c_author = models.CharField(max_length=20)  # 댓글 작성자
        c_author = models.ForeignKey(Member,
                                     on_delete=models.CASCADE)
        c_content = models.CharField(max_length=100)  # 댓글 내용
        # board라는 class variable은 실제 table이 생성되면
        # board_id라는 이름의 column으로 생성되고 ForeignKey로 설정
        board = models.ForeignKey(Board,
                                  on_delete=models.CASCADE)

        def __str__(self):
            return self.c_content

