from cProfile import label
from tensorflow.keras.models import load_model
import numpy as np
import pandas as pd
import datetime
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import matplotlib.pyplot as plt
from time import sleep
n=282
data1 = pd.read_csv('file_A_test_3.csv')


model_P= load_model('NNmodel_12_P.keras')
model_Lux= load_model('NNmodel_12_Lux.keras')

start_time = datetime.datetime.now()
Yp=(data1['P'].iloc[-n-1:-1]/100).to_list()
Yl=(data1['lux'].iloc[-n-1:-1]/100).to_list()

# Yp['time'] = data1['localtime'].iloc[-n-1:-1].values

# Yp=(data1['P'].iloc[(-n-1)-n+10:-n+108]/100).to_list()
# Yl=(data1['lux'].iloc[(-n-1)-n+10:-n+108]/100).to_list()
# Yp['localtime'] =  data1['localtime'].iloc[(-n-1)-n+10:-n+108].values
# Yp.info()
# Yp.to_csv("Yp.csv")
Y1= pd.DataFrame(Yp[::-1]).transpose()
Y2= pd.DataFrame(Yl[::-1]).transpose()
print(len(Yp))
print(len(Yl))

# df1 = pd.DataFrame(Yp)
# df1['time'] = data1['localtime'].iloc[(-n-1)-n+10:-n+10].values
# df1.to_csv("AAA.csv")

Y_final_P= []
Y_final_L= []

for i in range (n):
    Y1 = np.expand_dims(Y1, axis=1) 
    Y2 = np.expand_dims(Y2, axis=1) 
    Y1_P = float(model_P.predict(Y1)*100)
    Y2_P = float(model_Lux.predict(Y2)*100)     

    if Y1_P < 5 : 
        Y1_P=0
    if Y2_P < 0 : 
        Y2_P=0
    Y_final_P.append(Y1_P)
    Y_final_L.append(Y2_P)

    Yp.append(Y1_P/100)
    Yl.append(Y2_P/100)

    del Yp[0]
    del Yl[0]

    Y1= pd.DataFrame(Yp[::-1]).transpose()
    Y2= pd.DataFrame(Yl[::-1]).transpose()

df = pd.DataFrame(Y_final_P)
df1 = pd.DataFrame(Y_final_L)

df.to_csv("Y_final_P.csv")
df1.to_csv("Y_final_L.csv")

end_time = datetime.datetime.now()
print(end_time-start_time)
