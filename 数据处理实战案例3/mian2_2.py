import pandas as pd
from tqdm import tqdm
import threading
import concurrent.futures

with open('new_Gowalla_totalCheckins.txt', 'r')as f:
    content = f.readlines()

userid = []
timedata = []
itemid = []
for c in content[1:]:
    c = c.strip('\n')
    c = c.split(" ")
    userid.append(c[0])
    timedata.append(c[1])
    itemid.append(c[2])


def userid_list():
    with open('userid_list.txt','r',encoding='utf-8')as f:
        content = f.readlines()
    dict1 = {}
    for c in content[1:]:

        c = str(c)
        c = c.strip('\n')
        c = c.split(' ')
        dict1[c[0]] = c[1]

    def dict_main(i):
        for key, value in dict1.items():
            if str(key) == str(i):
                return int(value)

    new_target = []
    for i in tqdm(userid):
        target1 = dict_main(i)
        new_target.append(target1)

    return new_target


def item_list():
    with open('item_list.txt', 'r', encoding='utf-8')as f:
        content = f.readlines()
    dict1 = {}
    for c in content[1:]:
        c = str(c)
        c = c.strip('\n')
        c = c.split(' ')
        dict1[c[0]] = c[1]



    def dict_main(i):
        for key, value in dict1.items():
            if str(key) == str(i):
                return int(value)

    new_target = []
    for i in tqdm(itemid):
        target1 = dict_main(i)
        new_target.append(target1)

    return new_target


# def pool_thread():
    # with concurrent.futures.ThreadPoolExecutor(max_workers=8)as e:
    #     # 调用这个函数，用一个列表的形式把这个函数给保存下来
    #     userid2 = [e.submit(userid_list,s) for s in tqdm(userid)]
    #     # 用叠带把这个函数的内容一个个打印出来
    #     for futuer in concurrent.futures.as_completed(userid2):
    #         print(futuer.result())
    #     itemid2 = [e.submit(item_list, s) for s in tqdm(itemid)]
    #     for futuer in concurrent.futures.as_completed(itemid2):
    #         print(futuer.result())
    #     return userid2,itemid2
    # for j,k in zip(userid,itemid):
    #     userid1 = userid_list(j)
    #     itemid1 = item_list(k)


if __name__ == '__main__':
    userid1 = userid_list()
    itemid1 = item_list()
    # userid1, itemid1 = pool_thread()
    count = 0
    itemid_list = []
    sum_itemid = []

    userid_list = []
    sum_userid = []

    while count + 1 < len(itemid1):
        itemid_list.append(itemid1[count])
        userid_list.append(userid1[count])
        while userid1[count] == userid1[count + 1]:
            itemid_list.append(itemid1[count + 1])
            userid_list.append(userid1[count + 1])
            count += 1
            if count + 1 == len(itemid1):
                break
        # if len(itemid_list) >= 20:
        sum_itemid.append(itemid_list)
        sum_userid.append(userid_list)
        itemid_list = []
        userid_list = []
        count += 1

    for i, j in tqdm(zip(sum_userid, sum_itemid)):
        if len(i) >= 20:
            with open('rating.txt', 'a', encoding='utf-8')as f:
                j.insert(0, i[0])
                a = ' '.join('%s' % id for id in j)
                f.write(a + '\n')