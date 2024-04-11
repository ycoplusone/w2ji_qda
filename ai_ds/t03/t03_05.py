import numpy as np
import scipy as sp
import pandas as pd
import matplotlib as mpl
import seaborn as sns
import sqlite3
'''
3.5 Binning & Creating Dummy variables
- Binning(구간화)
    수치형 컬럼의 자료값을 두개 이상의 구간으로 나누는 방법 , 이 경우 각 구간에 속한 자료값은 범주형 속성을 가짐.

- Dummy Vriables(가변수)
    범주형 값을 갖는 컬럼을 여러개의 이진형 컬럼으로 변환할때.

# 예제 - Binngin(구간화)
df = pd.DataFrame({'Year':[2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020]})
df['binning'] = pd.cut(df.Year, 
       bins=[0, 2010, 2015, 2020, 2022], 
       right=True, 
       labels=['2004~2010', '2011~2015', '2016~2020', '2021~2022'])
print(df)    

# dummy variables 예제
print( pd.get_dummies(df['binning']) )    
'''



