import pandas as pd

def new_net():
    df = pd.read_excel("./data/历年客流.xlsx").loc[:, ['年份', '月', '线网','线网出行量']]
    df.dropna(axis=0, how='any', inplace=True)
    list_year = [str(l) for l in df['年份']]
    list_month = [str(m) for m in df['月']]
    list_net = [int(n) for n in df['线网']]
    list_trip = [int(t) for t in df['线网出行量']]
    avg_2021_net = []
    avg_2021_trip = []
    list_1_2021 = []
    list_2_2021 = []
    list_3_2021 = []
    list_4_2021 = []
    list_5_2021 = []
    list_6_2021 = []
    list_7_2021 = []
    list_8_2021 = []
    list_9_2021 = []
    list_10_2021 = []
    list_11_2021 = []
    list_12_2021 = []
    list_1_2021_1 = []
    list_2_2021_1 = []
    list_3_2021_1 = []
    list_4_2021_1 = []
    list_5_2021_1 = []
    list_6_2021_1 = []
    list_7_2021_1 = []
    list_8_2021_1 = []
    list_9_2021_1 = []
    list_10_2021_1 = []
    list_11_2021_1 = []
    list_12_2021_1 = []
    for i in range(len(list_year)):
        if '2021' in list_year[i]:
            if '1' == list_month[i]:
                list_1_2021.append(list_net[i])
                list_1_2021_1.append(list_trip[i])
            if '2' == list_month[i]:
                list_2_2021.append(list_net[i])
                list_2_2021_1.append(list_trip[i])
            if '3' == list_month[i]:
                list_3_2021.append(list_net[i])
                list_3_2021_1.append(list_trip[i])
            if '4' == list_month[i]:
                list_4_2021.append(list_net[i])
                list_4_2021_1.append(list_trip[i])
            if '5' == list_month[i]:
                list_5_2021.append(list_net[i])
                list_5_2021_1.append(list_trip[i])
            if '6' == list_month[i]:
                list_6_2021.append(list_net[i])
                list_6_2021_1.append(list_trip[i])
            if '7' == list_month[i]:
                list_7_2021.append(list_net[i])
                list_7_2021_1.append(list_trip[i])
            if '8' == list_month[i]:
                list_8_2021.append(list_net[i])
                list_8_2021_1.append(list_trip[i])
            if '9' == list_month[i]:
                list_9_2021.append(list_net[i])
                list_9_2021_1.append(list_trip[i])
            if '10' == list_month[i]:
                list_10_2021.append(list_net[i])
                list_10_2021_1.append(list_trip[i])
            if '11' == list_month[i]:
                list_11_2021.append(list_net[i])
                list_11_2021_1.append(list_trip[i])
            if '12' == list_month[i]:
                list_12_2021.append(list_net[i])
                list_12_2021_1.append(list_trip[i])


    if len(list_1_2021) and len(list_1_2021_1) > 0:
        avg_2021_1 = sum(list_1_2021) / len(list_1_2021)
        avg_2021_1_1 = sum(list_1_2021_1) / len(list_1_2021_1)
        avg_2021_net.append(avg_2021_1)
        avg_2021_trip.append(avg_2021_1_1)
    else:
        avg_2021_net.append(0)
        avg_2021_trip.append(0)
    if len(list_2_2021) and len(list_2_2021_1) > 0:
        avg_2021_2 = sum(list_2_2021) / len(list_2_2021)
        avg_2021_2_1 = sum(list_2_2021_1) / len(list_2_2021_1)
        avg_2021_net.append(avg_2021_2)
        avg_2021_trip.append(avg_2021_2_1)
    else:
        avg_2021_net.append(0)
        avg_2021_trip.append(0)
    if len(list_3_2021) and len(list_3_2021_1) > 0:
        avg_2021_3 = sum(list_3_2021) / len(list_3_2021)
        avg_2021_3_1 = sum(list_3_2021_1) / len(list_3_2021_1)
        avg_2021_net.append(avg_2021_3)
        avg_2021_trip.append(avg_2021_3_1)
    else:
        avg_2021_net.append(0)
        avg_2021_trip.append(0)
    if len(list_4_2021) and len(list_4_2021_1) > 0:
        avg_2021_4 = sum(list_4_2021) / len(list_4_2021)
        avg_2021_4_1 = sum(list_4_2021_1) / len(list_4_2021_1)
        avg_2021_net.append(avg_2021_4)
        avg_2021_trip.append(avg_2021_4_1)
    else:
        avg_2021_net.append(0)
        avg_2021_trip.append(0)
    if len(list_5_2021) and len(list_5_2021_1) > 0:
        avg_2021_5 = sum(list_5_2021) / len(list_5_2021)
        avg_2021_5_1 = sum(list_5_2021_1) / len(list_5_2021_1)
        avg_2021_net.append(avg_2021_5)
        avg_2021_trip.append(avg_2021_5_1)
    else:
        avg_2021_net.append(0)
        avg_2021_trip.append(0)
    if len(list_6_2021) and len(list_6_2021_1) > 0:
        avg_2021_6 = sum(list_6_2021) / len(list_6_2021)
        avg_2021_6_1 = sum(list_6_2021_1) / len(list_6_2021_1)
        avg_2021_net.append(avg_2021_6)
        avg_2021_trip.append(avg_2021_6_1)
    else:
        avg_2021_net.append(0)
        avg_2021_trip.append(0)
    if len(list_7_2021) and len(list_7_2021_1) > 0:
        avg_2021_7 = sum(list_7_2021) / len(list_7_2021)
        avg_2021_7_1 = sum(list_7_2021_1) / len(list_7_2021_1)
        avg_2021_net.append(avg_2021_7)
        avg_2021_trip.append(avg_2021_7_1)
    else:
        avg_2021_net.append(0)
        avg_2021_trip.append(0)
    if len(list_8_2021) and len(list_8_2021_1) > 0:
        avg_2021_8 = sum(list_8_2021) / len(list_8_2021)
        avg_2021_8_1 = sum(list_8_2021_1) / len(list_8_2021_1)
        avg_2021_net.append(avg_2021_8)
        avg_2021_trip.append(avg_2021_8_1)
    else:
        avg_2021_net.append(0)
        avg_2021_trip.append(0)
    if len(list_9_2021) and len(list_9_2021_1) > 0:
        avg_2021_9 = sum(list_9_2021) / len(list_9_2021)
        avg_2021_9_1 = sum(list_9_2021_1) / len(list_9_2021_1)
        avg_2021_net.append(avg_2021_9)
        avg_2021_trip.append(avg_2021_9_1)
    else:
        avg_2021_net.append(0)
        avg_2021_trip.append(0)
    if len(list_10_2021) and len(list_10_2021_1) > 0:
        avg_2021_10 = sum(list_10_2021) / len(list_10_2021)
        avg_2021_10_1 = sum(list_10_2021_1) / len(list_10_2021_1)
        avg_2021_net.append(avg_2021_10)
        avg_2021_trip.append(avg_2021_10_1)
    else:
        avg_2021_net.append(0)
        avg_2021_trip.append(0)
    if len(list_11_2021) and len(list_11_2021_1) > 0:
        avg_2021_11 = sum(list_11_2021) / len(list_11_2021)
        avg_2021_11_1 = sum(list_11_2021_1) / len(list_11_2021_1)
        avg_2021_net.append(avg_2021_11)
        avg_2021_trip.append(avg_2021_11_1)
    else:
        avg_2021_net.append(0)
        avg_2021_trip.append(0)
    if len(list_12_2021) and len(list_12_2021_1) > 0:
        avg_2021_12 = sum(list_12_2021) / len(list_12_2021)
        avg_2021_12_1 = sum(list_12_2021_1) / len(list_12_2021_1)
        avg_2021_net.append(avg_2021_12)
        avg_2021_trip.append(avg_2021_12_1)
    else:
        avg_2021_net.append(0)
        avg_2021_trip.append(0)

    return avg_2021_net,avg_2021_trip

