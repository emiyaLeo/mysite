from django import forms
from .models import Comment
from django.forms import widgets

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)
        labels = {'text':''}
        widgets = {'text':widgets.TextInput(attrs={'class': 'form-control'})}


