from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)
    contents = models.TextField()

    # 어떤 폴더에 이미지가 들어가는지 -> 사용자가 올린 이미지는 MEDIA 폴더로 들어간다.
    # 이미지를 저장할 때 폴더를 깊게 하여 저장하는 것이 좋다. -> 폴더의 depth가 깊을 수록 좋음
    # 폴더 트리 작성법!!!
    main_image = models.ImageField(upload_to="blog/%Y/%m/%d", blank=True) # 저장시 앱이름과 날짜를 사용한 이름으르 저장한다.
    # 이미지가 중복되면 이미지에는 난수가 들어가니 걱정하지 않아도 되지만
    # 이미지가 하나의 폴더에 많아졌을 경우, 성능 이슈가 있을 수 있으므로 폴더 분리를 권장하는 것
    # 아니면 filename에 날짜를 넣는 것도 좋은 방법입니다. -> 난수로 처리하면 보안성은 올라가지만 파일명을 알 수 없어서 관리가 어려울 수 있습니다.

    # 따라서 저장되는 폴더의 파일명을 잘 정해야한다. -> 위의 방식으로 하는 것을 추천(앱+날짜)
    # 한 폴더에 이미지를 저장하지말고 폴더를 분리하는 것이 좋다.
    
    # a.png => 2021/02/26/12345678.png 이렇게 되어 있어야 언제 업로드 되었는지 알 수 있다.
    # 만약에 a.png라고 저장이 되어있다면 
    # 방법 1. 자동화 스크립트를 만들어서 DB에서 게시물 생성 날짜를 가져와서 파일명을 재작성
    # 방버 2. 일관된 날짜로 (서비스 시작날짜) 폴더를 만들어서 그 안에 넣는 방법 -> 이 다음의 게시물부터 날짜를 다시 관리

    # 아래처럼 upload_to를 함수로 지정할 수도 있습니다.
    # def get_image_path(instance, filename):
    # # Post class의 인스턴스의 pk를 의미
    #     return f"blog/{instance.pk}/%Y/%m/{filename}"
    # main_image = models.ImageField(upload_to=get_image_path, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)  # 처음 생성될 때만 추가
    updated_at = models.DateTimeField(auto_now=True)  # 수정할 때마다 추가

    def __str__(self):
        return self.title