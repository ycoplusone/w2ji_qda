import numpy as np
import scipy as sp
import pandas as pd
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import SimpleImputer , IterativeImputer
from sklearn.linear_model import LinearRegression

import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import klib


df = pd.read_csv('D:\\python_workspace\\w2ji_qda\\kaggle\\guide\\data\\titanic\\train.csv')
df_imputed1 = pd.DataFrame.copy(df)
df_imputed2 = pd.DataFrame.copy(df)


df['Sex'].replace({'male':0,'female':1},inplace=True)   #남자 0 , 여자 1
#df['Embarked'].replace({np.nan:0,'S':1,'C':2,'Q':3},inplace=True) #nan값은 이후 다시 대치처리 한다.
Embarked_a =  df['Embarked'].unique()
Embarked_b = list( range(0,len(Embarked_a),1) )
df['Embarked'].replace( to_replace=Embarked_a , value=Embarked_b , inplace=True )

#a = df['Cabin'].unique()
#b = list( range(0,len(a),1) )
#df['Cabin'].replace( to_replace=a , value=b , inplace=True )


#sns.heatmap(data = df.corr(), annot=True, fmt = '.2f', linewidths=.5, cmap='Blues')
#plt.show()

idx = df.Age.isnull() == True
train_x = df[['Pclass']][~idx]
train_y = df[['Age']][~idx]
test_x  = df[['Pclass']][idx]

from sklearn.linear_model import LinearRegression
# 선형회귀모형 인스탄스 생성 후 학습
lm1 = LinearRegression().fit(train_x, train_y)

pre = lm1.predict(test_x)
print( pre[0])

pre = pre + 5*np.random.rand(len(pre),1)

print(pre[0])


df_imputed1.loc[idx,'Age'] = np.round( lm1.predict(test_x) , 0) # 회귀 대치
df_imputed2.loc[idx,'Age'] = np.round( lm1.predict(test_x) + 5*np.random.rand(len(test_x),1) ,0) #확률적 회귀 대치


print('회귀 대치',df_imputed1.Age[888])
print('확률 회귀 대치',df_imputed2.Age[888])

#print(df_imputed1[['Pclass','Age']][idx].value_counts())
#print(df_imputed2[['Pclass','Age']][idx].value_counts())


'''    
a=  df[ (df['Pclass']==3) & (df['SibSp']==8)  ]
print(a)

_a = lm1.predict(test_x)
_b = np.random.rand(891,1)
for i in range(0,891):
    print( _a[i] , _b[i] , _a[i] + _b[i])
'''