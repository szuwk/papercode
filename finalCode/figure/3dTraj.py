# import necessary module
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pylab import mpl
mpl.rcParams['font.sans-serif'] = ['SimHei']  # 设置字体为黑体
mpl.rcParams['axes.unicode_minus'] = False
data = pd.read_csv(r'E:\paperData\allData\mk416.txt',sep = '\t',nrows=30000)
# data = data[data.A5==3]
# x = list(data['X']/10)
# y = list(data['Y']/10)
x = list(data['A3'])
y = list(data['A4'])
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
figure1 = ax.plot(x, y, z, c='r')
# figure2 = ax.plot(first_1000, second_1000, third_1000, c='b')
plt.savefig(r'室内轨迹分布图.png')
plt.show()