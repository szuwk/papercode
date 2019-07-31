# -*- coding:utf-8 -*-
# 出行方式统计
import pandas as pd
import matplotlib.pyplot as plt
# plt.rcParams['font.family'] = ['sans-serif']
# plt.rcParams[ 'font.sans-serif'] = [ 'Microsoft YaHei']
# plt.rcParams[ 'axes.unicode_minus'] = False
from pylab import mpl
mpl.rcParams['font.sans-serif'] = ['SimHei']  # 设置字体为黑体
mpl.rcParams['axes.unicode_minus'] = False
data = pd.read_csv(r'E:\Data\preprocessedData\addfile.txt',sep='\t')
# thisTerm_data = pd.read_csv(r'E:\Data\RF\data_processed\latest_data\ztt_423.txt', sep='\t')
# print(thisTerm_data.columns)


# 提取真值数据每一段运动的开始时间，结束时间，经纬度，运动方式，计算持续时间
# 提取预测数据每一段运动的开始时间，结束时间，经纬度，运动方式，计算持续时间
def transData(data):  # 运动方式转换
    trans_pattern1 = []
    for i in range(len(data)):
        if data['A5'][i] == 1 and data['trans_pattern'][i] == 7:
            trans_pattern1.append(5)
        elif data['A5'][i] == 1 and data['trans_pattern'][i] != 7:
            trans_pattern1.append(data['trans_pattern'][i])
        elif data['A5'][i] != 1 and data['trans_pattern'][i] == 1:
            trans_pattern1.append(7)
        elif data['A5'][i] != 1 and data['trans_pattern'][i] == 2:
            trans_pattern1.append(8)
        else:
            trans_pattern1.append(data['trans_pattern'][i])
    data['trans_pattern'] = trans_pattern1
    return data

def extract(data):  # 提取字段函数
    startTime = []
    endTime = []
    A5 = []
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
        print(newData['A5'][0])
        init = newData['A5'][0]
        count = 0
        i = 0
        while i <= len(newData) - 1:
            if int(init) == int(newData['A5'][i]):
                count += 1
                if count == 1:
                    startTime.append(newData['Time'][i])
                    A5.append(newData['A5'][i])
                    startLong.append(newData['Long'][i])
                    startLat.append(newData['Lat'][i])
                    startX.append(newData['A3'][i])
                    startY.append(newData['A4'][i])
                    filename.append(file)
            else:
                continuedTime.append(count)
                endTime.append(newData['Time'][i - 1])
                endLong.append(newData['Long'][i - 1])
                endLat.append(newData['Lat'][i - 1])
                count = 0
                init = newData['A5'][i]
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
    data2['A5'] =A5
    data2['fileName']=filename
    return data2
# 提取持续时间大于10小时的天次数据
def convert(data,initData):
    file  = set(list(data['fileName']))
    for i in file:
        if len(data[data.fileName==i])>36000:
            initData = initData.append(data[data.fileName==i])
    return initData

data = extract(data)
# 计算室内和室外天次的数量
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
# n1,n2=calnum(thisTerm_data)
# n3,n4 = calnum(lastTerm_data)
# print(n1,n2,n3,n4)
#
data.to_csv(r'E:\Data\preprocessedData\extract.txt', sep = '\t',index=False)

'''
print(data['continuedTime'].describe())
for i in range(1,9):
    print(i,data[data.trans_pattern == i]['continuedTime'].describe())
# print(data[data.trans_pattern==8]['continuedTime'].describe())
count = [len(data[data.trans_pattern==i]) for i in range(1,9)]
print(count)
def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        plt.text(rect.get_x()+rect.get_width()/2.-0.2, 1.03*height, '%s' % float(height))
name_list = [r'室外静止', r'步行', r'自行车', r'小巴',r'公交',r'地铁',r'室内静止',r'室内运动']
num_list = [len(data[data.trans_pattern==i]) for i in range(1,9)]
plt.style.use('ggplot')
a = plt.bar(range(len(num_list)), num_list, color = 'lightskyblue',tick_label=name_list)
autolabel(a)

plt.xlabel("出行方式")
plt.ylabel("轨迹段数量")
plt.title("出行方式-轨迹段数量")
plt.show()
'''