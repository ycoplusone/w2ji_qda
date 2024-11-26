import pandas as pd
import seaborn as sns

data = sns.load_dataset(name='flights')
print(data.info())
print('-'*50)
print(data.head())
print('-'*50)
print( data.loc[2:4] )
print( data.iloc[2:4] )
print('-'*50)
print( data.loc[:,['year','month']] )
print('조건','-'*50)
print( data.loc[data['year'] ==1949 ] )
print( data.loc[ (data['year'] ==1949) & (data['month']=='Dec') , ['year','month','passengers']] )
print('데이터 정렬','-'*50)
print( data.loc[data['year'] ==1949 ].sort_values(by='passengers',ascending=False) )
print('집계함수','-'*50)
print( data['year'].value_counts() )
print( pd.crosstab( data['year'] , data['month'] ) )
print( pd.pivot_table( data=data , index='year',columns='month' , values='passengers' ) )
print( data.groupby( 'year' )['passengers'].mean() )
print('데이터 연결','-'*50)
a = data.loc[:,['year','month','passengers']]
b = data.loc[:,['passengers']].sort_values(by='passengers',ascending=False).reset_index(drop=True)
print( pd.concat( [a,b],axis=1 ) )
print('merge','-'*50)
a = data.loc[:,:].sort_values(by='passengers',ascending=True).reset_index(drop=True)
b = data.loc[:,:].sort_values(by='passengers',ascending=False).reset_index(drop=True)
print( pd.merge(left=a , right=b , how='inner' , on=['year','month']  ) )
#print('melt','-'*50)


