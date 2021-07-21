import pandas as pd

df1 = pd.read_csv('./data/concat_1.csv')
df2 = pd.read_csv('./data/concat_2.csv')
df3 = pd.read_csv('./data/concat_3.csv')

df3.columns = 'E', 'F', 'G', 'H'
df3.index = 4, 5, 6, 7
# axis = 1 좌우로 붙임
# axis = 0 (default) 눕혀서 붙임
# total = pd.concat((df1, df2, df3), ignore_index=True, axis=1)

total = pd.concat((df1, df2, df3))

print(total)
