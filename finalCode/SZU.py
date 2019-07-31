import pandas as pd
data =pd.read_csv(r'E:\addData\zth_0412.txt',sep = '\t')
data = data[['time','Long','Lat']]
data.to_csv(r'E:\mapData\zth_0412.csv',sep = ',')