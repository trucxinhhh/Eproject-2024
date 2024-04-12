import json
import pandas as pd

from urllib import request, parse
from time import sleep
import json

def get_file_A():
    req=request.Request("http://rockwell.eproject.kienlab.com/api/raw?dev_id=D4:8A:FC:A5:ED:E0&length=-10000")
    r = request.urlopen(req)
    respone_data=r.read().decode()
    respone_data=json.loads(respone_data)
    df = pd.DataFrame(respone_data)
    return df

def get_file_B():
    req=request.Request("http://rockwell.eproject.kienlab.com/api/raw?dev_id=D4:8A:FC:99:66:68&length=-10000")
    r = request.urlopen(req)
    respone_data=r.read().decode()
    respone_data=json.loads(respone_data)
    df = pd.DataFrame(respone_data)
    return df

df_A = get_file_A()
df_B = get_file_B()

# Ghi hai DataFrame vào hai file CSV
df_A.to_csv('file_A_test.csv', index=False)
df_B.to_csv('file_B_test.csv', index=False)
