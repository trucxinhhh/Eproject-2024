from cProfile import label
from tensorflow.keras.models import load_model
import numpy as np
import pandas as pd

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import matplotlib.pyplot as plt

n=1128
data1 = pd.read_csv('file_A_test_1.csv')


model_P= load_model('NNmodel_2_P.keras')
model_Lux= load_model('NNmodel_2_Lux.keras')


Yp=(data1['P'].iloc[-n-1:-1]/100).to_list()
Yl=(data1['lux'].iloc[-n-1:-1]/100).to_list()


Y1= pd.DataFrame(Yp[::-1]).transpose()
Y2= pd.DataFrame(Yl[::-1]).transpose()

Y_final_P= []
Y_final_L= []

for i in range (n):
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


