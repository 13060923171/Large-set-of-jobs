import pandas as pd
from sklearn.preprocessing import OneHotEncoder, LabelEncoder
import itertools
import numpy as np
from tqdm import tqdm
from numba import jit
import time
import concurrent.futures
from scipy import spatial

df1 = pd.read_csv('rating2.csv').iloc[15486:]

df2 = pd.DataFrame()
# df2['item_id1'] = ['item_id1']
# df2['item_id2'] = ['item_id2']
# df2['相似度'] = ['相似度']
# df2.to_csv('item.csv',encoding='utf-8-sig',mode='w',index=False,header=False)

@jit()
def jit_monte_carlo_pi():
    for j,k in tqdm(zip(df1['物品ID'],df1['用户ID'])):
        for i,o in zip(df1['物品ID'],df1['用户ID']):

            vec1 = str(k).split(' ')
            vec1 = list(map(int, vec1))
            vec2 = str(o).split(' ')
            vec2 = list(map(int, vec2))
            if len(vec1) == len(vec2):
                cos_sim = 1 - spatial.distance.cosine(vec1, vec2)
            else:
                cos_sim = 0
            if cos_sim > 0.7 and j != i:
                df2['item_id1'] = [j]
                df2['item_id2'] = [i]
                df2['相似度'] = [cos_sim]
                df2.to_csv('item.csv', encoding='utf-8-sig', mode='a+', index=False, header=False)
            else:
                pass


if __name__ == '__main__':
    jit_monte_carlo_pi()



