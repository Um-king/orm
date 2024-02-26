from django import forms
from .models import Post


# class PostForm(forms.ModelForm):  # forms.ModelForm!! -> forms.Form이 원래 기본 Form인데 이것을 사용한다.
#     title = forms.CharField(max_length=10)
#     contents = forms.CharField(widget=forms.Textarea)

#     class Meta:
#         model = Post # 모델의 포스트를 읽어와서 포스트 폼을 연결한다
#         fields = ["title", "contents"]



# 모든 필드를 쓰겠다!
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = "__all__"