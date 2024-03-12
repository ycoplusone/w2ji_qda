import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# 1. 데이터 로드
titanic_df = sns.load_dataset('titanic')

# 2. 데이터 탐색
# EDA 탐색적 데이터 분석 수행하기
# .info() 함수로 데이터 컬럼별 타입(자료형), 값이 있는 행(Non-Null)의 갯수 등을 알 수 있습니다.
print( titanic_df.info() )

print( titanic_df.head() )

# 3. 범주형 컬럼과 수치형 컬럼 분리.
category_cols  = ['sex','embarked','class','who','adult_male','deck','embark_town','alive','alone']
numerical_cols = ['age','sibsp','parch','fare']


print('\n','4. 데이터의 통계량으로 살펴보기','\n')
print(titanic_df.describe())

print('\n','5. value_counts()를 통해 각 컬럼별로 몇 개의 row가 있는지 셀 수 있습니다','\n')
for i in category_cols:
    print( i , '카운터 ::')
    print( titanic_df.loc[:,i].value_counts() ,'\n')