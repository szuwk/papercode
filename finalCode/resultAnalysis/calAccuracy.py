# -*- coding:utf-8 -*-
# 结果预测
import pandas as pd
import numpy as np
from sklearn.metrics import confusion_matrix
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_predict
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report
np.set_printoptions(suppress=True)
data = pd.read_csv(r'E:\Data\RF\data_processed\result\concatData\patternProcessed.txt',sep='\t')

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

data = transData(data)

data.to_csv(r'E:\Data\RF\data_processed\result\concatData\rfTrain_patternProcessed.txt',sep='\t',index = False)
# rf训练集
data  = pd.read_csv(r"E:\Data\RF\data_processed\result\concatData\rfTrain_patternProcessed.txt", sep='\t')
# data1 = pd.read_csv(r"E:\Data\RF\data_processed\result\rfTest\addAccelerator_trainData.txt", sep='\t')
# print(data1.columns)
# print(data.isna(),'sfsdfsf')
# print(data.isnull())
data = data.replace('#VALUE!', 1)
data = data.replace('', 1)
data = data.dropna()
print('----------------------------------rf--------------------------------------------')
data = data[[
    'Time', 'Long', 'Lat','X','Y', 'Ax', 'Ay', 'Az', 'A1', 'A2', 'A3', 'A4',
    'A5',
    'Len5', 'Speed5', 'Acceleration5', 'displacement5', 'V_var5', 'A_var5', 'Point_density5', 'Len11', 'Speed11',
    'Acceleration11', 'displacement11', 'V_var11', 'A_var11', 'Point_density11', 'Len21', 'Speed21', 'Acceleration21',
    'displacement21', 'V_var21', 'A_var21', 'Point_density21', 'Len31', 'Speed31', 'Acceleration31', 'displacement31',
    'V_var31', 'A_var31', 'Point_density31', 'Len61', 'Speed61', 'Acceleration61', 'displacement61', 'V_var61',
    'A_var61', 'Point_density61', 'Len121', 'Speed121', 'Acceleration121', 'displacement121', 'V_var121', 'A_var121',
    'Point_density121', 'Len301', 'Speed301', 'Acceleration301', 'displacement301', 'V_var301', 'A_var301',
    'Point_density301', 'Len601', 'Speed601', 'Acceleration601', 'displacement601', 'V_var601', 'A_var601',
    'Point_density601','fileName','trans_pattern']]
    # 'y_pred', 'filterPattern']]
data = data[data.trans_pattern != 6]
print(len(data))
print(set(data['trans_pattern']))
log_model = RandomForestClassifier()
# log_model = AdaBoostClassifier()
# log_model=GradientBoostingClassifier()
# log_model = MultinomialNB()
# log_model = DecisionTreeClassifier()
X = data.ix[:, 12:69]
y = data.ix[:, 70]
# 加速计数据
# X = data.ix[:, 10:131]
# y = data.ix[:, 132]
# 提取加速度特征后数据
# X = data.ix[:, :20]
# y = data.ix[:, 20]
# 所有特征
# X = data.ix[:, 10:187]
# y = data.ix[:,188]
print(X, y)
# X = data.ix[:, 0:9]
# y = data.ix[:, 9]
# 十折交叉验证
y_pred = cross_val_predict(log_model, X, y, cv=10)

print(confusion_matrix(data['trans_pattern'], y_pred))
data['y_pred'] = y_pred
# rf训练结果
# data.to_csv(r"E:\Data\RF\data_processed\result\rfTest\rfTrain_final.txt", sep='\t', index=False)
# 传感器结果
data.to_csv(r"E:\Data\RF\data_processed\result\rfTest\rfTrain_patternProcessedfinal.txt", sep='\t', index=False)

cm = confusion_matrix(data['trans_pattern'], y_pred)
target_names = ['室外静止', '步行', '自行车', '小巴', '公交', '室内静止', '室内运动']
print(classification_report(data['trans_pattern'], y_pred, target_names=target_names))
# cm = confusion_matrix(fileExtract['trans_pattern'], fileExtract['y_pred'])
cm_normalized = cm / cm.sum(axis=1)[:, np.newaxis]
print(cm_normalized)
log_model.fit(X, y)
importances = log_model.feature_importances_
indices = np.argsort(importances)[::-1]
feat_labels = data.columns[12:69]
for f in range(X.shape[1]):
    print("%2d) %-*s %f" % (f + 1, 30, feat_labels[indices[f]], importances[indices[f]]))