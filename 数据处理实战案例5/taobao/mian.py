import pandas as pd
from tqdm import tqdm


#生成train和test文件
df = pd.read_csv('rating.csv')


uid = list(df.user.values)
iid = list(df.item.values)

count = 0
iid_list = []
sum_iid = []

uid_list = []
sum_uid = []

while count+1 < len(iid):
    iid_list.append(iid[count])
    uid_list.append(uid[count])
    while uid[count] == uid[count+1]:
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


list_target = []
list_80 = []
list_20 = []
for c in tqdm(sum_uid):
    target = (c[0])
    list_target.append(target)
for c in tqdm(sum_iid):
    neirong = c
    bai_80 = int(len(neirong) * 0.8)
    nei_80 = neirong[:bai_80]
    list_80.append(nei_80)
    nei_20 = neirong[bai_80:]
    list_20.append(nei_20)

for i,o,p in zip(list_target,list_80,list_20):
    a = o.insert(0,i)
    b = p.insert(0,i)
    with open('train.txt','a',encoding='utf-8')as f:
        c = ' '.join('%s' % id for id in o)
        f.write(c+'\n')
    with open('test.txt','a',encoding='utf-8')as f:
        d = ' '.join('%s' % id for id in p)
        f.write(d+'\n')