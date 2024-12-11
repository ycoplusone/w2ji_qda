from io import StringIO
import pandas as pd
import missingno as msno
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from datetime import datetime

csv_data = StringIO("""
x1,x2,x3,x4,x5
1,0.1,"1",2019-01-01,A
2,,,2019-01-02,B
3,,"3",2019-01-03,C
,0.4,"4",2019-01-04,A
5,0.5,"5",2019-01-05,B
,,,2019-01-06,C
7,0.7,"7",,A
8,0.8,"8",2019-01-08,B
9,0.9,,2019-01-09,C
""")

df = pd.read_csv(csv_data, dtype={"x1": pd.Int64Dtype()}, parse_dates=[3])
print(df)
print(df.isnull())
print(df.isnull().sum())
print('-'*20)
#msno.matrix(df)
#plt.show()
#msno.bar(df)
#plt.show()

#t = sns.load_dataset('titanic')
#print( t.tail() )
#msno.matrix(t)
#plt.show()

'''
결측된 데이터를 처리하는 방법은 두가지다.
- 결측된 데이터가 너무 많은 경우 해당 데이터 열 전체를 삭제할수 있다.
- 결측된 데이터가 일부인 경우 가장 그럴듯한 값으로 대체 할수 있다. 이를 결측 데이터 대체(imputation)
'''

# thresh 인수를 사용하면 특정 갯수 이상의 비결측 데이터가 있는 행또는 열을 남긴다.
print( df.dropna(thresh=7 , axis=1) ) # 세로 열 비결측 7개 이상 출력
print( df.dropna(thresh=3 , axis=0) ) # 가로 열 비결측 3개 이상 출력
print('*'*50)

''' 타이타닉 데이터에서 deck 데이터는 결측된 데이터가 너무 많기 때문에 이 방법으로 데이터를 삭제한다.
'''
# 데이터가 절반 이상이 없는 열을 삭제
t = sns.load_dataset('titanic')
t2 = t.dropna(thresh= int( len(t) * 0.5 ) , axis=1 ) # deck 컬럼은 제거됨.

#msno.matrix(t)
#msno.matrix(t2)
#plt.show()

'''
결측 데이터를 대체할 때는 해당 열의 비결측 데이터의 평균값 혹은 중앙값 등의 대체값으로 사용하여 결측된 데이터를 채운다.
scikit-learn 패키지의 simpleimputer 클래스를 사용하면 쉽게 결측 데이터를 대체할수 있다.
1. SimpleImputer 클래스 객체를 생성한다. 이때 strategy 인수를 "mean" 평균값 , "median" 중앙값 , "most_frequent" 최빈값 으로 대체한다.
2. fit_transform 메서드를 사용하여 대체값이 채워진 데이터프레이을 생성한다.

strategy 인수를 선택하는 방법은 다음과 같다.
1. 데이터가 실수 연속값인 경우에는 평균 또는 중앙값 사용. 값의 분포가 대칭적이면 평균이 좋고 값의 분포가 심하게 비대칭 인경우 중앙값이 적당하다.
2. 데이터가 범주 값이거나 정수 값인 경우에는 최값값을 사용.
'''

from sklearn.impute import SimpleImputer
# 평균으로 Imputer 선언
imputer_mean = SimpleImputer(strategy='most_frequent')
df['x4'] = df['x4'].dt.strftime('%Y%m%d') # datatime64 => object 으로 변경
print('*'*50)
print( df )
df[['x1', 'x2', 'x3','x4']] = imputer_mean.fit_transform( df[['x1', 'x2', 'x3','x4']] )
print('*'*50)
print( df )

''' 타이타닉 데이터에서 embark_town 데이터부터 대체해보자.
이 값은 범주값이므로 strategy='most_frequent'로 하여 최빈값을 대체값으로 사용한다.
대체하기 전의 embark_town 데이터 분포를 살펴보면 southhamton 값이 가장 많다.
대체 후에는 이 값으로 결측 데이터가 대체될것이다.

sns.countplot( t.embark_town )
plt.title('embark_town 분포')
plt.show()
'''
#msno.matrix(t)
imputer_embark_town = SimpleImputer(strategy='most_frequent')
t[['embark_town']]  = imputer_embark_town.fit_transform( t[['embark_town']] )
t[['embarked']]     = imputer_embark_town.fit_transform( t[['embarked']] )
#msno.matrix(t)
#plt.show()

'''
age 데이터를 대체한다. 대체하기 전의 age 데이터 분포를 살펴보면 비대칭인 것을 볼수 있다.
sns.kdeplot(t[['age']])
plt.show()
따라서 strategy='median' 중앙값으로 대체한다.
'''
imputer_age = SimpleImputer(strategy='median')
t[['age']] = imputer_age.fit_transform(t[['age']])
#msno.matrix(t)
#plt.show()


