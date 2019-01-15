import pandas as pd
from pandas import Series,DataFrame

df1 = pd.read_csv('20190114.csv') #含id
df2 = pd.read_csv('20181231.csv')


df1['appC'] = Series([str(x) for x in Series['appCode']])
df1['addR'] = Series([str(x) for x in Series['address']])

appC_df1 = df1.set_index('appC')
addR_df1 = df1.set_index('addR')

result = pd.concat([addR_df1,appC_df1])
