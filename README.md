<<<<<<< README.md
## 김승우
### 역할 분담
김승우 : 프로젝트 생성, 모델 생성, url 작성 그리고 search 함수 구현 단계에서 navigator,
serializer 및 view 함수 작성 과정에서 driver 역할을 맡았다.

### 새로 배운 점



## 이가희

### 역할 분담
이가희 : 프로젝트 생성, 모델 생성, url 작성 그리고 search 함수 구현 단계에서 driver 역할을 맡았고,
serializer 및 view 함수 작성 과정에서 navigator 역할을 맡았다.

### 새로 배운 점
장고에서는 파이썬 데이터를 보통 queryset으로 가져오는데, 이때 브라우저는 queryset으로 받아온 데이터를 읽지 못한다. 따라서 파이썬 코드를 읽을 수 있게 JSON형태로 변환해주는 Serializer를 사용해줘야 한다. Serializer는 모델에서 정의한 것들을 다시 써줘야하지만, ModelSerializer를 사용한다면 모델 필드를 기반으로 Serializer의 필드들이 자동으로 결정되었다. 

filter를 활용해 줄거리, 영화제목을 이용한 검색 기능을 구현하는 방법을 배웠다.

DB에서 다른 테이블을 참조할 때는 Foreign Key를 사용하고, 자신을 참조하는 테이블을 참조할 때는 related_name을 사용한다. 
예시: Comment객체는 Post 객체를 ForeignKey로 가진다. Post가 자신을 참조하는 Comment를 가려오는 역참조 상황이라면 related_name을 사용한다.

### 어려웠던 점
serializers.py를 작성하는 과정에서 ModelSerializer가 아닌 Serializer를 불러와서 POSTMAN에 JSON데이터가 뜨지 않았었다.
해당 실수를 발견하기까지 오래 걸렸고, 이번 프로젝트를 통해 확실하게 Serializer와  ModelSerializer의 차이를 알게되었다.

### 느낀 점
처음 페어 프로그래밍을 진행해봤는데, Navigator와 Driver역할 모두 기능과 코드를 자세히 알아야했으며, 모르는 것을 발견하고
채우는 과정이 굉장히 많은 도움이 됐던 것 같다.
