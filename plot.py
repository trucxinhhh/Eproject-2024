import pandas as pd
import matplotlib.pyplot as plt
n=282
# Đọc dữ liệu từ file CSV
# data = pd.read_csv('file_A_test.csv')
df = pd.read_csv('Y_final.csv')

# Lấy dữ liệu từ cột đó
# column_data = data['P'].iloc[-n-1:-1]
column_data = df['0'].iloc[:480]


# Vẽ đồ thị
plt.plot(column_data)
plt.xlabel('Chỉ số')
plt.ylabel('Giá trị')
# plt.title('')
plt.show()
