import pandas as pd
import numpy as np
import concurrent.futures
from tqdm import tqdm
# user=pd.read_table('Gowalla_user_edges.txt',sep='\t',header=None)     #读入txt文件，分隔符为\t
# total=pd.read_table('new_Gowalla_totalCheckins.txt',sep='\t',header=None)     #读入txt文件，分隔符为\t
# print(total)
# # def time_str(x):
# #     x = str(x)
# #     x = x.split('T')
# #     return x[0]
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

# # total[1] = total[1].apply(time_str)
# userid = list(total.userid)
# print(userid)
# timedata = list(total[1].values)
# itemid = list(total[4].values)


def get_csv():
    count = 0
    itemid_list = []
    sum_itemid = []


    while count+1 < len(itemid):
        itemid_list.append(itemid[count])
        while userid[count] == userid[count+1] and timedata[count] == timedata[count+1]:
            itemid_list.append(itemid[count+1])
            count += 1
            if count+1 == len(itemid):
                break
        sum_itemid.append(itemid_list)
        itemid_list = []
        count += 1
    return sum_itemid


def write_csv(s):
    df = pd.DataFrame()
    # for s in tqdm(sum_itemid):
    if len(s) >=2:
        n = 2
        a = [s[i:i + n] for i in range(0, len(s), n)]
        for i in a:
            if len(i) == 2:
                df['item1'] = [i[0]]
                df['item2'] = [i[1]]
                df.to_csv('Gowalla_item_edges.csv',mode='a',encoding='utf-8',index=None,header=None)
            else:
                df['item1'] = [i[0]]
                df['item2'] = None
                df.to_csv('Gowalla_item_edges.csv', mode='a', encoding='utf-8', index=None,header=None)


def pool_thread():
    sum_itemid = get_csv()
    with concurrent.futures.ThreadPoolExecutor(max_workers=10)as e:
        # 调用这个函数，用一个列表的形式把这个函数给保存下来
        futuers = [e.submit(write_csv,s) for s in tqdm(sum_itemid)]
        # 用叠带把这个函数的内容一个个打印出来
        for futuer in concurrent.futures.as_completed(futuers):
            print(futuer.result())


if __name__ == '__main__':
    # get_csv(userid, timedata, itemid)
    pool_thread()
    # sum_itemid = get_csv()
    # for s in tqdm(sum_itemid):
    #     write_csv(s)