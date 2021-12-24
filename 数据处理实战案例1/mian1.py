import pandas as pd
from tqdm import tqdm
import concurrent.futures

df = pd.read_csv('ratings.csv')
def uid_main():
    list_uid = df.uid.values
    count = 0
    list_count = []
    for i in range(len(list_uid)):
        if list_uid[i-1] == list_uid[i]:
            count = count
            list_count.append(count-1)
        else:
            count += 1
            list_count.append(count-1)

    with open('user_list.txt','w',encoding='utf-8')as f:
        f.write('uid id'+'\n')

    for i in range(len(list_uid)):
        if list_uid[i - 1] != list_uid[i]:
            with open('user_list.txt', 'a', encoding='utf-8')as f:
                a = str(list_uid[i]) + " " + str(list_count[i])
                f.write(a+'\n')


def iid_main():
    list_iid = list(df.iid.values)
    count = 0
    list_count = []
    l2 = list(set(list_iid))
    l2.sort(key=list_iid.index)
    for i in l2:
        list_count.append(count)
        count += 1
    with open('item_list.txt','w',encoding='utf-8')as f:
        f.write('iid id'+'\n')

    for i in tqdm(range(len(l2))):
        with open('item_list.txt', 'a', encoding='utf-8')as f:
            a = ' '.join([str(l2[i]),str(list_count[i])])
            f.write(a+'\n')

iid_main()

# #多进程
# with concurrent.futures.ThreadPoolExecutor(max_workers=10)as e:
#     futuers = [e.submit(iid_main)]
#     for futuer in concurrent.futures.as_completed(futuers):
#         print(futuer.result())
