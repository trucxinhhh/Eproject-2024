import pandas as pd
import matplotlib.pyplot as plt
n=1128
# Đọc dữ liệu từ file CSV
data = pd.read_csv('file_A_test_3.csv')
# df = pd.read_csv('Y_final_P.csv')
df = pd.read_csv('Y_final_L.csv')



Y = data['lux'].iloc[-n-1:-1].values
# Y = data['P'].iloc[-n-1:-1].values
Y2 = df['0'].iloc[-n-1:-1].values
# # Y = data['P'].values
# # Y2 = df['0'].values

print(len(Y2))
print(len(Y))
# Vẽ đồ thị
plt.plot(Y,"b",label= "Thực tế", linewidth=1)
plt.plot(Y2,"r--",label="Dự đoán",linewidth=2)
plt.show()
