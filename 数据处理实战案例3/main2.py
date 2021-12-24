import pandas as pd
import numpy as np
import threading
from tqdm import tqdm

# total=pd.read_table('Gowalla_totalCheckins.txt',sep='\t',header=None)     #读入txt文件，分隔符为\t
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
# userid = list(total[0].values)
# itemid = list(total[4].values)


def get_date():
    count = 0
    itemid_list = []
    sum_itemid = []

    userid_list = []
    sum_userid = []

    while count+1 < len(itemid):
        itemid_list.append(itemid[count])
        userid_list.append(userid[count])
        while userid[count] == userid[count+1]:
            itemid_list.append(itemid[count+1])
            userid_list.append(userid[count + 1])
            count += 1
            if count+1 == len(itemid):
                break

        sum_itemid.append(itemid_list)
        sum_userid.append(userid_list)
        itemid_list = []
        userid_list = []
        count += 1

    return sum_itemid,sum_userid

def txt_itemid(sum_itemid):
    count = 0
    for s in sum_itemid:
        if len(s) >= 20:
            for i in s:
                with open('item_list.txt', 'a', encoding='utf-8')as f:
                    a = str(i) + " " + str(count)
                    f.write(a + '\n')
                    count += 1


def txt_userid(sum_userid):
    count = 0
    for s in sum_userid:
        if len(s) >= 20:
            with open('userid_list.txt', 'a', encoding='utf-8')as f:
                a = str(s[0]) + " " + str(count)
                f.write(a + '\n')
                count += 1
                print(count)


if __name__ == '__main__':
    with open('item_list.txt', 'w', encoding='utf-8')as f:
        f.write('itemid new_itemid' + '\n')

    with open('userid_list.txt', 'w', encoding='utf-8')as f:
        f.write('userid new_userid' + '\n')

    sum_itemid, sum_userid = get_date()
    thread1 = threading.Thread(target=txt_userid,args=(sum_userid,))
    thread1.start()
    thread2 = threading.Thread(target=txt_itemid, args=(sum_itemid,))
    thread2.start()
    # txt_itemid(sum_itemid[0:100])
    # txt_userid(sum_userid[0:100])

