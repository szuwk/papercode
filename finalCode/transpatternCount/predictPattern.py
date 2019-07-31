# -*- coding:utf-8 -*-
# 对预测处理后的结果，统计出行方式
import pandas as pd
import matplotlib.pyplot as plt
from pylab import mpl
mpl.rcParams['font.sans-serif'] = ['SimHei']  # 设置字体为黑体
mpl.rcParams['axes.unicode_minus'] = False
def extract(data):  # 提取字段函数
    startTime = []
    endTime = []
    filterPattern = []
    continuedTime = []
    startLong = []
    startLat = []
    endLong = []
    endLat = []
    startX = []
    startY = []
    endX = []
    endY = []
    filename = []
    data2 = pd.DataFrame()
    filelist = set(list(data['fileName']))
    print(filelist)
    for file in filelist:
        newData = data[data.fileName==file]
        newData.to_csv(r'aaa.txt',sep='\t',index=False)
        newData = pd.read_csv(r'aaa.txt',sep='\t')
        print(file)
        init = newData['filterPattern'][0]
        count = 0
        i = 0
        while i <= len(newData) - 1:
            if int(init) == int(newData['filterPattern'][i]):
                count += 1
                if count == 1:
                    startTime.append(newData['Time'][i])
                    filterPattern.append(newData['filterPattern'][i])
                    startLong.append(newData['Long'][i])
                    startLat.append(newData['Lat'][i])
                    startX.append(newData['A3'][i])
                    startY.append(newData['A4'][i])
                    filename.append(file)
                print(init,count)
            else:
                continuedTime.append(count)
                endTime.append(newData['Time'][i - 1])
                endLong.append(newData['Long'][i - 1])
                endLat.append(newData['Lat'][i - 1])
                count = 0
                init = newData['filterPattern'][i]
                endX.append(newData['A3'][i - 1])
                endY.append(newData['A4'][i - 1])
                i-=1
            if i == len(newData) - 1:
                continuedTime.append(count)
                endTime.append(newData['Time'][i])
                endLong.append(newData['Long'][i])
                endLat.append(newData['Lat'][i])
                endX.append(newData['A3'][i])
                endY.append(newData['A4'][i])
            i += 1
            print(file+str(i))
    print(len(startTime), len(endTime))
    print(startTime)
    print(endTime)
    data2['startTime'] = startTime
    data2['endTime'] = endTime
    data2['startLong'] = startLong
    data2['startLat'] = startLat
    data2['endLong'] = endLong
    data2['endLat'] = endLat
    data2['startX'] = startX
    data2['startY'] = startY
    data2['endX'] = endX
    data2['endY'] = endY
    data2['continuedTime'] = continuedTime
    data2['filterPattern'] = filterPattern
    data2['fileName']=filename
    return data2

initData = pd.DataFrame(columns=['Time','Long','Lat','Ax','Ay','Az','A1','A2','A3','A4','A5','fileName','filterPattern'])
def convert(data,initData):
    file  = set(list(data['fileName']))
    for i in file:
        if len(data[data.fileName==i])>36000:
            initData = initData.append(data[data.fileName==i])
    return initData

data = pd.read_csv(r'E:\Data\RF\data_processed\result\rfTest\filterPattern.txt',sep = '\t')
# data = pd.read_csv(r'bbbbb.txt',sep = '\t')
# d = data[data.fileName =='gql_1108_1.txt']
# d.to_csv(r'bbbbb.txt',sep = '\t',index=False)
# print(data.columns)
data = extract(data)
data.to_csv(r'E:\Data\RF\data_processed\result\rfTest\filterPatternResult.txt',sep = '\t',index=False)
def calnum(data):
    indoor  =[]
    outdoor = []
    file = set(list(data['fileName']))
    for i in file:
        if len(data[data.trans_pattern==7])>0 or len(data[data.trans_pattern==8])>0:
            indoor.append(i)
        else:
            outdoor.append(i)
    return len(indoor),len(outdoor)
# data = data[data.fileName!='newmetro_402.txt']
print(data['continuedTime'].describe())
for i in range(1,9):
    print(i,data[data.filterPattern == i]['continuedTime'].describe())
# print(data[data.trans_pattern==8]['continuedTime'].describe())
count = [len(data[data.filterPattern==i]) for i in range(1,9)]
print(count)
def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        plt.text(rect.get_x()+rect.get_width()/2.-0.2, 1.03*height, '%s' % float(height))
name_list = [r'室外静止', r'步行', r'自行车', r'小巴',r'公交',r'地铁',r'室内静止',r'室内运动']
num_list = [len(data[data.filterPattern==i]) for i in range(1,9)]
plt.style.use('ggplot')
a = plt.bar(range(len(num_list)), num_list, color = 'lightskyblue',tick_label=name_list)
autolabel(a)

plt.xlabel("出行方式")
plt.ylabel("轨迹段数量")
plt.title("出行方式-轨迹段数量")
plt.show()