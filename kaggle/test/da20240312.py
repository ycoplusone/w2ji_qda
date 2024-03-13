import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. 데이터 로드
titanic_df = sns.load_dataset('titanic')

df = titanic_df.drop(columns=['survived']) #독립변수를 제외한 종속변수들만 처리.



# 2. 데이터 탐색
# 해당 데이터의 범주형 데이터와 수치형 데이터를 확인한다.
print('\n','데이터의 형태 확인','\n')
a = df.info()
   
str_cols = []
num_cols = []

for i in df.columns:
    if len(df[i].unique()) > 9:
        num_cols.append(i)
    else:
        str_cols.append(i)

print( '카테 : ',str_cols )
print( '숫치 : ',num_cols )
