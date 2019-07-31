# -*- coding: utf-8
# 保存每一天次的结果
import pandas as pd
from sklearn.metrics import confusion_matrix
import numpy as np
import os
np.set_printoptions(suppress=True)
data = pd.read_csv(r"E:\Data\RF\data_processed\result\rfTest\filterPattern.txt",sep='\t')
fileNamelist = set(list(data['fileName']))
# num=[]
# number = []
# filename=[]
for i in fileNamelist:
    fileExtract=data[data.fileName==i]
    # print(i)
    # print(fileExtract['trans_pattern'].drop_duplicates(),'\n',fileExtract['y_pred'].drop_duplicates())
    # cm = confusion_matrix(fileExtract['trans_pattern'], fileExtract['y_pred'])
    # cm_normalized = cm / cm.sum(axis=1)[:, np.newaxis]
    # print(cm_normalized)
    lstdir = os.path.join(r'E:\Data\RF\data_processed\result\rfTest\RFeachFIle', i)
    print(i)
    print(set(list(fileExtract['trans_pattern'])))
    print(set(list(fileExtract['filterPattern'])))
    cm = confusion_matrix(fileExtract['trans_pattern'], fileExtract['filterPattern'])
    print(cm)
    cm = confusion_matrix(fileExtract['trans_pattern'], fileExtract['filterPattern'])
    cm_normalized = cm / cm.sum(axis=1)[:, np.newaxis]
    print(cm_normalized)
    fileExtract.to_csv(lstdir,sep = '\t',index=False)
# print(num)
# print(number)
# print(filename)