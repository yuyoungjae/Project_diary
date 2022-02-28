# ModelForm class를 여기에 작성

# ModelForm class를 만드려면 Django가 제공해주는 기능(class)를
# 이용해야 해요. (class를 상속받아서 작성해야 해요)

from django import forms
from diary_main.models import Board


class BoardForm(forms.ModelForm):
    class Meta:
        model = Board
        # fields = "__all__"
        fields = ['b_title', 'b_img', 'b_author', 'b_content']
        #
        labels = {
            'b_title': '글 제목',
            'b_img': '이미지',
            'b_author': '글 작성자',
            'b_content': '글 내용'
        }
        #
        widgets = {
            'b_title': forms.TextInput(
                attrs={
                    'class': 'form-control w-50',
                             'placeholder': '제목을 입력하세요!'
                }
            ),
            'b_author': forms.TextInput(
                attrs={
                    'class': 'form-control w-25',
                    'placeholder': '작성자를 입력하세요!'
                }
            ),
            'b_content': forms.Textarea(
                attrs={
                    'class': 'form-control w-75',
                    'placeholder': '글 내용을 입력하세요!'
                }
            )  # Textarea() : 여러 줄짜리 입력상자
        }


class BoardDetailForm(forms.ModelForm):
    class Meta:
        model = Board
        fields = '__all__'

        labels = {
                    'b_title': '글 제목',
                    'b_img': '이미지',
                    'b_author': '글 작성자',
                    'b_content': '글 내용',
                    'b_comment_count': '댓글 개수',
                    'b_like_count': '좋아요 개수'
                }

        widgets = {
            'b_title': forms.TextInput(
                attrs={
                    'class': 'form-control w-50'
                }
            ),
            'b_img': forms.TextInput(
                attrs={
                    'class': 'form-control w-25'
                }
            ),
            'b_author': forms.TextInput(
                attrs={
                    'class': 'form-control w-25'
                }
            ),
            'b_content': forms.Textarea(
                attrs={
                    'class': 'form-control w-75'
                }
            ),
            'b_comment_count': forms.TextInput(
                attrs={
                    'class': 'form-control w-25'
                }
            ),
            'b_like_count': forms.TextInput(
                attrs={
                    'class': 'form-control w-25'
                }
            )
        }