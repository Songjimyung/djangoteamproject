from django import forms
from .models import Board
<<<<<<< HEAD
from django.contrib.auth.models import User


# 게시글 작성 폼
# 가져오는 값 : id, title, content
class BoardForm(forms.ModelForm):
    class Meta:
        model = Board
        fields = ('title', 'content', 'author')
=======

# forms.py


class BoardForm(forms.ModelForm):
    class Meta:
        model = Board
        fields = ['board_id', 'title', 'content']
>>>>>>> ad85b2fd6e281c1fbcce8b9c3a927d92031188b2
