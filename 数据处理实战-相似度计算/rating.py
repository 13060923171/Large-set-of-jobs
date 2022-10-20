import pandas as pd     #引入pandas包

train = pd.read_table('train.txt',sep='\t',header=None)
test = pd.read_table('test.txt',sep='\t',header=None)


def main1(x):
    x1 = str(x).split(' ')
    x1 = x1[1:]
    x2 = ' '.join(x1)
    return x2


train[0] = train[0].apply(main1)
test[0] = test[0].apply(main1)


df1 = pd.DataFrame()
df1['用户ID'] = list(train.index)
df1['values1'] = list(train[0])


df2 = pd.DataFrame()
df2['用户ID'] = list(test.index)
df2['values2'] = list(test[0])

result = pd.merge(df1, df2, on='用户ID')

result['物品ID'] = result['values1'] + " " + result['values2']
result = result.drop(['values1','values2'],axis=1)


def main2(x):
    x = str(x).split(' ')
    return len(x)


result['len'] = result['物品ID'].apply(main2)

new_df = result[result['len'] >= 20]
new_df = new_df.drop(['len'],axis=1)
new_df.to_csv('rating.csv',index=False)