import pandas as pd
from tqdm import tqdm

def shengcheng_user():
    df = pd.read_csv('user1.csv')
    user_x = list(df.user.values)
    user_y = list(df.gender.values)
    user_z = list(df.age_level.values)

    user_list = []
    sum_user = []

    count = 0

    gender_list = []
    sum_gender = []

    age_level_list = []
    sum_age_level = []

    while count + 1 < len(user_y):
        gender_list.append(user_y[count])
        user_list.append(user_x[count])
        age_level_list.append(user_z[count])
        while user_y[count] == user_y[count + 1] and user_z[count] == user_z[count + 1]:
            gender_list.append(user_y[count +1])
            user_list.append(user_x[count +1])
            age_level_list.append(user_z[count +1])
            count += 1
            if count + 1 == len(user_y):
                break
        sum_user.append(user_list)
        sum_gender.append(gender_list)
        sum_age_level.append(age_level_list)
        user_list = []
        gender_list = []
        age_level_list = []
        count += 1

    def read_list(list1):
        for i in list1:
            list1.remove(i)
            list1.insert(0, i)
            with open('user.txt', 'a', encoding='utf-8')as f:
                a = ' '.join('%s' % id for id in list1)
                f.write(a + '\n')

    sum_user1 = []
    for u in sum_user:
        if len(u) >= 2:
            sum_user1.append(u)


    for i in tqdm(sum_user1):
        read_list(i)


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
    # df = pd.read_csv('user.csv')
    # df.drop_duplicates(inplace=True)
    # df.to_csv('user1.csv',index=None)
    # shengcheng_user()
    shengcheng_item()