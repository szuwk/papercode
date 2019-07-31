# -*- coding:utf-8 -*-
# 特征工程
import os
import pandas as pd
import numpy as np
import datetime
from scipy.interpolate import lagrange
import math
from sklearn.cluster import KMeans

# 计算两点x，y之间的距离
def getLine(x, y):
    pdist = np.sqrt(np.sum(np.square(x - y)))
    return pdist

# 构造特征
def getFeature(data, interval):
    lenth = []                      #长度
    speed = []                      #速度
    acceleration = []               #加速度
    displacement = []               #位移
    V_var = []                     #速度方差
    A_var = []                     #加速度方差
    dist_max = []                  #点密度
    for i in range(int((interval - 1) / 2), int(len(data) - (interval - 1) / 2)):
        cal_lenth = 0
        cal_front_lenth = 0
        cal_back_lenth = 0
        for j in range(interval - 1):
            vec1 = [data['A3'][i - (interval - 1) / 2 + j], data['A4'][i - (interval - 1) / 2 + j]]
            vec2 = [data['A3'][i - (interval - 1) / 2 + j + 1], data['A4'][i - (interval - 1) / 2 + j + 1]]
            vec1 = np.array(vec1)
            vec2 = np.array(vec2)
            cal_lenth = cal_lenth + getLine(vec1, vec2)
            cal_speed = cal_lenth / interval
        for k in range(int((interval - 1) / 2)):
            vec1 = [data['A3'][i - (interval - 1) / 2 + k], data['A4'][i - (interval - 1) / 2 + k]]
            vec2 = [data['A3'][i - (interval - 1) / 2 + k + 1], data['A4'][i - (interval - 1) / 2 + k + 1]]
            vec1 = np.array(vec1)
            vec2 = np.array(vec2)
            cal_front_lenth = cal_front_lenth + getLine(vec1, vec2)
            vec3 = [data['A3'][i + k], data['A4'][i +k]]
            vec4 = [data['A3'][i + k + 1], data['A4'][i + k + 1]]
            vec3 = np.array(vec3)
            vec4 = np.array(vec4)
            cal_back_lenth = cal_back_lenth + getLine(vec3, vec4)
        clusterSet = [[data['A3'][i], data['A4'][i]]]
        for h in range(int((interval - 1) / 2)):
            clusterSet.append([data['A3'][i - h - 1], data['A4'][i - h - 1]])
            clusterSet.append([data['A3'][i + h + 1], data['A4'][i + h + 1]])
        kmeans = KMeans(n_clusters=1, random_state=0).fit(clusterSet)
        dist = [getLine(np.array([data['A3'][i], data['A4'][i]]),
                        np.array([kmeans.cluster_centers_[0][0], kmeans.cluster_centers_[0][1]]))]
        for k in range(int((interval - 1) / 2)):
            dist.append(getLine(np.array([data['A3'][i - k - 1], data['A4'][i - k - 1]]),
                                np.array([kmeans.cluster_centers_[0][0], kmeans.cluster_centers_[0][1]])))

            dist.append(getLine(np.array([data['A3'][i + k + 1], data['A4'][i + k + 1]]),
                                np.array([kmeans.cluster_centers_[0][0], kmeans.cluster_centers_[0][1]])))
        distMax = np.max(dist)
        if distMax==0:
            distMax=10000
        else:
            distMax = interval / (math.pi * distMax ** 2)
        cal_acceleration = abs(cal_back_lenth - cal_front_lenth) / 9
        vec1 = [data['A3'][i - int((interval - 1) / 2)], data['A4'][i - int((interval - 1) / 2)]]
        vec2 = [data['A3'][i + int((interval - 1) / 2)], data['A4'][i + int((interval - 1) / 2)]]
        vec1 = np.array(vec1)
        vec2 = np.array(vec2)
        cal_displacement = getLine(vec1, vec2)
        if len(lenth) == 0:
            lenth.extend([cal_lenth] * (int((interval + 1) / 2)))
            speed.extend([cal_speed] * (int((interval + 1) / 2)))
            acceleration.extend([cal_acceleration] * int((interval + 1) / 2))
            displacement.extend([cal_displacement] * int((interval + 1) / 2))
            dist_max.extend([distMax] * (int((interval + 1) / 2)))
        elif len(lenth) == len(data) - int((interval + 1) / 2):
            lenth.extend([cal_lenth] * (int((interval + 1) / 2)))
            speed.extend([cal_speed] * (int((interval + 1) / 2)))
            acceleration.extend([cal_acceleration] * int((interval + 1) / 2))
            displacement.extend([cal_displacement] * int((interval + 1) / 2))
            dist_max.extend([distMax] * (int((interval + 1) / 2)))
        else:
            lenth.append(cal_lenth)
            speed.append(cal_speed)
            acceleration.append(cal_acceleration)
            displacement.append(cal_displacement)
            dist_max.append(distMax)
    for i in range(int((interval - 1) / 2), int(len(data) - (interval - 1) / 2)):
        v_var = []
        a_var = []
        for j in range(1, int((interval + 1) / 2)):
            v_var.append(speed[i - j])
            a_var.append(acceleration[i - j])
            v_var.append(speed[i + j])
            a_var.append(acceleration[i + j])
        v_var.append(speed[i])
        a_var.append(acceleration[i])
        V_var_1 = np.array(v_var).var()
        A_var_1 = np.array(a_var).var()
        if len(V_var) == 0:
            V_var.extend([V_var_1] * int((interval + 1) / 2))
            A_var.extend([A_var_1] * int((interval + 1) / 2))
        elif len(V_var) == len(data) - int((interval + 1) / 2):
            V_var.extend([V_var_1] * int((interval + 1) / 2))
            A_var.extend([A_var_1] * int((interval + 1) / 2))
        else:
            V_var.append(V_var_1)
            A_var.append(A_var_1)
    data['Len%d' % interval] = lenth
    data['Speed%d' % interval] = speed
    data['Acceleration%d' % interval] = acceleration
    data['displacement%d' % interval] = displacement
    data['V_var%d' % interval] = V_var
    data['A_var%d' % interval] = A_var
    data['Point_density%d' % interval] = dist_max
    return data


def ployinterp_column(s, n, k=5):  # k=5表示用空值的前后5个数值来拟合曲线，从而预测空值
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
    WifiDataDir = os.path.join(r'E:\addData\featureData\newfeature', fileName)  # 对新生成的文件进行命名的过程
    data = pd.read_csv(filepath, sep='\t')
    # trans_pattern = []
    # for i in range(len(data)):
        # trans_pattern.append(5)
    # data['trans_pattern'] = trans_pattern
    # data = data[
    #     ['Time', 'Long', 'Lat', 'X', 'Y', 'Ax', 'Ay', 'Az', 'time', 'A1', 'A2', 'A3', 'A4', 'A5', 'trans_pattern']]
    # ---------------------增加卡尔曼滤波后平滑数据的特征，并增加新的点密度特征-------------------------------------
    kalman_filter = kalman_filter(0.001, 0.1)
    s = np.random.normal(0, 10, len(data))
    x = list(data['X'])
    y = list(data['Y'])
    print(len(x),len(s))
    test_array_x = s + x
    test_array_y = s + y
    adc_x = []
    adc_y = []
    # print(test_array_x)
    for i in range(len(data)):
        adc_y.append(kalman_filter.kalman(test_array_y[i]) / 10)
    for i in range(len(data)):
        adc_x.append(kalman_filter.kalman(test_array_x[i]) / 10)
    data['new_x'] = adc_x
    data['new_y'] = adc_y

    A3 = []
    A4 = []
    for i in range(len(data)):
        if data['X'][i] == 0 and data['Y'][i] == 0:
            A3.append(data['A1'][i])
            A4.append(data['A2'][i])
        else:
            A3.append(data['new_x'][i]  + 493342.6152)
            A4.append(data['new_y'][i]  + 2493102.4037)
    data['A3'] = A3
    data['A4'] = A4
    print(data['A3'])
    data = data[
        # ['Time', 'Long', 'Lat', 'X', 'Y', 'Ax', 'Ay', 'Az', 'time', 'A1', 'A2', 'A3', 'A4', 'A5', 'trans_pattern']]
        ['Time', 'Long', 'Lat', 'X', 'Y', 'Ax', 'Ay', 'Az', 'time', 'A1', 'A2', 'A3', 'A4', 'A5']]
    data.to_csv(r'1121.txt',sep ='\t',index=False)
    data = pd.read_csv(r'1121.txt',sep ='\t')
    # ---------------------------------------截止----------------------------------------

    for i in ['A3', 'A4' ,'Ax', 'Ay', 'Az']:  # 如果i在data的列名中，data.columns生成的是data的全部列名
        for j in range(10, len(data)):  # len(data)返回了data的长度，若此长度为5，则range(5)会产生从0开始计数的整数列表
            if (data[i].isnull()[j] or data[i][j] == 0):
                print(i, j)
                # print(data[i][j])
                # 如果data[i][j]为空，则调用函数ployinterp_column为其插值
                # data[i][j] = ployinterp_column(data[i], j)
                data.loc[j, i]=ployinterp_column(data[i], j)
                # print(data[i][j])
    # data = data[data.Long != 0]
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
    data = getFeature(data, 301)
    end_time = datetime.datetime.now()
    print('计算interval = 301时，一共运行了%d秒' % (end_time - Start_time).seconds)
    Start_time = datetime.datetime.now()
    data = getFeature(data, 601)
    end_time = datetime.datetime.now()
    print('计算interval = 601时，一共运行了%d秒' % (end_time - Start_time).seconds)
    end_time = datetime.datetime.now()
    print('一共运行了%d秒' % (end_time - start_time).seconds)
    finalPath = os.path.join(r'E:\addData\featureData\newfeature', fileName)
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

eachFile(r'E:\addData\addnewData\d')