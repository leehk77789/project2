import tensorflow
import numpy as np
import cv2

#부동소수점 번호를 인쇄(컴퓨터 숫자 표기 방식)
np.set_printoptions(suppress=False)
#모델 로드
model=tensorflow.keras.models.load_model('dog.h5')
#ndarray = 다차원 행렬 자료구조 클래스 list와 동일한 출력 형태
data=np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

img=cv2.imread('./dog.jpg')

if img is None:
    print('Wrong path:', 'dog.jpg')
else:
    img=cv2.resize(img, dsize=(224, 224))

#asarray:데이터형태가 같으면 복사하지 않는다. ex)float32 and float64
image_array=np.asarray(img)

#정규화
normalized_image_array=(image_array.astype(np.float32) / 127.0)-1
data[0]=normalized_image_array

#예측
prediction=model.predict(data)

for i in prediction:
    if i[0]>0.7:
        text="골든 리트리버"
    img=cv2.resize(img,(500,500))
    cv2.putText(img,text,(10,30),cv2.FONT_ITALIC,1,(0,255,0),2)
cv2.imshow('img',img)
cv2.waitKey(0)