# -*- coding: utf-8
#读文件,提取原始数据中的有效字段
import os
import pandas as pd
# import final_code
import time
from datetime import date, datetime
#处理文件数量
def readFile(filepath):
    # f1 = open(filepath, "r")
    nowDir = os.path.split(filepath)[0]                  #获取路径中的父文件夹路径
    fileName = os.path.split(filepath)[1]                #获取路径中文件名
    # nowDir = nowDir.rstrip().split("\")
    WifiDataDir = os.path.join(nowDir, "New" + fileName) #对新生成的文件进行命名的过程
    data = pd.read_csv(filepath, encoding='utf-8', header=0,sep = '\t')
    data.columns = ['Time', 'Long', 'Lat', 'X', 'Y', 'Ax', 'Ay', 'Az', '3','4']
    data = data[['Time', 'Long', 'Lat','X', 'Y', 'Ax','Ay','Az']]
    T = []
    time = []
    for i in range(len(data)):
        T.append(str(data['Time'][i])[0:10])
        t1 = int(T[i])
        stamp = datetime.fromtimestamp(t1)
        # print(stamp)
        timeArray = datetime.strftime(stamp, "%Y/%m/%d %H:%M:%S")
        time.append(timeArray)
    data['Time'] = T
    data['time'] = time
    data = data[['Time', 'Long', 'Lat','X', 'Y', 'Ax','Ay','Az','time']]
    data.to_csv(WifiDataDir,index=False,sep = '\t')
def eachFile(filepath):
    count = 0
    pathDir = os.listdir(filepath)      #获取当前路径下的文件名，返回List
    for s in pathDir:
        newDir=os.path.join(filepath,s)     #将文件命加入到当前文件路径后面
        if os.path.isfile(newDir):         #如果是文件
            if os.path.splitext(newDir)[1]==".txt":  #判断是否是txt
                readFile(newDir)
                count+=1#读文件
                pass
        else:
            eachFile(newDir)                #如果不是文件，递归这个文件夹的路径
eachFile(r'E:\Data\preprocessedData\wk\other')