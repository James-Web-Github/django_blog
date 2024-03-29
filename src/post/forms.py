from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={
        'class':'form-control',
        'placeholder':'Type your comment',
        'id':'usercomment',
        'rows':'5'
    }))
    class Meta: 
        model = Comment
        fields = ('content',)