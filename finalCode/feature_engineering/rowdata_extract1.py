import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['simHei']
plt.rcParams['axes.unicode_minus'] = False
import datetime
start_time = datetime.datetime.now()
print(start_time)
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

def convert(data1,data2):
    data1.columns = ['Time','Long','Lat','X','Y','Ax','Ay','Az','time']
    data1['A1'] = data2['X_1']
    data1['A2'] = data2['Y_1']
    A3 = []
    A4 = []
    for i in range(len(data1)):
        if data1['X'][i] == 0 and data1['Y'][i] == 0:
            A3.append(data1['A1'][i])
            A4.append(data1['A2'][i])
        else:
            A3.append(data1['X'][i]/10 + 493342.6152)
            A4.append(data1['Y'][i]/10 + 2493102.4037)
    data1['A3'] = A3
    data1['A4'] = A4
    zhuangtai = []
    for i in range(len(data1)):
        if ((data1['X'][i] == 0) & (data1['Y'][i] == 0)) & ((data1['Long'][i] != 0) & (data1['Lat'][i] != 0)):
            zhuangtai.append(1)
        elif ((data1['X'][i] != 0) & (data1['Y'][i] != 0)) & ((data1['Long'][i] == 0) & (data1['Lat'][i] == 0)):
            zhuangtai.append(2)
        elif ((data1['X'][i] != 0) & (data1['Y'][i] != 0)) & ((data1['Long'][i] != 0) & (data1['Lat'][i] != 0)):
            zhuangtai.append(3)
        else:
            zhuangtai.append(4)
    data1['A5'] = zhuangtai
    return  data1
data1 = pd.read_csv(r'E:\Data\preprocessedData\ztt\New20180423123529_Data.txt',sep = '\t')
data2 = pd.read_csv(r'E:\Data\preprocessedData\ztt\ztt_0423.txt',sep = ',')
data = convert(data1,data2)
data.to_csv(r'E:\Data\preprocessedData\ztt\ztt_423.txt',sep = '\t',index=False)