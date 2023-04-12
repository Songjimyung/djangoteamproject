from django import forms
from .models import Board

# forms.py


class BoardForm(forms.ModelForm):
    class Meta:
        model = Board
        fields = ['board_id', 'title', 'content']
