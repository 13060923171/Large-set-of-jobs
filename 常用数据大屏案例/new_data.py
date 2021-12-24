import pandas as pd

def new_data():
    df = pd.read_excel("./data/历年客流.xlsx").loc[:, ['年份', '月', '线网', '线网出行量']]
    df.dropna(axis=0, how='any', inplace=True)
    list_net = [int(n) for n in df['线网']]
    list_trip = [int(t) for t in df['线网出行量']]
    return list_net[-1],list_trip[-1]

