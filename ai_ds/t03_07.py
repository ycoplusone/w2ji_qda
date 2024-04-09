import numpy as np
import scipy as sp
import pandas as pd
import matplotlib as mpl
import seaborn as sns
import sqlite3

'''
3.7 시군구별 음식점 데이터
- 데이터 
    * 일반음식점(CSV파일)   : fulldata_07_24_04_P_일반음식점.csv
    * 자치단체코드(엑셀파일) : 개방_자치단체코드목록.xlsx
- 문제
    * 일반음식점 데이터에서 컬럼 개방자치단체코드와 자치단체코드 데이터의 시군구(자치단체)코드를 연결하여 음식점 소재지인 시군구 컬럼을 추가
    * 전국 지자체(시군구)별 음식점의 수를 구하라
    * 전국 지자체(시군구)별 음식점의 수를 폐업또는 영업중으로 구분하여 구하라
    * 위 데이터에서 경복에 소재한 음식점 중에서 현재 시군구별로 영업중인 음식점의 수를 구하라
    * 전체 음식점 중 폐업비율을 구하고 크기순으로 나타내라
    * 시군구별 거주인구 수 데이터를 구해서 인구수 대비 영업중인 음식점의 비율을 시군구별로 구하고 인구대비음식점의 수가 가장 큰 순으로 나타내어라.
    * 음식점 데이터에서 ’업태구분명’은 음식점의 종류이다. 분석에서 관심 업태는 [‘한식’, ‘치킨’, ‘분식’, ‘양식’, ‘식육(숯불구이)’, ‘중국식’, ‘일식’, ‘까페’, ‘패스트푸드’] 이고 이를 위해서 기존 저장된 업태를 아래와 같이 변경하여라
    * 지역별 관심 업태에 따른 음식점의 수를 구하라.
'''

# 1. 데이터 로드
#df1 = pd.read_csv('http://bigdata.dongguk.ac.kr/lectures/AI/data/fulldata_07_24_04_P_%EC%9D%BC%EB%B0%98%EC%9D%8C%EC%8B%9D%EC%A0%90.csv',encoding='CP949')
#df2 = pd.read_excel('D:\\python_workspace\\w2ji_qda\\ai_ds\\data\\개방_자치단체코드목록.xlsx')
#df2.to_parquet('D:\\abc.parquet')
df = pd.read_csv('http://bigdata.dongguk.ac.kr/lectures/AI/data/fulldata_07_24_04_P_%EC%9D%BC%EB%B0%98%EC%9D%8C%EC%8B%9D%EC%A0%90.csv',encoding='CP949')
df.to_parquet('D:\\food.parquet')


