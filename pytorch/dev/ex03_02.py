# 1. 보스턴 데이터셋의 특징 출력
from sklearn.datasets import load_boston

# 경고 무시
import warnings
warnings.filterwarnings('ignore')

dataset = load_boston() # 데이터셋을 불러옴
print(dataset.keys())   # 데이터셋의 키(요소들의 이름)를 출력


# 2.데이터의 구정요소 확인
import pandas as pd

from sklearn.datasets import load_boston

dataset = load_boston()
dataFrame = pd.DataFrame(dataset["data"]) # ❶ 데이터셋의 데이터 불러오기
dataFrame.columns = dataset["feature_names"] # ❷ 특징의 이름 불러오기
dataFrame["target"] = dataset["target"] # ❸ 데이터 프레임에 정답을 추가

print(dataFrame.head()) # ➍ 데이터프레임을 요약해서 출력



# 3. 선형회귀를 위한 MLP모델의 설계
import torch
import torch.nn as nn

from torch.optim.adam import Adam


# ❶ 모델 정의
'''
신경망 모델을 정의합니다.
nn.Linear 와 nn.ReLU 만 사용.
Linear()는 MLP모델을 의미하고 ReLU()는 활성화 함수의 일종이다.
nn.Linear(13, 100)에서 13은 입력 차원 , 100은 출력 차원.(13개를 입력받아 100개의 특징을 반환한다.)
층의 입력과 이전 층의 출력이 일치하지 않으면 에러가 발생하므로 주의하자.
'''
model = nn.Sequential(
   nn.Linear(13, 100),
   nn.ReLU(),
   nn.Linear(100, 1)
)

X = dataFrame.iloc[:, :13].values # ❷ 정답을 제외한 특징을 X에 입력
Y = dataFrame["target"].values    # 데이터프레임의 target의 값을 추출


batch_size = 100
learning_rate = 0.001

# ❸ 가중치를 수정하기 위한 최적화 정의
'''
Adam()은 가장 많이 쓰이는 최적화 기법입니다.
역전파된 오차를 이용해 가중치를 수정하는 기법.
대표적으로  Adam과 경사하강법이 있습니다.
Adam()은 최적화가 필요한 모델의 가중치들과 학습률을 입력으로 받습니다.
'''
optim = Adam(model.parameters(), lr=learning_rate)


# 에포크 반복
for epoch in range(200):

   # 배치 반복
   for i in range(len(X)//batch_size):
       start = i*batch_size      # ④ 배치 크기에 맞게 인덱스를 지정       
       end = start + batch_size


       # 파이토치 실수형 텐서로 변환
       x = torch.FloatTensor(X[start:end])
       y = torch.FloatTensor(Y[start:end])

       optim.zero_grad() # ❺ 가중치의 기울기를 0으로 초기화 # 이전 배치에서 계산된 기울기가 남아 있기 때문에 초기화한다.
       preds = model(x)  # ❻ 모델의 예측값 계산. 모델에 데이터를 입력한다.
       loss = nn.MSELoss()(preds, y) # ❼ MSE 손실 계산 실제값과 예측값의 차이를 제곱하고 모든 입력에 대한 평균을 내는 오차를 말한다.
       loss.backward() # ⑦ 에서 계산된 오차값을 역전파한다.
       optim.step() 

   if epoch % 20 == 0:
       print(f"epoch{epoch} loss:{loss.item()}")

# 모델 성능 평가
for i in range(0,len(X)):
    prediction = model(torch.FloatTensor(X[i, :13]))
    real = Y[i]
    cap = real - prediction
    print(f"{i} \t prediction:{prediction.item()} \t real:{real} \t cap : {cap}")

