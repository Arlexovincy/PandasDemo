import pandas as pd

dataUrl = 'https://www.gairuo.com/file/data/dataset/team.xlsx'
df = pd.read_excel(dataUrl) 
print('原始数据:\n',df)

#复杂查询
Q1Over80 = df[df['Q1'] > 80] #获取Q1大于80的数据
print('获取Q1大于80的数据:\n',Q1Over80)

not80Data = df[~(df['Q1'] == 80)] #获取Q1不等于80的数据
print('获取Q1不等于80的数据:\n',not80Data)

data1 = df.loc[df['Q1'] > 90, 'Q1':] #Q1大于90，显示Q1及以后的数据
print('Q1大于90,显示Q1及以后的数据:\n',data1)

data2 = df.loc[(df['Q1'] > 90) & (df['Q2'] < 90)] #Q1大于90，Q2小于90的数据
print('Q1大于90,Q2小于90的数据:\n',data2)

data3 = df.Q1[lambda s: max(s.index)] #获取Q1的index的最大值
print('获取Q1的index的最大值:\n',data3)

data4 = df.loc[lambda df: df.Q1 == 80, 'Q1':'Q3'] #获取Q1等于80，Q1到Q3的数据
print('获取Q1等于80,Q1到Q3的数据:\n',data4)

data5 = df[df.Q1.isin([80,90,70,60])] #Q1在数组里面的数据
print('Q1在数组里面的数据:\n',data5)

data6 = df[df.isin({'team':['C','D'],'Q1':[36,93]})] #组合数据查询
print('组合数据查询:\n',data6)

data7 = df.query('Q1 > Q2 > 90') #直接写类似SQL where语句
print('Q1大于Q2大于90的数据:\n',data7)

data8 = df.query('(Q1 < 50) & (Q2 > 40) & (Q3 > 90)') # (Q1 < 50) & (Q2 > 40) & (Q3 > 90)
print('(Q1 < 50) & (Q2 > 40) & (Q3 > 90):\n',data8)

data9 = df.query('team not in ("E","A","B")') #不是A、B、E的team的数据
print('不是A、B、E的team的数据',data9)

data10 = df.filter(items=['Q1','Q2']) #只要Q1和Q2两列的数据
print('只要Q1和Q2两列的数据:\n',data10)
data11 = df.filter(regex='Q', axis=1) # 列名包含Q的列 df.filter(regex='e$', axis=1) # 以e结尾的列 df.filter(regex='1$', axis=0) # 正则，索引名以1结尾
data12 = df.filter(like='2', axis=0) # 索引中有2的
data13 = df.filter(regex='^2', axis=0).filter(like='Q', axis=1) # 索引中以2开头、列名有Q的

#排序
data14 = df.sort_index(ascending=False) #索引降序
print('索引降序:\n',data14)

data15 = df.sort_values(by=['team'], ascending= True) #team降序
print('team降序:\n',data15)

# df.fillna(0) # 将空值全修改为0
# # {'backfill', 'bfill', 'pad', 'ffill', None}, 默认为None df.fillna(method='ffill') # 将空值都修改为其前一个值
# values = {'A': 0, 'B': 1, 'C': 2, 'D': 3} df.fillna(value=values) # 为各列填充不同的值 df.fillna(value=values, limit=1) # 只替换第一个

df['total'] = df.sum(axis=1) #四个季度的成绩相加为总成绩
print('四个季度的成绩相加为总成绩:\n',df)

data16 = df.where(df.Q1 > 90) #Q1大于90的数据,不满足条件的都返回为NaN
print('Q1大于90的数据:\n',data16)