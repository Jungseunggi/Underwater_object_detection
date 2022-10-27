# Underwater_object_detection

## 1. 프로젝트 목적 및 배경 

- 아티슨앤오션은 다이버들을 위해서 스마트폰으로 촬영가능하게 만드는 장비를 만들고 있음.

- 이 사업은 선두주자로 시작하여 업계에서 상위권이지만 다른업체와의 차별을 위해 수중탐지모델을 기획.

- 하지만 수중에서의 이미지는 지상보다는 열악한 환경이라 많은 개선이 필요함.

- 따라서 수중생물탐지모델을 어떻게 성능을 높일 수 있을지가 목적.

## 2. 프로젝트를 통해 얻는 이익 

- 다이브로드는 비싼장비를 사지못하는 사람들에게 대안책으로 파고드는 것으로 느낌.

- 따라서 입문자들에게 인기가 있을텐데 입문자들은 수중생물에 대해 잘 알지 못함.

- 결론적으로 입문자들에게 조금 더 흥미롭고 도움이 되어 다른 제품들과는 차별점을 둔다고 생각함.


## 3. 프로젝트 과정  

### 3.1 데이터 수집과정

- 카테고리 선정 참고 사이트(https://www.diverbliss.com/marine-life-in-the-philippines/)

- pytube, selenium을 통해 데이터 수집 후 라벨링 진행

<img src="https://user-images.githubusercontent.com/102225200/197954799-db44f116-8cbc-43f4-9c69-a3c7a80802c1.png" width="600">

- 데이터 수집 및 라벨링 시간이 부족하여 모델링 훈련 및 테스트는 roboflow에서 사용(https://universe.roboflow.com/maeo/maeo)

<img src="https://user-images.githubusercontent.com/102225200/197955087-fcdf9435-1e5f-4ee3-afb1-15db2d041bf1.png" width="600">

### 3.2 모델 구현 과정

- 프로젝트 과정을 구상하기 위에 다양한 논문 중에 구현 가능할것으로 보이는 것을 참고(참고 논문 : Underwater Species Detection using Channel Sharpening Attention)

- Water-Net, CSAM을 통한 이미지 전처리 후 객체탐지 진행으로 구상

<img src="https://user-images.githubusercontent.com/102225200/197946461-0c7bc212-4fd9-4fe5-b7c3-5fc6dadc8106.png" width="600">

- Water-Net을 통해 이미지의 GC(gamma correction), WB(white balance), HE(histogram equalization) 개선

<img src="https://user-images.githubusercontent.com/102225200/197948857-0489c21b-9714-43c1-85fa-2edb25f87b71.gif" width="600">

- Water-Net의 문제점 -> 센터의 물체는 오히려 대비가 좋아졌지만 뒤에 있는 물체는 오히려 대비가 적어져 분간하기가 어려움


<img src="https://user-images.githubusercontent.com/102225200/197956383-418f372e-fe1c-44bb-99da-7d2f0458607e.png" width="600">

<sub> 위 : 적용 전,  아래 : 적용 후</sub>




- CSAM구현 못함 -> 대안방법 시도

<img src="https://user-images.githubusercontent.com/102225200/197949045-b652a5bc-df5f-4e28-8e6a-c0d140560c9b.png" width="600">


<img src="https://user-images.githubusercontent.com/102225200/197949582-e1284efe-f9aa-427d-873b-507ab231009f.png" width="600">



## 4. 프로젝트 결과  

<img src="https://user-images.githubusercontent.com/102225200/197946615-fd170e38-a4b2-44f5-b497-bfade89dab5c.png" width="600">


- 큰 차이는 없지만 이미지 전처리를 한 후 mAP가 조금 더 높은 것을 확인.

- F1_Confidence Curve를 통해 이미지 전처리를 통해 훈련을 한 모델은 더 높은 신뢰도에서 좋은 결과가 나오므로 성능이 더 좋은 것으로 판단

- CSAM대안으로 제시한 OpenCV sharpen 기능은 결과가 더 안좋아짐.



<img src="https://user-images.githubusercontent.com/102225200/197950167-706f1eea-de65-4c61-9094-fc2b355c427e.png" width="600">

- 이미지 테스트결과 전처리 전에는 탐지못하거나 다른객체로 인식하는걸 제대로 인식함.


## 5. 회고 및 느낀점

- 이미지 전처리를 통해 성능이 향상됨

- 테스트를 통해 문제점이 왜 그런이유가 발생했는지 분석

- 이미지 전처리단계에서 CSAM을 구현 못하였고 대안책으로 제시한 2가지 방법모두 성능이 떨어짐.

- Water-Net의 문제점도 있었지만 지식과 학습이 부족하여 모델의 수정을 못함

- 객체탐지에서 사용한 Yolov5s의 백본과 헤드부분을 Yolov7 참고하여 수정하여 시간과 성능을 높이고 싶었지만  지식과 시간이 부족하여 수정을 못함.

- 데이터 수집단계에서는 수중생물에 대한 지식이 없어서 카테고리 선정에서 시간을 많이 소비

