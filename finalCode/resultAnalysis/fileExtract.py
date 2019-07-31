# -*- coding:utf-8 -*-
# 另一种提取各天次结果方法
import pandas as pd
data = pd.read_csv(r"E:\paperData\rfTrain_predData.txt",sep='\t')
for i in {}.fromkeys(list(data['fileName'])).keys():
    print(i)
    data2 = data[data.fileName == i]
    data2.to_csv(r'E:\paperData\allData\%s'%i,sep='\t',index=False)