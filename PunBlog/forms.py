from .models import Commnent
from django import forms



class CommentForm(forms.ModelForm):
    class Meta:
        model = Commnent
        fields = ('body', )