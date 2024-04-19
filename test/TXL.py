import numpy as np
import pandas as pd
import csv
from datetime import datetime, timedelta
from pandas import DataFrame, concat
import time
data =pd.read_csv('R:/DuAn/THI/eproject_2024/file_A_test_2.csv')
# time1 = data['localtime'] 
data['localtime'] = [t.replace('.000Z', 'Z') for t in data['localtime'].astype(str)]
times_shifted = pd.to_datetime(data['localtime'].shift(1))
# pd.to_datetime(shifted) - pd.to_datetime(data['localtime'])
times = pd.to_datetime(data['localtime'])
delta_times = (times - times_shifted)
error_index_append=delta_times.index[(delta_times>= timedelta(minutes=6))].tolist()
error_index_delete=delta_times.index[delta_times>= timedelta(minutes=15)].tolist()

print(error_index_append)
print(error_index_delete)

for i in error_index_delete: 
    data.loc[i] =np.nan
    # print(data.head(i+3))
    # time.sleep(50)
    for j in error_index_append: 
        if i == j : 
            rm_index=error_index_append.index(j)
            error_index_append.remove(error_index_append[rm_index])



P=data.iloc[:,4:5].values
lux=data.iloc[:,5:6].values
df=pd.DataFrame(times,columns=['localtime'])
df['P']=P
df['Lux']=lux

for m in error_index_append: 
    pavg = (df['P'][m] + df['P'][m-1])/2
    luxavg = (df['Lux'][m] + df['Lux'][m-1])/2
    df0=pd.DataFrame({'P':[pavg], 'Lux': [luxavg], 'localtime':[0] })
    df = pd.concat([df.iloc[:m], df0, df.iloc[m:]]).reset_index(drop=True)
    # print(df.head(m+3))
    # time.sleep(5)
# df=df.fillna(0)
# print(df.head(60))
print("nhap so ngo vao")
n=int((input()))

df2 = pd.DataFrame(times,columns=['localtime'])
df2['P']=df['P']

for i in range(1,n+1):
    df2[i]=((df2['P'].shift(periods=i)))
df2['Lux']=df['Lux']
for j in range(1,n+1):
    df2[j+n]=((df2['Lux'].shift(periods=j)))
# df['U']=U
# for m in range(1,n+1):
#     df[m+2*n]=((df['U'].shift(periods=m)))

data_final=df2.dropna()
df2.to_csv("Book1.csv")
data_final.to_csv('Book2.csv')
