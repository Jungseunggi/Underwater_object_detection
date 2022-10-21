# Underwater_object_detection

### 1. 프로젝트를 통해 해결하려고 했던 문제는 무엇이었나요? 왜 이런 프로젝트를 기획하고 실행했나요? 

- 아티슨앤오션은 다이버들을 위해서 스마트폰으로 촬영가능하게 만드는 장비를 만들고 있음.

- 이 사업은 선두주자로 시작하여 업계에서 상위권이지만 다른업체와의 차별을 위해 수중탐지모델을 기획.

- 하지만 수중에서의 이미지는 지상보다는 열악한 환경이라 많은 개선이 필요함.

- 따라서 수중생물탐지모델을 어떻게 성능을 높일 수 있을지가 목적.

### 2. 이 문제는 왜 중요한가요? 이 문제를 해결하면 어떤 가치(benefit)이 있을까요? 왜 그렇게 생각하시나요? 

- 다이브로드는 비싼장비를 사지못하는 사람들에게 대안책으로 파고드는 것으로 느낌.

- 따라서 입문자들에게 인기가 있을텐데 입문자들은 수중생물에 대해 잘 알지 못함.

- 결론적으로 입문자들에게 조금 더 흥미롭고 도움이 되어 다른 제품들과는 차별점을 둔다고 생각함.

### 3. 어떤 과정을 거쳐 프로젝트를 진행했나요?  

- Water-Net, CSAM을 통한 이미지 전처리 후 객체탐지 진행으로 구상 

### 4. 프로젝트 결과는 어떤가요?  

- 큰 차이는 없지만 이미지 전처리를 한 후 mAP가 조금 더 높은 것을 확인.

- F1_Confidence Curve를 통해 이미지 전처리를 통해 훈련을 한 모델은 더 높은 신뢰도에서 좋은 결과가 나오므로 성능이 더 좋은 것으로 판단

- CSAM대안으로 제시한 OpenCV sharpen 기능은 결과가 더 안좋아짐.

- 이미지 테스트결과 전처리 전에는 탐지못하거나 다른객체로 인식하는걸 제대로 인식함.

### 5. 잘 한 점, 만족한 점은 무엇인가요? 

- 이미지 전처리를 통해 성능이 향상됨

- 테스트를 통해 문제점이 왜 그런이유가 발생했는지 분석

### 6. 아쉬운 점, 한계점은 무엇인가요?

- 이미지 전처리단계에서 CSAM을 구현 못하였고 대안책으로 제시한 2가지 방법모두 성능이 떨어짐.

- Water-Net의 문제점도 있었지만 지식과 학습이 부족하여 모델의 수정을 못함

- 객체탐지에서 사용한 Yolov5s의 백본과 헤드부분을 Yolov7 참고하여 수정하여 시간과 성능을 높이고 싶었지만  지식과 시간이 부족하요 수정을 못함.

- 데이터 수집단계에서는 수중생물에 대한 지식이 없어서 카테고리 선정에서 시간을 많이 소비

