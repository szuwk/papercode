# -*- coding:utf-8 -*-
# 出行结果滤波算法
import pandas as pd
import os
# p1, p2, p3, p4, p5, p6, p7, p8代表各出行方式持续时间的阈值，暂时取，p8=6，p1=60,其他取30
def patternFilter(data, p1, p2, p3, p4, p5, p6, p7, p8):
    filelist = set(list(data['fileName']))
    for file in filelist:
        print(file)
        newData = data[data.fileName == file]
        newData.to_csv(r'aaa.txt', sep='\t', index=False)
        newData = pd.read_csv(r'aaa.txt', sep='\t')
        newData['filterPattern']=list(newData['y_pred'])
        i = 0
        count = 0
        init = newData['filterPattern'][0]
        flag  = True
        while i <= len(newData) - 1:
            if int(init) == int(newData['filterPattern'][i]):
                count += 1
            else:
                if int(init) != 8 and int(init) != 1 and count > 30:
                    if flag == False:
                        newData.loc[:i - 1, 'filterPattern'] = i * [int(init)]
                        flag = True
                    pass
                elif int(init)==8 and count>5:
                    if flag == False:
                        newData.loc[:i - 1, 'filterPattern'] = i * [int(init)]
                        flag = True
                    pass
                elif int(init)==1 and count>60:
                    if flag == False:
                        newData.loc[:i - 1, 'filterPattern'] = i * [int(init)]
                        flag = True
                    pass
                else:
                    if i-count-1 <0:
                        flag = False
                    else:
                        newData.loc[i - count:i-1, 'filterPattern'] = count * [newData['filterPattern'][i-count -1]]
                init = newData['filterPattern'][i]
                i -= 1
                count = 0
            if i == len(newData) - 1:
                if int(init) != 8 and int(init) != 1 and count > 30:
                    pass
                elif int(init)==8 and count>5:
                    pass
                elif int(init)==1 and count>60:
                    pass
                else:
                    newData.loc[i - count+1:i, 'filterPattern'] = count * [newData['filterPattern'][i - count - 1]]
            i += 1
        lstdir = os.path.join(r'E:\Data\RF\data_processed\result\rfTest\filterProcessedpattern', file)
        newData.to_csv(lstdir,sep = '\t',index=False)


data = pd.read_csv(r"E:\Data\RF\data_processed\result\rfTest\rfTrain_patternProcessedfinal.txt", sep='\t')
print(data.columns)
patternFilter(data, 1, 2, 3, 4, 5, 6, 7, 8)