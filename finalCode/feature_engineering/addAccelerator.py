# -*- coding:utf-8 -*-
# -*- coding:utf-8 -*-
# 增加手机加速度计特征,包括X,Y，Z以及和加速度的平均值，均值，标准差，前25%，75%分位值
import os
import pandas as pd
import datetime
from scipy.interpolate import lagrange
import numpy as np


def getLine(x, y):
    pdist = np.sqrt(np.sum(np.square(x - y)))
    return pdist


def getFeature(data, interval):
    meanX = []
    meanY = []
    meanZ = []
    stdX = []
    stdY = []
    stdZ = []
    meanXYZ = []
    stdXYZ = []
    medianXYZ = []
    percent25 = []
    percent75 = []
    medianX = []
    medianY = []
    medianZ = []
    percentX25 = []
    percentY25 = []
    percentZ25 = []
    percentX75 = []
    percentY75 = []
    percentZ75 = []
    for i in range(int((interval - 1) / 2), int(len(data) - (interval - 1) / 2)):
        meanX.append(np.mean(
            np.array([abs(data['Ax'][row]) for row in range(i - int((interval - 1) / 2), i + int((interval + 1) / 2))])))
        meanY.append(np.mean(
            np.array([abs(data['Ay'][row]) for row in range(i - int((interval - 1) / 2), i + int((interval + 1) / 2))])))
        meanZ.append(np.mean(
            np.array([abs(data['Az'][row]) for row in range(i - int((interval - 1) / 2), i + int((interval + 1) / 2))])))
        stdX.append(np.std(
            np.array([abs(data['Ax'][row]) for row in range(i - int((interval - 1) / 2), i + int((interval + 1) / 2))])))
        stdY.append(np.std(
            np.array([abs(data['Ay'][row]) for row in range(i - int((interval - 1) / 2), i + int((interval + 1) / 2))])))
        stdZ.append(np.std(
            np.array([abs(data['Az'][row]) for row in range(i - int((interval - 1) / 2), i + int((interval + 1) / 2))])))
        meanXYZ.append(np.mean(
            np.array([data['sumXYZ'][row] for row in range(i - int((interval - 1) / 2), i + int((interval + 1) / 2))])))
        stdXYZ.append(np.std(
            np.array([data['sumXYZ'][row] for row in range(i - int((interval - 1) / 2), i + int((interval + 1) / 2))])))
        medianXYZ.append(np.median(
            np.array([data['sumXYZ'][row] for row in range(i - int((interval - 1) / 2), i + int((interval + 1) / 2))])))
        percent25.append(np.percentile(
            np.array([data['sumXYZ'][row] for row in range(i - int((interval - 1) / 2), i + int((interval + 1) / 2))]),
            25))
        percent75.append(np.percentile(
            np.array([data['sumXYZ'][row] for row in range(i - int((interval - 1) / 2), i + int((interval + 1) / 2))]),
            75))
        medianX.append(np.median(
            np.array([abs(data['Ax'][row]) for row in range(i - int((interval - 1) / 2), i + int((interval + 1) / 2))])))
        percentX25.append(np.percentile(
            np.array([abs(data['Ax'][row]) for row in range(i - int((interval - 1) / 2), i + int((interval + 1) / 2))]), 25))
        percentX75.append(np.percentile(
            np.array([abs(data['Ax'][row]) for row in range(i - int((interval - 1) / 2), i + int((interval + 1) / 2))]), 75))
        medianY.append(np.median(
            np.array([abs(data['Ay'][row]) for row in range(i - int((interval - 1) / 2), i + int((interval + 1) / 2))])))
        percentY25.append(np.percentile(
            np.array([abs(data['Ay'][row]) for row in range(i - int((interval - 1) / 2), i + int((interval + 1) / 2))]), 25))
        percentY75.append(np.percentile(
            np.array([abs(data['Ay'][row]) for row in range(i - int((interval - 1) / 2), i + int((interval + 1) / 2))]), 75))
        medianZ.append(np.median(
            np.array([abs(data['Az'][row]) for row in range(i - int((interval - 1) / 2), i + int((interval + 1) / 2))])))
        percentZ25.append(np.percentile(
            np.array([abs(data['Az'][row]) for row in range(i - int((interval - 1) / 2), i + int((interval + 1) / 2))]), 25))
        percentZ75.append(np.percentile(
            np.array([abs(data['Az'][row]) for row in range(i - int((interval - 1) / 2), i + int((interval + 1) / 2))]), 75))
        if i == int((interval - 1) / 2):
            for j in range(int((interval - 1) / 2)):
                meanX.append(np.mean(
                    np.array([abs(data['Ax'][row]) for row in
                              range(i - int((interval - 1) / 2), i + int((interval + 1) / 2))])))
                meanY.append(np.mean(
                    np.array([abs(data['Ay'][row]) for row in
                              range(i - int((interval - 1) / 2), i + int((interval + 1) / 2))])))
                meanZ.append(np.mean(
                    np.array([abs(data['Az'][row]) for row in
                              range(i - int((interval - 1) / 2), i + int((interval + 1) / 2))])))
                stdX.append(np.std(
                    np.array([abs(data['Ax'][row]) for row in
                              range(i - int((interval - 1) / 2), i + int((interval + 1) / 2))])))
                stdY.append(np.std(
                    np.array([abs(data['Ay'][row]) for row in
                              range(i - int((interval - 1) / 2), i + int((interval + 1) / 2))])))
                stdZ.append(np.std(
                    np.array([abs(data['Az'][row]) for row in
                              range(i - int((interval - 1) / 2), i + int((interval + 1) / 2))])))
                meanXYZ.append(np.mean(
                    np.array([data['sumXYZ'][row] for row in
                              range(i - int((interval - 1) / 2), i + int((interval + 1) / 2))])))
                stdXYZ.append(np.std(
                    np.array([data['sumXYZ'][row] for row in
                              range(i - int((interval - 1) / 2), i + int((interval + 1) / 2))])))
                medianXYZ.append(np.median(
                    np.array([data['sumXYZ'][row] for row in
                              range(i - int((interval - 1) / 2), i + int((interval + 1) / 2))])))
                percent25.append(np.percentile(
                    np.array([data['sumXYZ'][row] for row in
                              range(i - int((interval - 1) / 2), i + int((interval + 1) / 2))]),
                    25))
                percent75.append(np.percentile(
                    np.array([data['sumXYZ'][row] for row in
                              range(i - int((interval - 1) / 2), i + int((interval + 1) / 2))]),
                    75))
                medianX.append(np.median(
                    np.array([abs(data['Ax'][row]) for row in
                              range(i - int((interval - 1) / 2), i + int((interval + 1) / 2))])))
                percentX25.append(np.percentile(
                    np.array([abs(data['Ax'][row]) for row in
                              range(i - int((interval - 1) / 2), i + int((interval + 1) / 2))]), 25))
                percentX75.append(np.percentile(
                    np.array([abs(data['Ax'][row]) for row in
                              range(i - int((interval - 1) / 2), i + int((interval + 1) / 2))]), 75))
                medianY.append(np.median(
                    np.array([abs(data['Ay'][row]) for row in
                              range(i - int((interval - 1) / 2), i + int((interval + 1) / 2))])))
                percentY25.append(np.percentile(
                    np.array([abs(data['Ay'][row]) for row in
                              range(i - int((interval - 1) / 2), i + int((interval + 1) / 2))]), 25))
                percentY75.append(np.percentile(
                    np.array([abs(data['Ay'][row]) for row in
                              range(i - int((interval - 1) / 2), i + int((interval + 1) / 2))]), 75))
                medianZ.append(np.median(
                    np.array([abs(data['Az'][row]) for row in
                              range(i - int((interval - 1) / 2), i + int((interval + 1) / 2))])))
                percentZ25.append(np.percentile(
                    np.array([abs(data['Az'][row]) for row in
                              range(i - int((interval - 1) / 2), i + int((interval + 1) / 2))]), 25))
                percentZ75.append(np.percentile(
                    np.array([abs(data['Az'][row]) for row in
                              range(i - int((interval - 1) / 2), i + int((interval + 1) / 2))]), 75))
    for j in range(int((interval - 1) / 2)):
        meanX.append(np.mean(
            np.array([abs(data['Ax'][row]) for row in range(i - int((interval - 1) / 2), i + int((interval + 1) / 2))])))
        meanY.append(np.mean(
            np.array([abs(data['Ay'][row]) for row in range(i - int((interval - 1) / 2), i + int((interval + 1) / 2))])))
        meanZ.append(np.mean(
            np.array([abs(data['Az'][row]) for row in range(i - int((interval - 1) / 2), i + int((interval + 1) / 2))])))
        stdX.append(np.std(
            np.array([abs(data['Ax'][row]) for row in range(i - int((interval - 1) / 2), i + int((interval + 1) / 2))])))
        stdY.append(np.std(
            np.array([abs(data['Ay'][row]) for row in range(i - int((interval - 1) / 2), i + int((interval + 1) / 2))])))
        stdZ.append(np.std(
            np.array([abs(data['Az'][row]) for row in range(i - int((interval - 1) / 2), i + int((interval + 1) / 2))])))
        meanXYZ.append(np.mean(
            np.array([data['sumXYZ'][row] for row in range(i - int((interval - 1) / 2), i + int((interval + 1) / 2))])))
        stdXYZ.append(np.std(
            np.array([data['sumXYZ'][row] for row in range(i - int((interval - 1) / 2), i + int((interval + 1) / 2))])))
        medianXYZ.append(np.median(
            np.array([data['sumXYZ'][row] for row in range(i - int((interval - 1) / 2), i + int((interval + 1) / 2))])))
        percent25.append(np.percentile(
            np.array([data['sumXYZ'][row] for row in range(i - int((interval - 1) / 2), i + int((interval + 1) / 2))]),
            25))
        percent75.append(np.percentile(
            np.array([data['sumXYZ'][row] for row in range(i - int((interval - 1) / 2), i + int((interval + 1) / 2))]),
            75))
        medianX.append(np.median(
            np.array([abs(data['Ax'][row]) for row in range(i - int((interval - 1) / 2), i + int((interval + 1) / 2))])))
        percentX25.append(np.percentile(
            np.array([abs(data['Ax'][row]) for row in range(i - int((interval - 1) / 2), i + int((interval + 1) / 2))]), 25))
        percentX75.append(np.percentile(
            np.array([abs(data['Ax'][row]) for row in range(i - int((interval - 1) / 2), i + int((interval + 1) / 2))]), 75))
        medianY.append(np.median(
            np.array([abs(data['Ay'][row]) for row in range(i - int((interval - 1) / 2), i + int((interval + 1) / 2))])))
        percentY25.append(np.percentile(
            np.array([abs(data['Ay'][row]) for row in range(i - int((interval - 1) / 2), i + int((interval + 1) / 2))]), 25))
        percentY75.append(np.percentile(
            np.array([abs(data['Ay'][row]) for row in range(i - int((interval - 1) / 2), i + int((interval + 1) / 2))]), 75))
        medianZ.append(np.median(
            np.array([abs(data['Az'][row]) for row in range(i - int((interval - 1) / 2), i + int((interval + 1) / 2))])))
        percentZ25.append(np.percentile(
            np.array([abs(data['Az'][row]) for row in range(i - int((interval - 1) / 2), i + int((interval + 1) / 2))]), 25))
        percentZ75.append(np.percentile(
            np.array([abs(data['Az'][row]) for row in range(i - int((interval - 1) / 2), i + int((interval + 1) / 2))]), 75))
    data['meanX%d' % interval] = meanX
    data['medianX%d' % interval] = medianX
    data['percentX25%d' % interval] = percentX25
    data['percentX75%d' % interval] = percentX75
    data['meanY%d' % interval] = meanY
    data['medianY%d' % interval] = medianY
    data['percentY25%d' % interval] = percentY25
    data['percentY75%d' % interval] = percentY75
    data['meanZ%d' % interval] = meanZ
    data['medianZ%d' % interval] = medianZ
    data['percentZ25%d' % interval] = percentZ25
    data['percentZ75%d' % interval] = percentZ75
    data['stdX%d' % interval] = stdX
    data['stdY%d' % interval] = stdY
    data['stdZ%d' % interval] = stdZ
    data['meanXYZ%d' % interval] = meanXYZ
    data['stdXYZ%d' % interval] = stdXYZ
    data['medianXYZ%d' % interval] = medianXYZ
    data['percent25%d' % interval] = percent25
    data['percent75%d' % interval] = percent75
    return data


def ployinterp_column(s, n, k=5):  # k=2表示用空值的前后两个数值来拟合曲线，从而预测空值
    y = s[list(range(n - k, n)) + list(range(n + 1, n + 1 - k))]  # 取值，range函数返回一个左闭右开（[left,right)）的序列数
    y = y[y.notnull()]  # 取上一行中取出数值列表中的非空值，保证y的每行都有数值，便于拟合函数
    return lagrange(y.index, list(y))(n)  # 调用拉格朗日函数，并添加索引


# 处理文件数量
def readFile(filepath):
    from calmanFilter import kalman_filter
    start_time = datetime.datetime.now()
    print(start_time)
    nowDir = os.path.split(filepath)[0]  # 获取路径中的父文件夹路径
    fileName = os.path.split(filepath)[1]  # 获取路径中文件名
    # nowDir = nowDir.rstrip().split("\")
    WifiDataDir = os.path.join(r'E:\Data\RF\data_processed\latest_data\newData\addAcceleratorData',
                               fileName)  # 对新生成的文件进行命名的过程
    data = pd.read_csv(filepath, sep='\t')
    for i in ['Ax', 'Ay', 'Az']:  # 如果i在data的列名中，data.columns生成的是data的全部列名
        for j in range(10, len(data)):  # len(data)返回了data的长度，若此长度为5，则range(5)会产生从0开始计数的整数列表
            if (data[i].isnull()[j] or data[i][j] == 0):
                print(i, j)
                # 如果data[i][j]为空，则调用函数ployinterp_column为其插值
                data.loc[j, i] = ployinterp_column(data[i], j)
                # print(data[i][j])
    sumXYZ = []
    for i in range(len(data)):
        sumXYZ.append(np.sqrt(np.square(data['Ax'][i]) + np.square(data['Ay'][i]) + np.square(data['Az'][i])))
    data['sumXYZ'] = sumXYZ
    data.to_csv(WifiDataDir, sep='\t', index=False)
    data = pd.read_csv(WifiDataDir, sep='\t')
    data = getFeature(data, 5)
    end_time = datetime.datetime.now()
    print("filename为%s时" % (fileName))
    print('计算interval = 5时，一共运行了%d秒' % (end_time - start_time).seconds)
    Start_time = datetime.datetime.now()
    data = getFeature(data, 11)
    end_time = datetime.datetime.now()
    print('计算interval = 11时，一共运行了%d秒' % (end_time - Start_time).seconds)
    Start_time = datetime.datetime.now()
    data = getFeature(data, 21)
    end_time = datetime.datetime.now()
    print('计算interval = 21时，一共运行了%d秒' % (end_time - Start_time).seconds)
    Start_time = datetime.datetime.now()
    data = getFeature(data, 31)
    end_time = datetime.datetime.now()
    print('计算interval = 31时，一共运行了%d秒' % (end_time - Start_time).seconds)
    Start_time = datetime.datetime.now()
    data = getFeature(data, 61)
    end_time = datetime.datetime.now()
    print('计算interval = 61时，一共运行了%d秒' % (end_time - Start_time).seconds)
    Start_time = datetime.datetime.now()
    data = getFeature(data, 121)
    end_time = datetime.datetime.now()
    print('计算interval = 121时，一共运行了%d秒' % (end_time - Start_time).seconds)
    Start_time = datetime.datetime.now()
    # data = getFeature(data, 301)
    end_time = datetime.datetime.now()
    print('计算interval = 301时，一共运行了%d秒' % (end_time - Start_time).seconds)
    Start_time = datetime.datetime.now()
    # data = getFeature(data, 601)
    end_time = datetime.datetime.now()
    print('计算interval = 601时，一共运行了%d秒' % (end_time - Start_time).seconds)
    end_time = datetime.datetime.now()
    print('一共运行了%d秒' % (end_time - start_time).seconds)
    finalPath = os.path.join(r'E:\Data\RF\data_processed\latest_data\newData\addAcceleratorData', fileName)
    data.to_csv(finalPath, sep='\t', index=False)


def eachFile(filepath):
    count = 0
    pathDir = os.listdir(filepath)  # 获取当前路径下的文件名，返回List
    for s in pathDir:
        newDir = os.path.join(filepath, s)  # 将文件命加入到当前文件路径后面
        if os.path.isfile(newDir):  # 如果是文件
            if os.path.splitext(newDir)[1] == ".txt":  # 判断是否是txt

                readFile(newDir)
                count += 1  # 读文件
                pass
        else:
            eachFile(newDir)  # 如果不是文件，递归这个文件夹的路径


eachFile(r'E:\Data\RF\data_processed\result\rfTest\filterPattern\d')
