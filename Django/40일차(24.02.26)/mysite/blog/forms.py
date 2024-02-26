from django import forms
from .models import Post

class PostForm(forms.Form):  # PostForm은 여러분이 원하는 이름으로 바꿔도 됩니다. forms.Form은 기본 form입니다. 이는 추후 forms.ModelForm로 바뀌어야 합니다.
    title = forms.CharField(max_length=100) # 가져온 내용을 해당 필드로 사용하겠다.
    contents = forms.CharField(widget=forms.Textarea)
    
    # 해당 코드가 우리가 위에서 설정한 출력할 내용의 Form을 Model에 반영하는 것
    class Meta:
        model = Post # Form 클래스를 ModelForm으로 바꾸는 작업 -> 이렇게 해줘야한다.
        fields = ["title", "contents"] # 어떤 필드를 보여줄 것이냐
        # 이런 식으로 fields를 설정해줘야 내가 {{form}}을 출력할때 어떤 것을 보여줄지 선택하는 것

        # fields = '__all__' # 이런식으로도 전체 내용을 호출할 수 있지만 잘 사용하지 않는다.