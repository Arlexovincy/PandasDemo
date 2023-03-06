import pandas as pd

dataUrl = 'https://www.gairuo.com/file/data/dataset/team.xlsx'
df = pd.read_excel(dataUrl) 
print('原始数据:\n',df)

data1 = df.groupby('team').sum() # 按team分组对应列并相加
print('按team分组对应列并相加:\n',data1)

#对不同列使用不同的计算方法
data2 = df.groupby('team').agg({
    'Q1': sum,
    'Q2': 'count',
    'Q3': 'mean',
    'Q4': max
})
print('对不同列使用不同的计算方法:\n',data2)