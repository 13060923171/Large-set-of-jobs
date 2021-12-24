import pandas as pd
from tqdm import tqdm

def uid_list():
    with open('user_list.txt','r',encoding='utf-8')as f:
        content = f.readlines()
    dict1 = {}
    for c in content[1:]:

        c = str(c)
        c = c.strip('\n')
        c = c.split(' ')
        dict1[c[0]] = c[1]

    df = pd.read_csv('ratings.csv')
    uid = list(df.uid.values)
    def dict_main(i):
        for key, value in dict1.items():
            if str(key) == str(i):
                return int(value)
    new_target = []
    for i in tqdm(uid):
        target1 = dict_main(i)
        new_target.append(target1)

    return new_target


def iid_list():
    with open('item_list.txt', 'r', encoding='utf-8')as f:
        content = f.readlines()
    dict1 = {}
    for c in content[1:]:
        c = str(c)
        c = c.strip('\n')
        c = c.split(' ')
        dict1[c[0]] = c[1]

    df = pd.read_csv('ratings.csv')
    uid = list(df.iid.values)

    def dict_main(i):
        for key, value in dict1.items():
            if str(key) == str(i):
                return int(value)

    new_target = []
    for i in tqdm(uid):
        target1 = dict_main(i)
        new_target.append(target1)

    return new_target



list_uid = uid_list()
list_iid = iid_list()

list_uid1 = []
list_iid1 = []
list_uid2 = []
list_iid2 = []
count = 0


while count+1 < len(list_uid):
    list_uid1.append(list_uid[count])
    list_iid1.append(list_iid[count])
    while list_uid[count] == list_uid[count+1]:
        list_uid1.append(list_uid[count+1])
        list_iid1.append(list_iid[count + 1])
        count += 1
        if count+1 == len(list_uid):
            break
    list_uid2.append(list_uid1)
    list_iid2.append(list_iid1)

    list_uid1 = []
    list_iid1 = []
    count += 1

for i,j in tqdm(zip(list_uid2,list_iid2)):
    with open('rating.txt','a',encoding='utf-8')as f:
        j.insert(0,i[0])
        a = ' '.join('%s' %id for id in j)
        f.write(a+'\n')