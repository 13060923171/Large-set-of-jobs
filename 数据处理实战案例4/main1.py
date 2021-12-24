#生成item_link文件用来后面做区分处理

import pandas as pd
from tqdm import tqdm
from itertools import chain
df = pd.read_csv('rating_new.csv')

uid = list(df.user_new.values)
timedata = list(df.time.values)
iid = list(df.item_new.values)
new_iid = list(df.index)

count = 0
iid_list = []
sum_iid = []

uid_list = []
sum_uid = []

while count+1 < len(iid):
    iid_list.append(iid[count])
    uid_list.append(uid[count])
    while uid[count] == uid[count+1] and timedata[count] == timedata[count+1]:
        iid_list.append(iid[count+1])
        uid_list.append(uid[count+1])
        count += 1
        if count+1 == len(iid):
            break

    sum_iid.append(iid_list)
    sum_uid.append(uid_list)
    iid_list = []
    uid_list = []
    count += 1

sum_iid1 = []
sum_uid1 = []
for u,i in zip(sum_uid,sum_iid):
    if len(u) >= 2 and len(i) >= 2:
        sum_uid1.append(u)
        sum_iid1.append(i)


df = pd.DataFrame()
uid_1 = tqdm(list(chain(*sum_uid1)))
iid_1 = tqdm(list(chain(*sum_iid1)))
df['uid'] = uid_1
df['iid'] = iid_1
df.to_csv('item_link.csv')
# for i in tqdm(range(len(sum_iid))):
#     df['uid'] = sum_uid[i]
#     df['iid'] = sum_iid[i]
#     df.to_csv('item_link.csv',mode='a',index=None,header=None)
#     j = sum_iid[i]
#     j1 = sum_iid[i+1]
#     k = sum_uid[i]
#     k1 = sum_uid[i+1]
#     if k[0] == k1[0]:
#         j2 = j + j1
#         with open('iid_link.txt', 'a', encoding='utf-8')as f:
#             a = ' '.join('%s' % id for id in j2)
#             f.write(a + '\n')