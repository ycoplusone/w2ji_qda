'''
3.1 데이터 랭글링(data wrangling)
- 데이터 랭글링 복잡하고 지저분한 데이터를 쉽게 접근하여 분석할수 있도록 데이터 정리와 통합하는 프로세스
참고 : https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf
'''
# 3.1.1 라이브러리 로딩
import numpy as np
import scipy as sp
import pandas as pd
import matplotlib as mpl
import seaborn as sns
import sqlite3

# 3.1.2 외부데이터 읽기
df_csv = pd.read_csv('D:\\python_workspace\\w2ji_qda\\ai_ds\\data\\test.csv')
df_exc = pd.read_excel( 'D:\\python_workspace\\w2ji_qda\\ai_ds\\data\\006220_제주은행.xlsx' )
df_xml = pd.read_xml( 'D:\\python_workspace\\w2ji_qda\\ai_ds\\data\\2016년_사망교통사고.xml' , encoding='utf-8' )

# sqlite3 생성
conn = sqlite3.connect('D:\\python_workspace\\w2ji_qda\\ai_ds\\data\\ai_ds.db')
# df를 sqlite db 테이블에 저장
df_exc.to_sql('jeju_bank',conn , if_exists='replace' , index=False) 
#db 테이블 읽어오기
jeju_bank = pd.read_sql( 'select * from jeju_bank',conn,index_col=None )
conn.close()

''' 
3.1.3 dataframe data type
object / string / 숫자 문자 혼합
int64  / int    / 숫자
float64/ float  / 숫자
datetime64/     / 날짜 시간 형식
category  /     / 범주형 데이터 형식
bool      / bool / boolian 형식
'''

'''
3.1.4 dataframe attributes & methods
dtypes      / 컬럼의 데이터 타입
columns     / 컬럼명
axes        / 레코드 라벨및 컬럼명
ndim        / 컬럼의 개수(차원)
size        / 레코드수 * 컬럼수
shape       / 행 및 컬럼의 개수, 튜플형식
T           / 행,컬럼 치환 transpose
print('dtypes : ', jeju_bank.dtypes )
print('columns  : ', jeju_bank.columns  )
print('axes  : ', jeju_bank.axes  )
print('ndim  : ', jeju_bank.ndim  )
print('size  : ', jeju_bank.size  )
print('shape  : ', jeju_bank.shape  )
print('T  : ', jeju_bank.T  )
'''

'''
3.1.5 dataframe methods

'''


