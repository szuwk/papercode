# -*- coding: utf-8
# 特征重要性计算
import numpy as np
import pandas as pd
from sklearn.svm import SVC
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import MultinomialNB
df = pd.read_csv(r'E:\Data\RF\data_processed\result\rfTest\adaTrain_final.txt', sep='\t')

x, y = df.iloc[:, 0:57].values, df.iloc[:, 58].values
feat_labels = df.columns[0:57]
log_model = RandomForestClassifier()
# log_model = AdaBoostClassifier()
# log_model=GradientBoostingClassifier()
# log_model = MultinomialNB()
# log_model = DecisionTreeClassifier()

log_model.fit(x,y)
importances = log_model.feature_importances_
indices = np.argsort(importances)[::-1]
for f in range(x.shape[1]):
    print("%2d) %-*s %f" % (f + 1, 30, feat_labels[indices[f]], importances[indices[f]]))