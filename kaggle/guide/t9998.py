import pandas as pd

# MultiIndex를 가진 DataFrame 생성
arrays = [['A', 'A', 'B', 'B'], [1, 2, 1, 2]]
index = pd.MultiIndex.from_arrays(arrays, names=('first', 'second'))
df = pd.DataFrame({'data': [1, 2, 3, 4]}, index=index)

# MultiIndex를 일반적인 DataFrame으로 변경
df_reset = df.reset_index()

#print("Original DataFrame:")
print(df.info())
#print("\nDataFrame after reset_index():")
print(df_reset.info())