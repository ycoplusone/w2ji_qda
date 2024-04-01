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
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import SimpleImputer , IterativeImputer
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import klib

# 1. 데이터 로딩
df = pd.read_csv('D:\\python_workspace\\w2ji_qda\\kaggle\\guide\\data\\titanic\\train.csv')

'''
1. 데이터 전처리 과정에서 결측치 처리.
    - 데이터의 결측은 모델 학습과정에서 문제르르 일으킬 수 있다.
    - 이를 해결하기 위해 여러방법으로 결측치 처리한다.
    - 결측치 처리 방법으로 크게 제거(Deletion)와 대치(Imputation)이 있다.
    ※ 결측치를 확인하는 과정에서는 데이터의 도메인 지식이 필요하다.
    ※ 결측치를 삭제하는 방법으로 처리하는것은 많은 리스크가 따른다.

2. 대치(Imputation)
- 평균을  대치 => 평균은 모든 관측치의 값을 모두반영하므로 이상치의 영향을 많이 받기 때문에 주의가 필요
- 중앙값 대치  => 중앙값은 모든 관측치의 값을 모두 반영하지 않으므로 이상치의 영향을 덜 받는다.
- 최반값 대치  => 최반값을 이용한 이방식은 빈도수를 사용하기 때문에 범주형 변수에 사용하는것이 좋다.
- MICE로 대치  ( Multiveriate Imputation by Chained Equations ) 다중대치법
     => Round robin 방식을 반복하여 결측 값을 회귀하는 방식
     => 결측값을 회귀하는 방식으로 처리하기 때문에 이 방식은 수치형 변수에 자주 사용된다.
     => 범주형 변수에도 사용이 가능하지만 조금더 복잡하고 먼저 인코딩 해야 한다.

- fillna()를 이용한 대치
    => 특정값으로 대치
    => 특정열로의 값으로 대치
    => 결측치 바로 이전의 값으로 대치
    => 결측치 바로 이후 값으로 대치     
'''

'''
# 예제
def func_imputer(df , col , str ):
    # 대치 함수  
    #df : DataFrame
    #col : 컬럼
    #str : 'mean', 'median', 'most_frequent', 'constant' 만 가능 , 평균 ,중앙 , 최빈 , 정해진값
    
    # SimpleImputer의 인스턴스 생성
    imputer_mean = SimpleImputer(strategy= str)
    # 열을 2d 배열로 재구성 해야 한다.
    __df = df[col].values.reshape(-1,1)     
    return  np.round( imputer_mean.fit_transform( __df ) ,0)

mean =  func_imputer( df , 'Age' ,'mean' ) # 평균으로 대치
median = func_imputer( df , 'Age' ,'median' ) #중앙값으로 대치
most_frequent = func_imputer( df , 'Age' ,'most_frequent' ) # 최빈값 으로 대치

print('원본 : ',df.Age[888])
print('평균 : ',mean[888])
print('중앙 : ',median[888])
print('최빈 : ',most_frequent[888])

def func_misc_imputer( df , col , str ):    
    # MICE로 대치  ( Multiveriate Imputation by Chained Equations ) 다중대치법
    # df : DataFrame
    # col : 컬럼
    # str : 'mean', 'median', 'most_frequent', 'constant' 만 가능 , 평균 ,중앙 , 최빈 , 정해진값    
    
    __df = df[col].values.reshape(-1,1)     
    imputer_mice = IterativeImputer( initial_strategy= str)
    numeric_data = imputer_mice.fit_transform( __df )
    return numeric_data

print( 'mice : ',func_misc_imputer(df , 'Age' , 'mean')[888]  )

# fillna 로 대치
print( df.Age.fillna( 99 )[886:890] ) # 특정값으로 대치
print( df.Age.fillna( df.Fare )[886:890] ) # 특정열의 값으로 대치
print( df.Age.fillna( method = 'ffill' )[886:890] ) # 결측치 이전값으로 대치
print( df.Age.fillna( method = 'bfill' )[886:890] ) # 결측치 이후값으로 대치
'''





'''---------------------------------------------------------------------------
1-1. MCAR(Missing Completely At Random, 완전 무작위 결측)
    - 결측치가 발생한 변수의 값에 상관없이 전체에 걸쳐 무작위로 발생한 경우
    - 통계적으로 결측치의 영향이 없으므로 제거 가능
    ※ MCAR의 경우 일밙거으로 해당 데이터 포인트를 삭제하거나 평균/중앙/최빈 등으로 대치(imputation)을 사용한다.

1-2. MAR(Missing At Random, 무작위 결측)
    - 결측치가 발생한 변수의 값이 다른 변수와 상관관계가 있어 추정이 가능한경우
    - 통계적으로 결측치의 영향이 다소 있으나 편향이 없으므로 대체 가능
    ※ 회귀분석, 기대값 최대화 알고리즘(Expectation-Maximization algorithm), 다중대입(Multiple-Imputation) 등 접근법을 사용하여 결측치를 처리한다. 

1-3. MNAR(Missing Not At Random, 비무작위 결측)
    - 결측치가 발생한 변수의 값과 고나계가 있고 그 이유가 있는 경우
    - 통계적으로 결측치의 영향이 크므로 결측치의 원인에 대한 조사 후 대응 필요
    ※ 해결하는 정확한 방법이 존재하진 않음.
'''

'''
2. 결측치 탐색
print('info', df.info() )
print('isnull', df.isnull() )
print('notnull', df.notnull() )
print('sum0', df.isnull().sum(axis=0) ) # axix = 0 열기준 , 1 행기준
print( df.describe() ) # df의 수치형 항목 전체 통계 자료.
'''
'''
# 평균 , 표준편차 , 왜도 , 첨 그래프.
# 왜도(skew) => -0.5 ~ 0.5 대칭적이다. -1~-0.5 , 0.5 ~1 적당히 치우쳐져있다 , -1이하 , 1 이상 상당히 치우쳐있다.
# 첨도(kurtosis) => 3을 기준으로 3보다 크면 outlier 값이 많다. 3보다 작다면 outlier가 부족하다는 의미.
klib.dist_plot( df.Age ) # 정규분포를 고려 했을때 0~20세의 데이터에 일부 누락이 있는 것으로 추정된다.
plt.show()
'''

'''
3. 결측치 처리
3-1. 제거(deletion)
    - MCAR(완전무작위 결측)일때 사용가능.
    - 데이터의 손실이 발생 -> 자유도 감소 -> 통계적 검정력 저하
    - 표본의 수가 충분하고 결측값이 10~15% 이내일때에는 결측값을 제거한 후 분석하여도 결과에 크게 영향이 주지 않는다.
3-2. 대치(imputation)
    - 표본 평균과 같은 대표값으로 대체할 경우 -> 대표값 데이터가 많아짐 -> 잔차 변동이 줄어듬 -> 잘못된 통계적 결론 유도
    - 모수 추정시 편향 발생    
'''

'''
4. 결측치 제거(deletion)
4-1. Listwise deletion
    - 결측치가 존재하는 행자체를 삭제하는 방식.
    - MCAR일때문 가능
    - 데이터 표본의 숫자가 적은 경우 표본의 축소로 인한 검정력 감소.
4-2. Pairwise deletion
    - 분석에 사용하는 속성의 결측치가 포함된 행만 제거하는 방식
    - MCAR일 때만 가능
#예제
#Listwise deletion
df_listwise = df.dropna() # na값이 존재하는 행 전체 제거
print(df.info())
print(df_listwise.info()) #데이터의 약 80%가 제거 되었다. 전술했듯이 제거되는 데이터가 전체의 10~15% 일때만 사용한다.

#Pairwise deletion
df_pairwise = df.dropna( subset=['Age','Embarked'] ) #나이와 탑승항 컬럼만 제저한다.
print( df_pairwise.info() ) #데이터의 약20%가 제거 되었다. 전술했듯이 제거되는 데이터는 전체의 10~15%일때만 사용.    
'''

'''
5. 결츠치 대치(Imputation)
5-1. Single Imputation(단순대체법)
    - 결측치의 대체값으로 하나의 값을 선정하는것.
    - mean,correlation, 회귀계수와 같은 파라미터 추정 시 편향(bias) 발생가능성 높음.
    - 이러한 추정 편향으로 인해 아예 결측값을 제거하는것보다 통계적 특성이 나빠질수 있음.

'''















'''
타이타닉 자료의 결측치 처리.
결측치 항목 Age(수치형) , Cabin(범주형) , Embarked(범주형)
Pclass , Sex , Survived 의 각각의 평균 ,  중앙값 , 최빈값 을 측정하여 대치한다.
'''
# 수치형의 경우 대치 방식
#_tmp =  df.groupby(['Pclass','Sex','Survived'])['Age'].agg(['mean','median','std','max','min']) 
#print(_tmp) # 평균과 중앙값 그리고 표전편차를 확인후 특이사항을 확인후 대치할 값의 방식을 정한다. 평균값으로 대치 하기로 한다.

# 범주형의 경우 대치 방식










# 2. 누락된값 처리 - null , NaN , 공백 같은 값을 확인후 처리한다.
#print( df.info() ) # null 값 확인 Non-null count 확인.
# => age와 Embarkedrk Nan 데이터가 일부 확인 되었다.
# [결측치 관련 질문](https://www.kaggle.com/competitions/titanic/discussion/25408)

#print( df[ df.Embarked.isna() ] ) # Embarked isna 인값 추출 2건의 데이터중 동승자가 전혀 없다 추정할수 없다.
#print( df[ df.Age.isna() ] ) # Age iana 추출




