from django.shortcuts import render, redirect
from .models import Post
import io
from PIL import Image as im
import torch
import cv2

# Create your views here.
def upload(request):
    if request.method == 'POST':
        post = Post()
        post.user = request.user
        post.image = request.FILES.get('img')
        
        post.save()  # 이미지 db에 저장



        model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)  # 모델 받아오기        
    
        uploadPosted_img_qs = Post.objects.filter().last()  # db의 가장 마지막 사진
       
        img = cv2.imread(uploadPosted_img_qs.image)  # opencv로 파일열기
    
        results = model(img)
        results.save()  #모델을 적용한 사진 저장 -> exp에 생길 것        
        result = results.pandas().xyxy[0].to_numpy()  # pandas 출력 결과를 넘파이 배열로 바꾼다
        print(result)
        result_dog = [item for item in result if item[6]=='dog']  # name이 dog인 것만 추출
        print(result_dog)
        result_cat = [item for item in result if item[6]=='cat']  # name이 cat인 것만 추출
        print(result_cat)

        for idx, r in enumerate(result_dog):  # dog인 요소에 하나씩 접근
            cropped = img[int(r[1]):int(r[3]), int(r[0]):int(r[2])]  # [ymin:ymax, xmin:xmax] 형태로 전달 -> 해당 영역 자름
            cv2.imwrite(f'dog{idx+1}.png', cropped)  # 해당 강아지 사진만 따로 저장
            cv2.rectangle(img, (int(r[0]), int(r[1])), (int(r[2]), int(r[3])), (255,0,255))  # (xmin, ymin), (xmax, ymax) -> 색깔 박스 그리기
            print(img.shape)
            

        for idx, r in enumerate(result_cat):  # cat인 요소에 하나씩 접근
            cropped = img[int(r[1]):int(r[3]), int(r[0]):int(r[2])]  # [ymin:ymax, xmin:xmax] 형태로 전달 -> 해당 영역 자름
            cv2.imwrite(f'cat{idx+1}.png', cropped)  # 해당 고양이 사진만 따로 저장
            cv2.rectangle(img, (int(r[0]), int(r[1])), (int(r[2]), int(r[3])), (255,255,0))  # (xmin, ymin), (xmax, ymax) -> 색깔 박스 그리기
            # to_numpy로 이미 숫자형태로 바꾸었기에 item 불필요
        cv2.imwrite('./static/media/result/result.png', img)  # 네모박스가 그려진 이미지를 result.png로 저장

        return redirect('/users/main') # main url 호출