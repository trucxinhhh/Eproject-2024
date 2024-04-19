
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense,LSTM
from tensorflow.keras.models import load_model, save_model

import matplotlib.pyplot as plt
import pandas as pd
from TXL import *
import tensorflow as tf
import csv
n=282 
loss=[]
#B1: chuẩn bị data
data = pd.read_csv('Book2.csv')

X = (data.iloc[:,3:(n)+3])/100
# print("len(X)",len(X))
X = np.expand_dims(X, axis=1) 
Y=data['P'].values/100
print (Y)
# # #B2 chuẩn bị mô hình AI
model = Sequential()  #tạo mô hình trống
model.add(LSTM(20, input_shape = (None,n), activation='tanh'))
model.add(Dense(20, activation ='tanh'))             
model.add(Dense(1, activation = "linear"))       
print(model.summary())


#B3 chuẩn bị giải thuật huấn luyện mô hình
model.compile(loss='mse', optimizer='Adam')  



# #B4 huấn luyện mô hình
history=model.fit(X, Y, epochs=10000, batch_size=32)
save_model(model, 'NNmodel_13_P.keras')

# Plotting the loss
plt.plot(history.history['loss'])
plt.title('Model Loss')
plt.ylabel('Loss')
plt.xlabel('Epoch')
plt.show()

print("Huấn luyện lux")
X1 = (data.iloc[:,(n)+4:(n)*2+4])/100
X1 = np.expand_dims(X1, axis=1)
Y1=data['Lux'].values/100
# #B2 chuẩn bị mô hình AI
model1 = Sequential()  #tạo mô hình trống
model1.add(LSTM(20, input_shape=(None, n), activation='tanh')) 
model1.add(Dense(10, activation ='tanh'))      
model1.add(Dense(1, activation = "linear"))       
print(model1.summary())


#B3 chuẩn bị giải thuật huấn luyện mô hình
model1.compile(loss='mse', optimizer='Nadam')  



# #B4 huấn luyện mô hình
history=model1.fit(X1, Y1, epochs=10000, batch_size=32)
save_model(model1, 'NNmodel_13_Lux.keras')

# Plotting the loss
plt.plot(history.history['loss'])
plt.title('Model Loss')
plt.ylabel('Loss')
plt.xlabel('Epoch')
plt.show()
