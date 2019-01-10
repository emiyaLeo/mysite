from django import forms
from .models import Comment
from ckeditor.widgets import CKEditorWidget

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)
        labels = {'text':''}
        widgets = {'text':CKEditorWidget}
