import numpy as np
import scipy as sp
import pandas as pd
import matplotlib as mpl
import seaborn as sns
import sqlite3
'''
3.6 예제 데이터 및 실습문제
3.6.1 시도이름을 깆누으로 두데이터를 병합하고 여자인구비(%) 와 외국인비율(%)을 계산하여 컬럼을 추가. ㅡ외국인비가 가장콘순으로 정렬

#예제
df1 = pd.read_csv('D:\\python_workspace\\w2ji_qda\\ai_ds\\data\\시도별_인구.csv')
df2 = pd.read_csv('D:\\python_workspace\\w2ji_qda\\ai_ds\\data\\시도별_외국인인구.csv')


# 병합
df3 = df1.merge( df2 , left_on='시도명',right_on='시도' )

# 여자인구비(%) 산출
df3['여성인구비'] = df3['여자'] / df3['총인구'] * 100

# 외국인비율(%) 산출
df3['외국인비'] = df3['외국인'] / df3['총인구'] * 100

# 정렬
df3.sort_values('외국인' ,ascending=False, inplace=True)

'''

'''
3.6.2 Most Popular Programming Languages
- 데이터 설명
    데이터는 2014년 부터 2022년 까지 월별로 프로그래밍언어의 인기도를 조사한것임
    인기도는 100% 만점 기준으로 변환되어 있음
- 다운로드
    원데이터는 kaggle에서 다운로드 https://www.kaggle.com/muhammadkhalid/most-popular-programming-languages-since-2004/version/6

# 프로그램언어별 전체 조사 기간 동안 평균 스코어를 구하고, 평균 스코어가 높은 순으로 나타내리.    
df = pd.read_csv('D:\\python_workspace\\w2ji_qda\\ai_ds\\data\\Most_Popular_Programming_Languages.csv')

# 재구조화
df1 = df.melt( id_vars='Date' , var_name='Lan' , value_name='Score' )

# 평균 산출
df2 = df1.groupby(['Lan']).agg(['mean'])

# 순위 산출
df2['rank'] = df2['Score'].rank(ascending=False)

# 정렬
df2.sort_values('rank' , ascending=True , inplace=True)
print(df2)
'''






