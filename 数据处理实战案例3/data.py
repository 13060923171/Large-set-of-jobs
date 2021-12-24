from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
from tqdm import tqdm
total=pd.read_table('Gowalla_totalCheckins.txt',sep='\t',header=None)     #读入txt文件，分隔符为\t

def time_str(x):
    x = str(x)
    x = x.split('T')
    return x[0]

total[1] = total[1].apply(time_str)

print(total.head())
with open('new_Gowalla_totalCheckins.txt', 'w', encoding='utf-8')as f:
    f.write('userid timedate itemid' + '\n')
for t in tqdm(range(len(total[1]))):
    if str(total[1][t]) >= '2010-10':
        with open('new_Gowalla_totalCheckins.txt', 'a', encoding='utf-8')as f:
            a = str(total[0][t]) + " " + str(total[1][t]) + " " + str(total[4][t])
            f.write(a + '\n')

# train_x,test_x,train_y,test_y = train_test_split(total[[0,1]].values,total[4].values,test_size=0.95)



# for i,j in tqdm(zip(train_x,train_y)):
#     with open('new_Gowalla_totalCheckins.txt', 'a', encoding='utf-8')as f:
#         a = str(i[0]) + " " + str(i[1]) + " " + str(j)
#         f.write(a + '\n')

