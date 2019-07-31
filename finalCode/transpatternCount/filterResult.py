# -*- coding:utf-8 -*-
import pandas as pd
import numpy as np
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
data = pd.read_csv(r'E:\Data\RF\data_processed\result\concatData\filterPatternprocessed.txt',sep='\t')
filterPattern = data['filterPattern']
print(confusion_matrix(data['trans_pattern'], data['filterPattern']))

cm = confusion_matrix(data['trans_pattern'], filterPattern)
target_names = ['室外静止', '室外运动', '自行车','小巴','公交','室内静止','室内运动']
print(classification_report(data['trans_pattern'], filterPattern, target_names=target_names))
# cm = confusion_matrix(fileExtract['trans_pattern'], fileExtract['filterPattern'])
cm_normalized = cm / cm.sum(axis=1)[:, np.newaxis]
print(cm_normalized)
