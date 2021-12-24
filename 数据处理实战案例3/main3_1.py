import pandas as pd
import numpy as np
import concurrent.futures
from tqdm import tqdm

user=pd.read_csv('Gowalla_item_edges.csv')     #读入txt文件，分隔符为\t
user.dropna(axis=0,how='any',inplace=True)

user1 = list(user['316637'])
user2 = list(user['16516'])



user_list=pd.read_table('item_list.txt',sep='\t')



def get_user(j,k):
    with open('item_list.txt', 'r')as f:
        content = f.readlines()
    dict1 = {}
    for c in content[1:]:
        c = c.strip('\n')
        c = c.split(" ")
        dict1[c[0]] = c[1]



    def dict_main(i):
        for key, value in dict1.items():
            if str(key) == str(i):
                return int(value)



    target1 = dict_main(j)
    target2 = dict_main(k)
    return target1,target2



def write_txt():
    new_target1 = []
    new_target2 = []
    for j,k in tqdm(zip(user1,user2)):
        # print(j,int(k))
        target1,target2 = get_user(j,int(k))
        if target1 != None and target2 != None:
            new_target1.append(target1)
            new_target2.append(target2)

    for j,k in tqdm(zip(new_target1,new_target2)):
        with open('item.txt', 'a', encoding='utf-8')as f:
            a = str(j) + " " + str(k)
            f.write(a + '\n')


if __name__ == '__main__':
    with open('item.txt', 'w', encoding='utf-8')as f:
        f.write('item1 item2' + '\n')
    write_txt()
