from django import forms
from bullets.models import Board, Comment

class BoardForm(forms.ModelForm):
    class Meta:
        model = Board
        fields = ['title' , 'content']
        labels = {
            'title' : '제목',
            'content' : '내용',
        }
'''
        # 코드로 스타일을 주는건 프로그래머와 디자이너의 역할분담이 모호해진다. 그냥 가능하단것만 보여줌
        widgets = {
            'title': forms.TextInput(attrs={'class' : 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows' : 10}),
        }
'''
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        labels = {
            'content' : '댓글내용',
        }