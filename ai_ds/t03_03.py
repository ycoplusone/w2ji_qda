import numpy as np
import scipy as sp
import pandas as pd
import matplotlib as mpl
import seaborn as sns
import sqlite3
'''3.3 재구조화(reshaping)'''
'''
3.3.1 pivot : Spread rows into columns
- Long format 의 DataFrame을 wide format으로 변환
- bar 컬럼의 각 행의 값(a,b,c) 을 컬럼으로 하여 values로 지정된 컬럼의 값을 배치
    df.pivot(index='foo'  , columns='bar',values='baz')
    pandas.pivot_table( df , indoex='foo' , columns='bar' , values='baz' )
# 예제
df = pd.DataFrame({'sex':['m','f','m','f','f']
                   , 'age':[20,30,40,50,60]
                   , 'income':[100,200,300,400,500]
                   })
print(df)
print( df.pivot(index='sex' , columns='age',values='income') )
print( pd.pivot_table(df , index='sex',columns='age',values='income') )    
'''

'''
3.3.2 Melt
- wide format의 dAtaFrame을 long format으로 변환
# 예제 - income과 cost를 구분하는 컬럼을 생성하고 해당 값을 새로운 컬럼에 배치하는예제.
df = pd.DataFrame({"Age": [20, 30, 25, 20, 30],
                   "Sex": pd.Categorical(['m', 'm', 'm', 'f', 'f'], ["m", "f"]),
                   "income": [180, 200, 300, 180, 120],
                   "cost": [100, 210, 200, 200, 150]})
print( df )

a = df.melt( id_vars=['Sex','Age'] 
        , value_vars=['cost','income']
        , var_name='항목' 
        , value_name='금액'
        )
print( a )
'''

