from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta: # 클래스 Meta로 연결할 수 있도록 ModelForm이 구현함
        model = Post
        fields = "__all__"


class CommentForm(forms.Form):
    message = forms.CharField(widget=forms.Textarea)
