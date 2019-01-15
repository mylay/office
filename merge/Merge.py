import pandas as pd
from pandas import Series,DataFrame

left = pd.read_csv('20190114.csv') #含id
right = pd.read_csv('20181231.csv')

# result = pd.merge(left, right, how="right", on=['appCode(CN)', 'address'])
#当左右连接字段不相同时，使用left_on,right_on
#on关联键
result = pd.merge(left, right, how="right", on=['appCode', 'address'])
# result = pd.merge(left, right, how='right')
wirter = pd.ExcelWriter('pandas_simple.xlsx')
result.to_excel(wirter, sheet_name='合并表', index=False)
wirter.save()

