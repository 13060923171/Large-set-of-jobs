import pandas as pd
from tqdm import tqdm


def user():
    with open('user_list.txt', 'r')as f:
        content = f.readlines()
    dict1 = {}
    for c in content[1:]:
        c = c.strip('\n')
        c = c.split(" ")
        dict1[c[0]] = c[1]

    df = pd.read_csv('user_sim.csv')
    neighbors = list(df.uid_neighbors.values)
    target = list(df.uid_target.values)

    def dict_main(i):
        for key, value in dict1.items():
            if str(key) == str(i):
                return int(value)

    new_neighbor = []
    new_target = []
    for i,j in zip(neighbors,target):
        neighbor = dict_main(i)
        target1 = dict_main(j)
        new_neighbor.append(neighbor)
        new_target.append(target1)

    df2 = pd.DataFrame()
    df2['uid_target'] = new_target
    df2['uid_neighbors'] = new_neighbor

    df2.to_csv('new_user_sim.csv')

def item():
    with open('item_list.txt', 'r')as f:
        content = f.readlines()
    dict1 = {}
    for c in content[1:]:
        c = c.strip('\n')
        c = c.split(" ")
        dict1[c[0]] = c[1]

    df = pd.read_csv('item_sim.csv')
    neighbors = list(df.iid_neighbors.values)
    target = list(df.iid_target.values)

    def dict_main(i):
        for key, value in dict1.items():
            if str(key) == str(i):
                return str(value)

    new_neighbor = []
    new_target = []
    for i, j in zip(neighbors, target):
        neighbor = dict_main(i)
        target1 = dict_main(j)
        new_neighbor.append(neighbor)
        new_target.append(target1)

    df2 = pd.DataFrame()
    df2['iid_target'] = new_target
    df2['iid_neighbors'] = new_neighbor

    df2.to_csv('new_item_sim.csv')

if __name__ == '__main__':
    user()
    item()