import torch
import cv2

model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)  # 모델 받아오기

img = cv2.imread('dogcat.jpg')  # opencv로 파일열기

print(f'a. ({img.shape[0]}, {img.shape[1]})')  # a.(세로, 가로) 출력

results = model(img)
results.save()  #모델을 적용한 사진 저장 -> exp에 생길 것

result = results.pandas().xyxy[0].to_numpy()  # pandas 출력 결과를 넘파이 배열로 바꾼다
print(result)
result_dog = [item for item in result if item[6]=='dog']  # name이 dog인 것만 추출
result_cat = [item for item in result if item[6]=='cat']  # name이 cat인 것만 추출
print(result)

tmp_img = cv2.imread('dogcat.jpg')  # 이미지를 자를 원본
print(tmp_img.shape)
for idx, r in enumerate(result_dog):  # dog인 요소에 하나씩 접근
    cropped = tmp_img[int(r[1]):int(r[3]), int(r[0]):int(r[2])]  # [ymin:ymax, xmin:xmax] 형태로 전달 -> 해당 영역 자름
    cv2.imwrite(f'dog{idx+1}.png', cropped)  # 해당 강아지 사진만 따로 저장
    cv2.rectangle(tmp_img, (int(r[0]), int(r[1])), (int(r[2]), int(r[3])), (255,0,0))  # (xmin, ymin), (xmax, ymax) -> 하얀 박스 그리기
    # to_numpy로 이미 숫자형태로 바꾸었기에 item 불필요
for idx, r in enumerate(result_cat):  
    cropped = tmp_img[int(r[1]):int(r[3]), int(r[0]):int(r[2])]  
    cv2.imwrite(f'cat{idx+1}.png', cropped) 
    cv2.rectangle(tmp_img, (int(r[0]), int(r[1])), (int(r[2]), int(r[3])), (255,0,0))
cv2.imwrite('result1.png', tmp_img)  # 하얀 네모박스가 그려진 이미지를 result1.png로 저장