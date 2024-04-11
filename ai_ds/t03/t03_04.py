import numpy as np
import scipy as sp
import pandas as pd
import matplotlib as mpl
import seaborn as sns
import sqlite3

'''3.4여러개의 DataFrame 결합'''

''' 
3.4.1 Concat & Append
- 데이터프레임을 행또는 열에 대하여 결합.
    pd.concat( objs , axis=0 , ignore_index=False ) #행으로 결합
    pd.concat( objs , axis=1 , ignore_index=False ) #열로 결합.
    DataFrame.append( df , ignore_index=False ) # 행으로 결합.
# 예제
df8 = pd.DataFrame({'name': ['Bob', 'Jake', 'Lisa', 'Sue'],'rank': [1, 2, 3, 4]})
df9 = pd.DataFrame({'name': ['Kim', 'Lee', 'Park', 'Jung'],'rank': [3, 1, 4, 2]})
print(  pd.concat([df8,df9]) )
print(  pd.concat([df8,df9] , ignore_index=True) )
print( df8.append(df9 , ignore_index=True) )
'''

'''
3.4.2 join & merge DataFrame
- 데이터프레임을 다른 데이터프레임과 열에 대하여 결합.
- join 방법 : how={"left", "right", "outer", "inner", "cross"}
    DF1.join(df2, on=column_name, how='left')   # left-join으로 결합
    DF1.merge(df2, how='inner', 
            on=column_name,
            left_on=None,
            right_on=None
            ) 

# 예제
df8 = pd.DataFrame({'name': ['Bob', 'Jake', 'Lisa', 'Sue'],'rank': [1, 2, 3, 4]})
df9 = pd.DataFrame({'name': ['Bob', 'Jake', 'Lisa', 'Sue'],'rank': [3, 1, 4, 2]})
print( pd.merge( df8 , df9 , on='name' ) )

df1 = pd.DataFrame({'employee': ['Bob', 'Jake', 'Lisa', 'Sue'],'group': ['Accounting', 'Engineering', 'Engineering', 'HR']})
df2 = pd.DataFrame({'employee': ['Lisa', 'Bob', 'Jake', 'Sue'],'hire_date': [2004, 2008, 2012, 2014]})
df3 = pd.DataFrame({'name': ['Bob', 'Jake', 'Lisa', 'Sue'],'salary': [70000, 80000, 120000, 90000]})

print( pd.merge(df1 , df3 , left_on='employee' , right_on='name') )

df6 = pd.DataFrame({'name': ['Peter', 'Paul', 'Mary'],'food': ['fish', 'beans', 'bread']}, columns=['name', 'food'])
df7 = pd.DataFrame({'name': ['Mary', 'Joseph'],'drink': ['wine', 'beer']}, columns=['name', 'drink'])

print( pd.merge(df6 , df7 , how='inner') )
print( pd.merge(df6 , df7 , how='outer') )
print( pd.merge(df6 , df7 , how='left') )
print( pd.merge(df6 , df7 , how='cross') )
'''
