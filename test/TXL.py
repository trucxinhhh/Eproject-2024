import numpy as np
import pandas as pd
import csv

data =pd.read_csv('R:/DuAn/THI/eproject_2024/file_A_test.csv')
time1 = data['localtime'] 

P=data.iloc[:,4:5].values
# lux=data.iloc[:,5:6].values
lux=data.iloc[:,3:4].values
print("nhap so ngo vao")
n=int((input()))
df=pd.DataFrame(time1,columns=['localtime'])

df['P']=P
for i in range(1,n+1):
    df[i]=((df['P'].shift(periods=i)))
df['Lux']=lux
for j in range(1,n+1):
    df[j+n]=((df['Lux'].shift(periods=j)))
# df['U']=U
# for m in range(1,n+1):
#     df[m+2*n]=((df['U'].shift(periods=m)))

data_final=df.dropna()

data_final.to_csv('Book2.csv')