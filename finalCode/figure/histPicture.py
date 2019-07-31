import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from pylab import mpl
mpl.rcParams['font.sans-serif'] = ['SimHei']  # 设置字体为黑体
mpl.rcParams['axes.unicode_minus'] = False
data = pd.read_csv('../transpatternCount/a.txt',sep = '\t')
data = data[data.trans_pattern==7]
# data = data[data.trans_pattern!=7]
# data = data[data.trans_pattern!=8]
print(data['continuedTime'].describe())
# data = data[data.continuedTime<8356]
x = np.array(data['continuedTime'])
fig = plt.figure()
ax = fig.add_subplot(1,1,1)

ax.hist(x,bins=50)
ax.set_title('室内运动时间-轨迹段个数')
ax.set_xlabel('室内运动时间(秒)')
ax.set_ylabel('轨迹段个数（次）')
# plt.savefig(r'室内运动时间-轨迹段个数.png')
fig.show()