#用于生成user.txt文件和item.txt文件

import pandas as pd
from tqdm import tqdm


def shengcheng_user():
    df = pd.read_csv('user_link_map.csv')
    user_x = list(df.user_new_x.values)
    user_y = list(df.user_new_y.values)

    uid_list = []
    sum_uid = []
    count = 0
    iid_list = []
    sum_iid = []

    while count + 1 < len(user_y):
        iid_list.append(user_y[count])
        uid_list.append(user_x[count])
        while user_x[count] == user_x[count + 1]:
            iid_list.append(user_y[count + 1])
            uid_list.append(user_x[count + 1])
            count += 1
            if count + 1 == len(user_y):
                break

        sum_iid.append(iid_list)
        sum_uid.append(uid_list)
        iid_list = []
        uid_list = []
        count += 1

    def read_list(list1):
        for i in list1:
            list1.remove(i)
            list1.insert(0, i)
            with open('user.txt', 'a', encoding='utf-8')as f:
                a = ' '.join('%s' % id for id in list1)
                f.write(a + '\n')



    for i in tqdm(sum_iid):
        read_list(i)

    # list_target = []
    # for c in tqdm(sum_uid):
    #     target = (c[0])
    #     list_target.append(target)
    #
    # for t, s in zip(list_target, sum_iid):
    #     a = s.insert(0, t)
    #     with open('user.txt', 'a', encoding='utf-8')as f:
    #         a = ' '.join('%s' % id for id in s)
    #         f.write(a + '\n')

def shengcheng_item():
    df = pd.read_csv('item_link.csv')
    user_x = list(df.uid.values)
    user_y = list(df.iid.values)

    uid_list = []
    sum_uid = []
    count = 0
    iid_list = []
    sum_iid = []

    while count + 1 < len(user_y):
        iid_list.append(user_y[count])
        uid_list.append(user_x[count])
        while user_x[count] == user_x[count + 1]:
            iid_list.append(user_y[count + 1])
            uid_list.append(user_x[count + 1])
            count += 1
            if count + 1 == len(user_y):
                break
        sum_uid.append(uid_list)
        sum_iid.append(iid_list)
        iid_list = []
        uid_list = []
        count += 1

    def read_list(list1):
        for i in list1:
            list1.remove(i)
            list1.insert(0, i)
            with open('item.txt', 'a', encoding='utf-8')as f:
                a = ' '.join('%s' % id for id in list1)
                f.write(a + '\n')

    for i in tqdm(sum_iid):
        read_list(i)
    # list_target = []
    # for c in tqdm(sum_uid):
    #     target = (c[0])
    #     list_target.append(target)

    # for t,s in zip(list_target,sum_iid):
    #     a = s.insert(0, t)
    #     with open('item.txt', 'a', encoding='utf-8')as f:
    #         a = ' '.join('%s' % id for id in s)
    #         f.write(a + '\n')


if __name__ == '__main__':
    shengcheng_user()
    # shengcheng_item()