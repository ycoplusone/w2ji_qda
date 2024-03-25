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
1. summary functions
    info()      / 데이터프레임 정보
    head()      / 처음 n개행 출력
    tail()      / 마지막  n개행 출력
    describe()  / 수치형 컬럼들의 기초통계값 출력
    max()       / 수치형 컬럼의 최대값
    min()       / 수치형 컬럼의 최소값
    mean()      / 수치형 컬럼의 평균
    median()    / 수치형 컬럼의 중앙
    mode()      / 수치형 컬럼의 최빈값
    var()       / 분산
    std()       / 표준편차
    sample()    / 임의의 n개 추출
    dropna()    / 결측치 제거
    sem()       / 평균에대한 표준오차
    skew()      / 왜도 
    kurt()      / 첨도
    agg( ['min','max'] )    / 여러개의 통계량을 한번재 산출
    print( jeju_bank.info() )
    print( jeju_bank.sem() )
    print( jeju_bank.agg(['max','mean','var']) )

2. Data type변경(casting)
    jeju_bank.astype('int32') 모든 컬럼 타입 변경
    jeju_bank.astype({'날짜':'int32'}) #지정 컬럼별 타입 변경
    
3. 범주형 컬럼 처리
    df_xml.daynight = pd.Categorical(df_xml.daynight, ['주간', '야간']) # 범주형 컬럼으로 변경
    df_xml.daynight = pd.Categorical(df_xml.daynight, ['주간', '야간']).rename_categories(['낮','밤']) # 카테고리 레이블 변경
'''


'''
3.1.6 DataFrame 에서 컬럼 및 레코드 추출
- 방법1 : 컬럼명을 대괄호에 리스트로 입력 df['sex']
- 방법2 : 컬럼명을 데이터프레임의 속성으로 간주 df.sex
- 방법3 : 
df[val]                     / 컬럼명val에 해당하는 컬럼 추출
df.loc[:,val]               / 컬럼명 val에 해당하는 컬럼 추출
df.loc[val]                 / 행이름에 해당하는 데이터 추출
df.loc[val1, val2]          / 행이름 val1, 컬럼명 val2 해당하는 데이터 추출
df.iloc[where]              / 행인덱스에 해당하는 행 추출
df.iloc[:,where]            / 열인덱스에 해당하는 행 추출
df.iloc[where_i,where_j]    / 행인덱스 & 열인덱스 에 해당하는 데이터 추출
# 예시
print( df_csv.head() ) # 5개행 출력
print( df_csv[10:20] ) # 10~20행 출력
print( df_csv.loc[10:20,['Pclass','Sex','Age']] ) # 10~20행의 특정 컬럼 출력
print( df_csv.iloc[10:20,[0,3,4,5]] ) # 10~20행의 특정 컬럼 출력
print( df_csv.iloc[0] ) # 첫번째 행 출력

print( df_csv.iloc[-1] ) #  마지막 행 출력
print( df_csv.iloc[:,0] ) # 첫번째 컬럼 출력
print( df_csv.iloc[:,-1] ) # 마지막 컬럼 출력
print( df_csv.iloc[0:7] ) # 1~7행 출력
print( df_csv.iloc[:,0:2] ) # 1~2 컬럼 출력
print( df_csv.iloc[ 1:3 , 0:2 ] ) # 1~3행 의 0~2컬럼 출력
'''

'''
3.1.7 dataframe : filtering & slicing
- Boolean 인덱시을 이용해서 필터링( > , >= , < , <= , == , != )
- 테스트 데이터를 ㅣ용해서 연봉 30000 이상을 필터링
degree  => 1: PhD , 0 : Masters
rank    => 1 : asst prof , 2 AssocProf , 3 Prof
sex     => 1 : female , 0 : male
year    => current rank
ysdeg   => 최고ㅗ 학위 취득 연도
salary  => dolars per year
# 예제
df_sal = pd.read_excel('D:\\python_workspace\\w2ji_qda\\ai_ds\\data\\salary.xlsx')
sal_1 = df_sal[ (df_sal['salary'] >= 30000) & (df_sal['sex'] == 1) ] # 30000 이상 여성 추출
'''

'''
3.1.8 Dataframe groupby method
- 데이터를 지정한 컬럼의 값으로 분리하여 그룹화
- 그룹화된 데이터프레임에 대한 후속 연산
#예제
df_sat = pd.read_csv( 'D:\\python_workspace\\w2ji_qda\\ai_ds\\data\\설문조사.csv' )
# 소속과 성별 그룹
group = df_sat.groupby(['소속','성별'])['학교생활만족도','지원동기'].agg(['mean','sum']) # groupby 기준 , 컬럼 , 집계방식
print(group)
'''

'''
3.1.9 dataframe : soring
1. 행열의 라벨에 대한 정렬
    dataframe.sort_index( axis , ascending , inplace=False )
2. 컬럼의 값으로 정렬
    dataframe.sort_values(by , ascending , inplace=False)
3. 예제
- 단과대학별 컬럼에 대한 평균 계산
- 단과대별 학교생활만족도 컬럼의 값에 대한 역순 정렬
df_sat = pd.read_csv( 'D:\\python_workspace\\w2ji_qda\\ai_ds\\data\\설문조사.csv' )
x = df_sat.groupby('소속').mean()
x.sort_values(by='학교생활만족도' , ascending=False , inplace=True)
print(x)
'''

'''
3.1.10 결측치의 처리
- 데이터에서 특정셀의 값이 없는 경우, 그 셀을 결측값이라고하고, 결측치가 포함된 데이터를 결측자료
- 결측자료는 (1)무응답 등으로 제공되는 정보가 없을때, (2) 자료의 손실 등으로 발생함.
- 이러한 결측치는 자료가 많은 경우에는 해당 레코드를 삭제또는 대체하여 분석함.
- Python에서 결측치는 Null 값(None) 또는 NaN(Not a number)를 의미하며 데이터 프레임에서는  NaN으로 표기.
dropna()                    / 결측치가있는 레코드 제거
dropna(how='all')           / 모든 컬럼값이 결측치인 경우에만 해당레코드 제거
dropna(axix=1,how='all')    / 모든 컬럼값이 결측치인 경우에만 해당 컬럼 제거
dropna(thresh=5)            / 5개보다 많은수의 결측치가 있으면 해당 레코드 제거
fillna(0)                   / 결측치를 0으로 대체
isnull()                    / 결측치가 하나라도 있으면 True값 반환
notnull()                   / 결측치가 하나도 엇으면 True반환
#예제
df = pd.DataFrame({'Sex':    ['m', 'm', 'm', None, 'f', 'f'],'Age':[20, 30, np.nan, 20, 30, 40],'income': [180, 200, 300, 180, None, 310]})
print(df)
print( df.dropna() )
print( df.fillna('f') )
'''

'''
3.1.11 컬럼추가
1. 방법
- df.assign( new_column_name= value)
- df.indsert(loc , new_column_name , value)
- df['new_column_name'] = value
# 예제
df = pd.DataFrame()
df = df.assign(Age=[20,30,40])
df.insert( 0 , 'Sex',['m','f','f'] )
df['amount'] = [180,200,250]
print(df)
'''

'''
3.1.12 컬럼의 데이터타입 변환
- 데이터프레임 컬럼 형 변환
    df.astype({'col1':dtypee,'col2':dtype})
    dtype : int , float , datetime , category
- 수치형 컬럼의 변환
    pd.to_numeric(dataframe , ['col1','col2'])
- 날짜시간 형으로 변황
    pd.to_datetime(dataframe , ['col1','col2'])
- 문자형으로 변환
    pd.to_string(dataframe,['col1','col2'])
- numpy array로 변환
    df.to_numpy()
- 범주형 컬럼 생성
    pd.Categorical(values , categories)
#예제
df = pd.DataFrame()
df = df.assign(Age = [10,20,30,40,50])
sex = pd.Categorical(['m','m','m','f','f'],['m','f'])
df['sex'] = sex
df.insert( 1 , 'amount',[100,200,300,400,500] )
print(df.dtypes)
print(df)    
'''










