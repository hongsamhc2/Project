# 				Project

###### 소개

​	파이썬 언어로 머신 러닝/딥러닝 프로젝트와 웹 프론트엔드 개발 프로젝트를 진행한다.



목록

- 딥러닝
  - DDQN- 강화학습 기반 주식 트레이딩 시스템
  - LSTM을 이용한 주가 예측
- 머신러닝
  - 선형 회귀 모델을 이용한 데이터 예측 분석
- 웹 프론트엔드
  - 공공 데이터 포털 - 데이터 다운로드 사이트
  - 개인 포트폴리오 사이트

## 딥러닝

###### 소개

- Tensorflow 와 Keras 신경망으로 이용한 학습모델 프로젝트
- 링크 https://github.com/hongsamhc2/Project/tree/main/DDQN-RL_Trading_System

### DDQN-강화학습 기반 주식 트레이딩 시스템

###### 소개

- DDQN 알고리즘을 이용한 주식 자동화 강화학습 프로젝트
- 인공 신경망을 정책을 통한 행동과 보상으로 가치 신경망 학습

###### 개발환경

- 사용언어 - 파이썬

- 라이브러리
  - Tensorflow
  - keras
  - numpy
  - pandas
- 대신증권 API

![Cap 2020-11-02 22-36-21-604](https://user-images.githubusercontent.com/69662531/97874020-c0466380-1d5b-11eb-97b9-3442f8690d3c.png)

### 케라스 주식 가격 예측

###### 소개

- 텐서플로우 케라스 신경망 모델을 사용한 딥러닝 학습
- LSTM 신경망을 통해 주식 종가 예측 (삼성전자)

![Cap 2020-11-03 21-37-51-302](https://user-images.githubusercontent.com/69662531/97985063-0ca4a880-1e1b-11eb-99a4-6ddac4eb800e.png)

## 머신러닝

소개

- 머신러닝 선형회귀 모델들을 이용한 주가 가격 예측
- LinearRegression / XGBoost Regressor 


![Cap 2020-11-03 21-46-12-322](https://user-images.githubusercontent.com/69662531/97985866-33afaa00-1e1c-11eb-834e-00b367471a4e.png)

![Cap 2020-11-03 21-45-09-336](https://user-images.githubusercontent.com/69662531/97985775-111d9100-1e1c-11eb-904c-19d2c4201ab4.png)




## 웹 프론트엔드

​	HTML , CSS, JS를 이용한 웹 프론트엔드 사이트를 제작합니다.서버로는 파이썬의 Flask 프레임워크를 사용합니다.



### 개인 포트폴리오 사이트

###### 소개

- 개인적으로 진행한 프로젝트들을 소개하는 포트폴리오 사이트
- 링크https://github.com/hongsamhc2/Project/tree/main/Web-PortFolio



###### 개발환경

- 파이썬, HTML ,CSS, jQuary
- 서버 - Flask 프레임워크


![Cap 2020-11-04 10-49-36-358](https://user-images.githubusercontent.com/69662531/98062652-d0f8f580-1e91-11eb-9909-0db88fbec45d.jpg)

### 공공 데이터 포털 - 데이터 다운로드 사이트

###### 소개

​	공공 데이터 포털의 REST API 로 제공되는 JSON / XML 형식의 데이터들을 URL 과 서비스키 / 요청 변수 입력시 CSV파일 형태로 다운로드를 제공하는 사이트

​	URL 형식으로 데이터를 요청하고 JSON /XML로 응답받아 프로그래밍 언어를 통해 재가공해야하는 과정의 복잡함을 피하고자 시작한 프로젝트

![Cap 2020-11-04 11-07-20-821](https://user-images.githubusercontent.com/69662531/98061077-70b48480-1e8e-11eb-93c7-1964177cafe3.png)



## 파이썬-모듈

###### 소개

​	프로젝트를 진행하면서 데이터 수집, 분석, 처리, 실행등에 관련된 필수 적인 모듈이나 프로젝트에 들어 가지는 않았지만, 진행하면서 쓰였던 중요한 모듈들을 소개한다.



### 아파트_실거래가 데이터 수집 모듈

- 국내 부동산 데이터 분석을 위한 아파트 실거래가를 수집하는 모듈
- 링크 https://github.com/hongsamhc2/Project/tree/main/Python-Module



###### 라이브러리

- urllib
- bs4

###### <예시>

- 법정동 코드 - 11110
- 날짜 년/월 - 202010
![Cap 2020-11-02 22-07-48-651](https://user-images.githubusercontent.com/69662531/97870975-1f55a980-1d57-11eb-8c7d-01142de82e2b.png)

### 대신증권 API 모듈

- 32비트 파이썬을 통한 API 데이터 요청 응답처리
- 주가 분단위 데이터및 일별 데이터 수집
