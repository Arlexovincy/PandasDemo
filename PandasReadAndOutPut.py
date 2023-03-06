import pandas as pd

# 读取Excel文件
teamData = pd.read_excel('team.xlsx') # 默认读取第一个标签页sheet
print("从本地读取Excel:\n",teamData)

#从url读取Excel文件
remoteExcelData = pd.read_excel('https://www.gairuo.com/file/data/dataset/team.xlsx')
print("从url读取Excel文件:\n",remoteExcelData)

# 读取JSON数据
jdata = '{"res":{"model":"iphone","browser":"safari","version":"604.1"}}'
jsonData = pd.read_json(jdata)
print("读取JSON数据:\n",jsonData)

#输出Excel
jsonData.to_excel('jsonTest.xlsx')