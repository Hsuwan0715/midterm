import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime

usecols = ['發生月', '發生日', '發生時', '發生分', '道路型態', '死亡人數', '2-30日死亡人數', '受傷人數']
df = pd.read_csv("/content/drive/MyDrive/Colab Notebooks/taipei.csv",usecols=usecols)

#temp = list()
#for i in range (len(data)): #取得道路型態的種類，並將其從dataframe型態轉為string型態
#  temp.append([data.at[i,'道路型態']])
#s = set(tuple(l) for l in temp)
#temp = [list(t) for t in s]

#acc_happened_road = list()
#for i in temp:
#  acc_happened_road.append("".join('%s' %id for id in i))

column_names_temp = ['發生月', '發生日', '發生時', '發生分']
df.drop_duplicates(subset=column_names_temp, keep='first', inplace=True) #事故一次會記錄多輛車，去除同起事故的紀錄

df = df.groupby(['道路型態']).sum()
df = df.reset_index(level=0)
df = df.reset_index(level=0)

width=0.25
x1=df['道路型態']
y1=df['受傷人數']
x2=[p + width for p in x1]
y2=(df['死亡人數']+df['2-30日死亡人數'])*100

plt.bar(x1, y1, label='受傷人數', width=0.25)  #繪製長條圖
plt.bar(x2, y2, label='死亡人數', width=0.25)  #繪製長條圖

plt.xticks([p + width for p in x1], x1)        #設定 X 軸刻度標籤
plt.title('taipei traffic')
plt.xlabel('road_type')
plt.ylabel('popularity')
plt.show()
