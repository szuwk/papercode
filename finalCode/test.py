# -*- coding:utf-8 -*-
# 卡尔曼滤波算法
import pandas as pd
import numpy as np
class kalman_filter:
    def __init__(self, Q, R):
        self.Q = Q
        self.R = R

        self.P_k_k1 = 1
        self.Kg = 0
        self.P_k1_k1 = 1
        self.x_k_k1 = 0
        self.ADC_OLD_Value = 0
        self.Z_k = 0
        self.kalman_adc_old = 0

    def kalman(self, ADC_Value):

        self.Z_k = ADC_Value

        if (abs(self.kalman_adc_old - ADC_Value) >= 60):
            self.x_k1_k1 = ADC_Value * 0.382 + self.kalman_adc_old * 0.618
        else:
            self.x_k1_k1 = self.kalman_adc_old;

        self.x_k_k1 = self.x_k1_k1
        self.P_k_k1 = self.P_k1_k1 + self.Q

        self.Kg = self.P_k_k1 / (self.P_k_k1 + self.R)

        kalman_adc = self.x_k_k1 + self.Kg * (self.Z_k - self.kalman_adc_old)
        self.P_k1_k1 = (1 - self.Kg) * self.P_k_k1
        self.P_k_k1 = self.P_k1_k1

        self.kalman_adc_old = kalman_adc

        return kalman_adc

data1 = pd.read_csv(r'F:\zky\NEW20171106150539_Data.txt', sep='\t')
data = data1[data1.X != 0]
kalman_filter = kalman_filter(0.001, 0.1)
s = np.random.normal(0, 10, len(data))
x = list(data['X'])
y = list(data['Y'])
print(len(x), len(s))
test_array_x = s + x
test_array_y = s + y
adc_x = []
adc_y = []
# print(test_array_x)
for i in range(len(data)):
    adc_y.append(kalman_filter.kalman(test_array_y[i]) / 10)
for i in range(len(data)):
    adc_x.append(kalman_filter.kalman(test_array_x[i]) / 10)
data['new_x'] = adc_x
data['new_y'] = adc_y
import matplotlib.pyplot as plt
import pandas as pd
# import plotly
# import plotly.graph_objs as go
import numpy

def ScatterLIne(data):

    # plt.scatter([i for i in range(len(data[data.X != 0]))], data['new_x'], s=10, label='X')
    # plt.scatter([i for i in range(len(data[data.Y != 0]))], data['Y'], s=10, label='Y')
    plt.plot([i for i in range(len(data[data.X != 0]))], data['new_y'],  label='X')
    plt.xlabel('time')
    plt.ylabel('Y')
    # plt.legend()
    plt.show()
    plt.savefig('a')
ScatterLIne(data)