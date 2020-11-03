# DDQN Reinforcement Learning Trading System

## DDQN 강화학습 주식 트레이딩 시스템

###### 소개 

- DDQN 알고리즘을 이용한 강화학습 주식 트레이딩 시스템

###### 개발환경

- 사용언어 - 파이썬
- IDE - PyCharm
- 라이브러리
  - Tensorflow
  - Keras
  - Pandas
  - Numpy
  - Matplotlib 
  - 등등



###### 개요

- 환경에서 주어진 State를 받아 Policy를 통해 Action 을 행동한다. 행동한 Action에 따른 Reward를 받게 되고 Q-value를 구하여 신경망을 학습하여 더 좋은 Reward을 받는 방향으로 모델을 업데이트한다.
- Keras의 인공신경망을 통해 가치 신경망을 구성하여 학습을 진행한다.
- 주식 데이터는 대신증권 API를 통해 수집한 종목별 일별 데이터를 사용하였으며, 실제 주식한경을 구성하는 것이 관건이라고 볼 수 있다.
- State 또는 Observation으로 주어지는 데이터는 아래와 같다.
  - [현재가,전일 종가, 전일 대비, 시가, 고가,저가,누적 거래량, 전일 거래량, 전일 거래랭 대비]
- 앞으로의 데이터 Feature는 추가 되거나 수정될 수 있다.



### Step.1

###### 개요

- 데스트를 진행할 환경을 일별 과거데이터를 저장해 높은 csv파일을 DataFrame으로 만들어 사용하였다.
- 일별 데이터의 종가를 현잭로 설정하였다.
- 보상을 (잔금 + 보유 주식수 * 현재가) - 초기자본금 / 초기자본금으로 설정 하였다.
- 보상 정책에 대한 수정이 필요로 한다.
- 학습에 대한 수익률이 일정치 않은것으로 판단되며, 매수/ 매도량을 1로 설정한 부분과 지속적인 + 수익률을 만들 수 있는 모델을 만드는 것이 앞으로의 과제라고 판단된다.

###### <시각화>
- 학습 단계에 따른 수익률
![Episode Profit](https://user-images.githubusercontent.com/69662531/97879326-34383a00-1d63-11eb-8e82-c766a8d59baa.png)

- 마지막 에피소드 행동 비율
![action_ratio](https://user-images.githubusercontent.com/69662531/97880985-2d122b80-1d65-11eb-85e7-de43d4c08c57.png)


### Step.2

###### <시각화>
- 학습 단계에 따른 수익률
![Episode Profit2](https://user-images.githubusercontent.com/69662531/97988941-221cd100-1e21-11eb-982a-36d8da2b919e.png)

- 마지막 에피소드 행동 비율
![action_ratio2](https://user-images.githubusercontent.com/69662531/97988945-234dfe00-1e21-11eb-9e9b-974162b275bc.png)

