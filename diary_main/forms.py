# modelform class를 여기에 작성해요!

# modelForm class를 만들려면 Django가 제공해주는 기능(class)를 이용해야해요!
# class를 상속받아서 작성해야함

from django import forms
from diary_main.models import Board

# modelform을 이용을하는데 어떤 modelform을 이용하는지 class Meta를 통해
# 이 모델폼이 어떤 모델과 관련이 있는지 화면에 사용하는 필드는 어떤 필드를 사용할지 정함
# model, fields 다 정해져 있음

class BoardForm(forms.ModelForm):
    class Meta:
        model = Board
        # fields = '__all__'
        # 테이블에있는 모든 데이터를 가져와서 좋아요개수와 댓글 개수도 가져옴 하지만 이건 작성자가 정하는게 아님
        # all을 사용해서 테이블에 사용된 모든 컬럼을 찍음 그렇기 때문에 all이 아닌 내가 정한것만 나오게 바꿔주면 됨
        fields = ['b_title','b_author','b_content']
        # 하지만 이렇게 출력하면 원하는것만 출력이 되지만 타이틀이 B title(label) 이런식으로 나와 맘에 안든다.

        labels = {
            'b_title': '글 제목',
            'b_author': '글 작성자',
            'b_content': '글 내용'
        }
        # 이제 타이틀도 바뀌었지만 그 내부의 입력상자도 "글 제목"이라써있어서 맘에 안들기 때문에 이 두가지를 편집해보자
        # 글 내용의 경우 한줄짜리 텍스트 상자가 아닌 여러줄 짜리 텍스트 상자로 바꿔야한다.(widgets)를 선언해서 바꾸자

        widgets = {
            'b_title': forms.TextInput(
                attrs= {
                    'class': 'form-control w-50',# bootstrap css임 w-50은 화면에 보이는 칸의 길이를 의미
                    'placeholder': '제목을 입력하세요' # 회색으로 된 입력상자 안에 글을 의미 이 내용을 바꿔줄 수 있음
                }
            ),    # TextInput() 한줄짜리 입력상자
            # 입력상자의 스타일을 변경하기 위해 ()안에 속성을 변경해 주면됨

            'b_author': forms.TextInput(
                attrs= {
                    'class': 'form-control w-25',
                    'placeholder': '작성자를 입력하세요'
                }
            ),
            'b_content': forms.Textarea(
                attrs= {
                    'class': 'form-control w-75',
                    'placeholder': '글 내용을 입력하세요'
                }
            )    # TextArea() : 여러줄짜리 입력상자

        }

class BoardDetailForm(forms.ModelForm):
    class Meta:
        model = Board
        fields ="__all__" # 모든 데이터

        labels = {
            'b_title': '글 제목',
            'b_author': '글 작성자',
            'b_content': '글 내용',
            'b_comment_count': '댓글 개수',
            'b_like_count': '좋아요 개수'
        }


        widgets = {
            'b_title': forms.TextInput(
                attrs= {
                    'class': 'form-control w-50'# bootstrap css임 w-50은 화면에 보이는 칸의 길이를 의미
                }
            ),    # TextInput() 한줄짜리 입력상자
            # 입력상자의 스타일을 변경하기 위해 ()안에 속성을 변경해 주면됨

            'b_author': forms.TextInput(
                attrs= {
                    'class': 'form-control w-25'
                }
            ),
            'b_content': forms.Textarea(
                attrs= {
                    'class': 'form-control w-75',
                }
            ),    # TextArea() : 여러줄짜리 입력상자
            'b_comment_count': forms.TextInput(
                attrs= {
                    'class': 'form-control w-25'
                }
            ),
           'b_like_count': forms.TextInput(
                attrs= {
                    'class': 'form-control w-25'
                }
            )


        }

