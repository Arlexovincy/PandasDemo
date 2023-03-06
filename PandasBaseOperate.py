import pandas as pd

dataUrl = 'https://www.gairuo.com/file/data/dataset/team.xlsx'
df = pd.read_excel(dataUrl) 
print('原始数据:\n',df)

df = df.set_index('name')
print("设置了索引后:\n",df)

df = df.reset_index() #重置索引
print('重置索引:\n',df)

# 为了方便查看数据，设置一下索引
df = df.set_index('name')

# 查看样本
s1 = df.Q1 #取Q1这一列
print('取某一列:\n',s1)

headFive = df.head(5) #取前五条数据
print('前五条数据:\n',headFive)

tailFive = df.tail(5) #取后五条数据
print('取后五条数据:\n',tailFive)

sampleThree = df.sample(3) #随机查看3条数据
print('随机查看3条数据:\n',sampleThree)

info = df.info #查看dataFrame的基本信息
print('基本信息:\n',info)

#统计计算
describe = df.describe() #基本都统计信息
print('基本统计信息:\n',describe)

mean = df.mean() #统计平均数
print('平均数统计:\n',mean)

q1Mean = df.Q1.mean() # Q1列的平均数统计
print('Q1列的平均数统计:\n',q1Mean)

rowMean = df.mean(axis=1) # 以此类推，可以统计其他很多的数据相关的数值比如绝对值、方差等
print('按行统计平均数:\n',rowMean)

#非统计计算
roundDF = df.round(2) #四舍五入，保留2位小数
print('四舍五入:\n',roundDF)

#数据选择

nameDF = df['Q1'] #获取name这一列的数据
print('获取Q1列的数据:\n',nameDF)

twoRowData = df[:2] #前两行的数据
print('获取前2行的数据:\n',twoRowData)

specialRowData = df[['Q1','Q4']] #获取Q1和Q4两列的数据
print('获取Q1和Q4两列的数据:\n',specialRowData)

zeroRow = df.loc['Liver'] #按照索引，获取某一行的数据
print('按照索引，获取某一行的数据:\n',zeroRow)

someRow = df.loc[['Liver','Gabriel','Eli']] #按照索引，获取某几行的数据
print('按照索引，获取某几行的数据:\n',someRow)

tenRow = df.loc['Liver':'Oah', ['Q1','Q2']] # Liver到Oah 的Q1和Q2的数据
print('Liver到Oah 的Q1和Q2的数据:\n',tenRow)

threeRow = df.iloc[:3] # 前3行
print('前3行\n',threeRow)

simple = df.iloc[:3, [0,1]] # 前3行数据，0,1列数据
print('simple:\n',simple)
