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
        
        post.save()



        model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)  # 모델 받아오기        uploaded_img_qs = I.objects.filter().last()
        
        img_bytes = uploadPostd_img_qs.image.read()

        img = im.open(io.BytesIO(img_bytes))

        # Change this to the correct path
        print(f'a. ({img.shape[0]}, {img.shape[1]})')  # a.(세로, 가로) 출력

        results = model(img)
        results.save()  #모델을 적용한 사진 저장 -> exp에 생길 것        
        result = results.pandas().xyxy[0].to_numpy()  # pandas 출력 결과를 넘파이 배열로 바꾼다
        print(result)
        result_dog = [item for item in result if item[6]=='dog']  # name이 person인 것만 추출
        print(result_dog)
        result_cat = [item for item in result if item[6]=='cat']  # name이 person인 것만 추출
        print(result_cat)

        for idx, r in enumerate(result_dog):  # person인 요소에 하나씩 접근
            cropped = tmp_img[int(r[1]):int(r[3]), int(r[0]):int(r[2])]  # [ymin:ymax, xmin:xmax] 형태로 전달 -> 해당 영역 자름
            cv2.imwrite(f'dog{idx+1}.png', cropped)  # 해당 인물 사진만 따로 저장
            cv2.rectangle(img, (int(r[0]), int(r[1])), (int(r[2]), int(r[3])), (255,255,255))  # (xmin, ymin), (xmax, ymax) -> 하얀 박스 그리기

        for idx, r in enumerate(result_cat):  # person인 요소에 하나씩 접근
            cropped = tmp_img[int(r[1]):int(r[3]), int(r[0]):int(r[2])]  # [ymin:ymax, xmin:xmax] 형태로 전달 -> 해당 영역 자름
            cv2.imwrite(f'cat{idx+1}.png', cropped)  # 해당 인물 사진만 따로 저장
            cv2.rectangle(tmp_img, (int(r[0]), int(r[1])), (int(r[2]), int(r[3])), (255,255,255))  # (xmin, ymin), (xmax, ymax) -> 하얀 박스 그리기
            # to_numpy로 이미 숫자형태로 바꾸었기에 item 불필요

        cv2.imwrite('media/images/result.png', tmp_img)  # 하얀 네모박스가 그려진 이미지를 result1.png로 저장

        
        path_hubconfig = "absolute/path/to/yolov5_code"
        path_weightfile = "absolute/path/to/yolov5s.pt"  # or any custom trained model

        model = torch.hub.load(path_hubconfig, 'custom',
                            path=path_weightfile, source='local')

        resu= model(img, size=640)
            lts.render()
            for img in results.imgs:
                img_base64 = im.fromarray(img)
                img_base64.save("media/yolo_out/image0.jpg", format="JPEG")

            inference_img = "/media/yolo_out/image0.jpg"

            form = ImageUploadForm()
            context = {
                "form": form,
                "inference_img": inference_img
            }
            return render(request, 'image/imagemodel_form.html', context)

        else:
            form = ImageUploadForm()
        context = {
         
        return red('/users/main')   "form": form
        }
        return render(request, 'image/imagemodel_form.html', context)
        