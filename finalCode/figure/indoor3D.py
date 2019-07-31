# import necessary module
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pylab import mpl
mpl.rcParams['font.sans-serif'] = ['SimHei']  # 设置字体为黑体
mpl.rcParams['axes.unicode_minus'] = False
data = pd.read_csv(r'E:\paperData\allData\newmk_329.txt', sep='\t')
data1 = pd.read_csv(r'wallline.csv',sep = ',')
data = data[(data.A5 ==3) & (data.trans_pattern==8)]
# data = data[data.A5 ==3]
data.to_csv(r'dt.txt',sep = '\t',index=False)
data =pd.read_csv(r'dt.txt',sep = '\t')
# data = data[data.A5==3]
# x = list(data['X']/10)
# y = list(data['Y']/10)
x = list(data['X'])
y = list(data['Y'])
z = [i for i in range(len(data))]
# new a figure and set it into 3d
fig = plt.figure()
ax = fig.gca(projection='3d')
ax.set_title("室内轨迹",fontsize=20)
# set figure information
ax.set_xlabel("X",fontsize=18)
ax.set_ylabel("Y",fontsize=18)
ax.set_zlabel("时间",fontsize=18)

# draw the figure, the color is r = read
figure1 = ax.plot(x, y, z, c='r',linewidth=1)
for i in range(len(data1)):
    ax.plot([data1['x1'][i]*10,data1['x2'][i]*10],[525-data1['y1'][i]*10,525-data1['y2'][i]*10],c ='b')
# data = pd.read_csv(r'E:\paperData\allData\newmk_328.txt', sep='\t')
# data = data[(data.A5 ==3) & (data.trans_pattern==8)]
# # data = data[data.A5 ==3]
# data.to_csv(r'dt.txt',sep = '\t',index=False)
# data =pd.read_csv(r'dt.txt',sep = '\t')
# x = list(data['X'])
# y = list(data['Y'])
# z = [i for i in range(len(data))]
# figure1 = ax.plot(x, y, z, c='g',linewidth=1)


plt.savefig(r'室内.png')
plt.show()