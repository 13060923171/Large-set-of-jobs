import pandas as pd
from tqdm import tqdm
df1 = pd.read_csv('rating.csv')

list1 = []
for i in df1['物品ID']:
    str1 = str(i).split(' ')
    for s in str1:
        list1.append(int(s))

list2 = list(set(list1))


df2 = pd.DataFrame()
df2['物品ID'] = ['物品ID']
df2['用户ID'] = ['用户ID']
df2.to_csv('rating2.csv',encoding='utf-8-sig',mode='w',index=False,header=False)


for l in tqdm(list2):
    use_id = []
    for j,k in zip(df1['用户ID'],df1['物品ID']):
        k1 = str(k).split(' ')
        k1 = list(map(int, k1))
        if l in k1:
            use_id.append(str(j))
    df2['物品ID'] = [l]
    df2['用户ID'] = [' '.join(use_id)]
    df2.to_csv('rating2.csv', encoding='utf-8-sig', mode='a+', index=False, header=False)

