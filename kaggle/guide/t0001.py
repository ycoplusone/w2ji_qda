'''
분석목표 : 타이타닉 생존자 데이터로 생존여부를 예측하기에 앞서 feature engineering 을 수행한다.
알고리즘 : 
종속변수 : Survived(생존여부) 0 = No, 1 = Yes
평가지표 : 
데이터셋 : 보험과 고나련된 데이터입니다. 보험사에서 청구하는 병원 비용이 종속변수이며
    PassengerId     : 승객id
    Survived        : 생존여부 0 = No, 1 = Yes
    Pclass          : 좌석등급 1 = 1st, 2 = 2nd, 3 = 3rd
    Name            : 이름
    Sex             : 성별
    Age             : 나이
    SibSp           : 등승한 형제 자매 수
    Parch           : 등승한 부모 혹은 자녀 수
    Ticket          : 티켓 번호
    Fare            : 요금
    Cabin           : 객실번호
    Embarked        : 탑승 항구  C = Cherbourg, Q = Queenstown, S = Southampton    

'''
import numpy as np
import scipy as sp
import pandas as pd
from sklearn.impute import SimpleImputer
import matplotlib as mpl
import seaborn as sns

# 1. 데이터 로딩
df = pd.read_csv('D:\\python_workspace\\w2ji_qda\\kaggle\\guide\\data\\titanic\\train.csv')

'''
1. 데이터 전처리 과정에서 결측치 처리.
    - 데이터의 결측은 모델 학습과정에서 문제르르 일으킬 수 있다.
    - 이를 해결하기 위해 여러방법으로 결측치 처리한다.
    - 결측치 처리 방법으로 크게 제거(Deletion)와 대치(Imputation)이 있다.
'''

def func_imputer(df , col , str ):
    ''' 대치 함수  
    df : DataFrame
    col : 컬럼
    str : 'mean', 'median', 'most_frequent', 'constant' 만 가능
    '''
    # SimpleImputer의 인스턴스 생성
    imputer_mean = SimpleImputer(strategy= str)
    # 열을 2d 배열로 재구성 해야 한다.
    __df = df[col].values.reshape(-1,1)     
    return  np.round( imputer_mean.fit_transform( __df ) ,0)
'''
2. 대치(Imputation)
- 평균을  대치 => 평균은 모든 관측치의 값을 모두반영하므로 이상치의 영향을 많이 받기 때문에 주의가 필요
- 중앙값 대치  => 중앙값은 모든 관측치의 값을 모두 반영하지 않으므로 이상치의 영향을 덜 받는다.
- 최반값 대치  => 최반값을 이용한 이방식은 빈도수를 사용하기 때문에 범주형 변수에 사용하는것이 좋다.
- MICE로 대치  
     => Round robin 방식을 반복하여 결측 값을 회귀하는 방식
     => 결측값을 회귀하는 방식으로 처리하기 때문에 이 방식은 수치형 변수에 자주 사용된다.
     => 범주형 변수에도 사용이 가능하지만 조금더 복잡하고 먼저 인코딩 해야 한다.


'''
# 예제
mean =  func_imputer( df , 'Age' ,'mean' ) # 평균으로 대치
median = func_imputer( df , 'Age' ,'median' ) #중앙값으로 대치
most_frequent = func_imputer( df , 'Age' ,'most_frequent' ) # 최빈값 으로 대치

print(df.Age[888])
print(mean[888])
print(median[888])
print(most_frequent[888])











# 2. 누락된값 처리 - null , NaN , 공백 같은 값을 확인후 처리한다.
#print( df.info() ) # null 값 확인 Non-null count 확인.
# => age와 Embarkedrk Nan 데이터가 일부 확인 되었다.
# [결측치 관련 질문](https://www.kaggle.com/competitions/titanic/discussion/25408)

#print( df[ df.Embarked.isna() ] ) # Embarked isna 인값 추출 2건의 데이터중 동승자가 전혀 없다 추정할수 없다.
#print( df[ df.Age.isna() ] ) # Age iana 추출

