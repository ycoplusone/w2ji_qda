import numpy as np
import scipy as sp
import pandas as pd
import matplotlib as mpl
import seaborn as sns
import sqlite3

df_sat = pd.read_csv( 'D:\\python_workspace\\w2ji_qda\\ai_ds\\data\\설문조사.csv' )

''' 3.2 데이터 요약 (Aggregation)'''
''' 
3.2.1 summary & aggregation
- 컬럼의 속성에 따른 요약 방법
    수치형(연속형)컬럼 : 평균,합,최대값,최소값, 분산, 표준편차 등
    명목형(범주형)컬럼 : 빈도
- 기술통계 및 요약함수
    describe()          / 컬럼별 기초통계값 출력
    crosstab()          / 범주형자료의 빈도/교차표
    value_counts()      / 서로 다른 값 들에 대하여 자료의 갯수
    max()               / 최대값
    min()               / 최소값
    mean()              / 평균
    median()            / 중앙값
    mode()              / 최빈값
    var()               / 분산
    std()               / 표준편차
    corr()              / 상관계수
    sem()               / 평균에 대한 표준오차
    skew()              / 왜도
    kurt()              / 첨도
    agg(['min','max','sum'])    / 여래개의 통계량
#예제
print( df_sat.describe() )# describe
# 예제 : 단과대학(소속)별 학교생할만족도 점수의 평균, 표준편차 계산
x = df_sat.groupby('소속')['학교생활만족도'].agg(['mean','std'])
print(x)    
'''

'''
3.2.2 apply
- 각 행 및 열별 동일한 연산을 수행하기 위한 메서드
    df.apply(func , axis=0,)
        - func : aggregation function
        - axis : 0 for row-wise , 1 for column-wise        

# 데이터프레임의 행별 평균또는 열별 평균을 apply()를 이용하여 구하는 코드
df = pd.DataFrame({'X': [1,3,5,7],  'Y': [2,3,4,5]})
print('1', df.apply( np.mean , axis=0 ) ) #행별 평균
print('2', df.apply( np.mean , axis=1 ) ) #열별 평균
'''

'''
3.2.3 map, applymap
- apply와 유사하지만 map은 series , applymap은 데이터프레임의 컬럼별 동일한 연산을 수행
    Series.map(func)
    DataFrame.mapapply(func)
- 아래는 map, applymap의 사용 예시
df = pd.DataFrame({'X': [1,3,5,7],  'Y': [2,3,4,5]})
print( df.X.map(lambda x: x%2 == 0), df.applymap(lambda x: x%2 == 0) )    
'''





