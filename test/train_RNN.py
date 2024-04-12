
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.models import load_model, save_model

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from TXL import n 
import tensorflow as tf
import csv

loss=[]
#B1: chuẩn bị data
data = pd.read_csv('Book2.csv')

X = (data.iloc[:,3:(n)+3])/100
Y=data['P'].values/100

# #B2 chuẩn bị mô hình AI
model = Sequential()  #tạo mô hình trống
model.add(Dense(20, input_shape = (n,), activation='tanh'))
model.add(Dense(20, activation ='tanh'))             
model.add(Dense(2, activation = "linear"))       
print(model.summary())


#B3 chuẩn bị giải thuật huấn luyện mô hình
model.compile(loss='mse', optimizer='Adam')  



# #B4 huấn luyện mô hình
history=model.fit(X, Y, epochs=1000, batch_size=32)
save_model(model, 'NNmodel_3_P.keras')

# Plotting the loss
plt.plot(history.history['loss'])
plt.title('Model Loss')
plt.ylabel('Loss')
plt.xlabel('Epoch')
plt.show()

print("Huấn luyện lux")
X1 = (data.iloc[:,(n)+4:(n)*2+5])/100
Y1=data['Lux'].values/100
# #B2 chuẩn bị mô hình AI
model = Sequential()  #tạo mô hình trống
model.add(Dense(20, input_shape = (n,), activation='tanh'))
model.add(Dense(20, activation ='tanh'))             
model.add(Dense(2, activation = "linear"))       
print(model.summary())


#B3 chuẩn bị giải thuật huấn luyện mô hình
model.compile(loss='mse', optimizer='Adam')  



# #B4 huấn luyện mô hình
history=model.fit(X1, Y1, epochs=1000, batch_size=32)
save_model(model, 'NNmodel_3_Lux.keras')

# Plotting the loss
plt.plot(history.history['loss'])
plt.title('Model Loss')
plt.ylabel('Loss')
plt.xlabel('Epoch')
plt.show()