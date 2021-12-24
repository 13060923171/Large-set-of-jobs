import pandas as pd
from tqdm import tqdm

def shengcheng_user():
    df = pd.read_csv('user.csv')
    user_x = list(df.user_target.values)
    user_y = list(df.user_neighbor.values)

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


    list_target = []
    for c in tqdm(sum_uid):
        target = (c[0])
        list_target.append(target)

    for t, s in zip(list_target, sum_iid):
        a = s.insert(0, t)
        with open('user.txt', 'a', encoding='utf-8')as f:
            a = ' '.join('%s' % id for id in s)
            f.write(a + '\n')


def shengcheng_item():
    df = pd.read_csv('item.csv')
    user_x = list(df.item.values)
    user_y = list(df.category.values)

    uid_list = []
    sum_uid = []
    count = 0
    iid_list = []
    sum_iid = []

    while count + 1 < len(user_y):
        iid_list.append(user_y[count])
        uid_list.append(user_x[count])
        while user_y[count] == user_y[count + 1]:
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
            with open('item.txt', 'a', encoding='utf-8')as f:
                a = ' '.join('%s' % id for id in list1)
                f.write(a + '\n')

    sum_iid1 = []
    sum_uid1 = []
    for u, i in zip(sum_uid, sum_iid):
        if len(u) >= 2 and len(i) >= 2:
            sum_uid1.append(u)
            sum_iid1.append(i)

    for i in tqdm(sum_uid1):
        read_list(i)



if __name__ == '__main__':
    # shengcheng_user()
    shengcheng_item()