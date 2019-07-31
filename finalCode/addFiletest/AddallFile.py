# -*- coding:utf-8 -*-
# 各天次文件合并
import pandas as pd
import os
import datetime
def eachFile(filepath):
    count = 0
    data = pd.DataFrame(columns = ['Time','Long','Lat','X','Y','Ax','Ay','Az','A1','A2','A3','A4',
                 'A5','fileName'])
        # 'Len5', 'Speed5', 'Acceleration5', 'displacement5', 'V_var5', 'A_var5',
        #          'Point_density5', 'Len11', 'Speed11', 'Acceleration11', 'displacement11', 'V_var11', 'A_var11',
        #          'Point_density11', 'Len21', 'Speed21', 'Acceleration21', 'displacement21', 'V_var21', 'A_var21',
        #          'Point_density21', 'Len31', 'Speed31', 'Acceleration31', 'displacement31', 'V_var31', 'A_var31',
        #          'Point_density31', 'Len61', 'Speed61', 'Acceleration61', 'displacement61', 'V_var61', 'A_var61',
        #          'Point_density61', 'Len121', 'Speed121', 'Acceleration121', 'displacement121', 'V_var121', 'A_var121',
        #          'Point_density121', 'Len301', 'Speed301', 'Acceleration301', 'displacement301', 'V_var301', 'A_var301',
        #          'Point_density301', 'Len601', 'Speed601', 'Acceleration601', 'displacement601', 'V_var601', 'A_var601',
        #          'Point_density601',
                                   # 'sumXYZ', 'meanX5', 'medianX5', 'percentX255', 'percentX755', 'meanY5', 'medianY5', 'percentY255', 'percentY755', 'meanZ5', 'medianZ5', 'percentZ255', 'percentZ755', 'stdX5', 'stdY5', 'stdZ5', 'meanXYZ5', 'stdXYZ5', 'medianXYZ5', 'percent255', 'percent755', 'meanX11', 'medianX11', 'percentX2511', 'percentX7511', 'meanY11', 'medianY11', 'percentY2511', 'percentY7511', 'meanZ11', 'medianZ11', 'percentZ2511', 'percentZ7511', 'stdX11', 'stdY11', 'stdZ11', 'meanXYZ11', 'stdXYZ11', 'medianXYZ11', 'percent2511', 'percent7511', 'meanX21', 'medianX21', 'percentX2521', 'percentX7521', 'meanY21', 'medianY21', 'percentY2521', 'percentY7521', 'meanZ21', 'medianZ21', 'percentZ2521', 'percentZ7521', 'stdX21', 'stdY21', 'stdZ21', 'meanXYZ21', 'stdXYZ21', 'medianXYZ21', 'percent2521', 'percent7521', 'meanX31', 'medianX31', 'percentX2531', 'percentX7531', 'meanY31', 'medianY31', 'percentY2531', 'percentY7531', 'meanZ31', 'medianZ31', 'percentZ2531', 'percentZ7531', 'stdX31', 'stdY31', 'stdZ31', 'meanXYZ31', 'stdXYZ31', 'medianXYZ31', 'percent2531', 'percent7531', 'meanX61', 'medianX61', 'percentX2561', 'percentX7561', 'meanY61', 'medianY61', 'percentY2561', 'percentY7561', 'meanZ61', 'medianZ61', 'percentZ2561', 'percentZ7561', 'stdX61', 'stdY61', 'stdZ61', 'meanXYZ61', 'stdXYZ61', 'medianXYZ61', 'percent2561', 'percent7561', 'meanX121', 'medianX121', 'percentX25121', 'percentX75121', 'meanY121', 'medianY121', 'percentY25121', 'percentY75121', 'meanZ121', 'medianZ121', 'percentZ25121', 'percentZ75121', 'stdX121', 'stdY121', 'stdZ121', 'meanXYZ121', 'stdXYZ121', 'medianXYZ121', 'percent25121', 'percent75121',

                                   # 'fileName','trans_pattern','y_pred','filterPattern'])
        # , 'trans_pattern','y_pred','filterPattern'])
    pathDir = os.listdir(filepath)  # 获取当前路径下的文件名，返回List
    for s in pathDir:
        newDir = os.path.join(filepath, s)  # 将文件命加入到当前文件路径后面
        if os.path.isfile(newDir):  # 如果是文件
            if os.path.splitext(newDir)[1] == ".txt":  # 判断是否是txt
                data1=readFile(newDir)
                data=data.append(data1)
                count += 1  # 读文件
                pass
        else:
            eachFile(newDir)  # 如果不是文件，递归这个文件夹的路径
    return data
def readFile(filepath):
    start_time = datetime.datetime.now()
    print(start_time)
    # nowDir = os.path.split(filepath)[0]  # 获取路径中的父文件夹路径
    fileName = os.path.split(filepath)[1]  # 获取路径中文件名
    # nowDir = nowDir.rstrip().split("\")
    # WifiDataDir = os.path.join('E:\Data\RF\data_processed', fileName)  # 对新生成的文件进行命名的过程
    # data=pd.read_csv(r'E:\Data\RF\data_processed\result\data.txt', sep='\t')
    print(fileName)
    data = pd.read_csv(filepath, sep='\t')

    print([i for i in data.columns])

    data['fileName']=[fileName for i in range(len(data))]
    data = data[[
        'Time','Long','Lat','X','Y','Ax','Ay','Az','A1','A2','A3','A4',
        'A5','fileName']]
        # 'Len5',	'Speed5'	,'Acceleration5',	'displacement5',	'V_var5',	'A_var5'	,'Point_density5',	'Len11',	'Speed11',	'Acceleration11'	,'displacement11',	'V_var11',	'A_var11',	'Point_density11'	,'Len21'	,'Speed21',	'Acceleration21'	,'displacement21',	'V_var21'	,'A_var21'	,'Point_density21'	,'Len31',	'Speed31',	'Acceleration31'	,'displacement31',	'V_var31'	,'A_var31'	,'Point_density31',	'Len61'	,'Speed61',	'Acceleration61'	,'displacement61'	,'V_var61',	'A_var61'	,'Point_density61'	,'Len121'	,'Speed121'	,'Acceleration121',	'displacement121'	,'V_var121',	'A_var121'	,'Point_density121',	'Len301',	'Speed301','Acceleration301',	'displacement301',	'V_var301',	'A_var301',	'Point_density301',	'Len601'	,'Speed601'	,'Acceleration601',	'displacement601',	'V_var601',	'A_var601'	,'Point_density601',
        # 'fileName','trans_pattern','y_pred','filterPattern']]
        # ,'trans_pattern','y_pred','filterPattern']]
    return data
data = eachFile(r'E:\Data\preprocessedData\addFile')
data.to_csv(r'E:\Data\preprocessedData\addfile.txt',sep='\t',index=False)

