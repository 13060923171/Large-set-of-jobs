import pandas as pd


def net():
    df = pd.read_excel("./data/历年客流.xlsx").loc[:,['年份','月','线网']]
    df.dropna(axis=0, how='any', inplace=True)
    list_year = [str(l) for l in df['年份']]
    list_month = [str(m) for m in df['月']]
    list_net = [int(n) for n in df['线网']]
    avg_2014 = []
    avg_2015 = []
    avg_2016 = []
    avg_2017 = []
    avg_2018 = []
    avg_2019 = []
    avg_2020 = []
    avg_2021 = []
    list_1_2014 = []
    list_2_2014 = []
    list_3_2014 = []
    list_4_2014 = []
    list_5_2014 = []
    list_6_2014 = []
    list_7_2014 = []
    list_8_2014 = []
    list_9_2014 = []
    list_10_2014 = []
    list_11_2014 = []
    list_12_2014 = []
    list_1_2015 = []
    list_2_2015 = []
    list_3_2015 = []
    list_4_2015 = []
    list_5_2015 = []
    list_6_2015 = []
    list_7_2015 = []
    list_8_2015 = []
    list_9_2015 = []
    list_10_2015 = []
    list_11_2015 = []
    list_12_2015 = []
    list_1_2016 = []
    list_2_2016 = []
    list_3_2016 = []
    list_4_2016 = []
    list_5_2016 = []
    list_6_2016 = []
    list_7_2016 = []
    list_8_2016 = []
    list_9_2016 = []
    list_10_2016 = []
    list_11_2016 = []
    list_12_2016 = []
    list_1_2017 = []
    list_2_2017 = []
    list_3_2017 = []
    list_4_2017 = []
    list_5_2017 = []
    list_6_2017 = []
    list_7_2017 = []
    list_8_2017 = []
    list_9_2017 = []
    list_10_2017 = []
    list_11_2017 = []
    list_12_2017 = []
    list_1_2018 = []
    list_2_2018 = []
    list_3_2018 = []
    list_4_2018 = []
    list_5_2018 = []
    list_6_2018 = []
    list_7_2018 = []
    list_8_2018 = []
    list_9_2018 = []
    list_10_2018 = []
    list_11_2018 = []
    list_12_2018 = []
    list_1_2019 = []
    list_2_2019 = []
    list_3_2019 = []
    list_4_2019 = []
    list_5_2019 = []
    list_6_2019 = []
    list_7_2019 = []
    list_8_2019 = []
    list_9_2019 = []
    list_10_2019 = []
    list_11_2019 = []
    list_12_2019 = []
    list_1_2020 = []
    list_2_2020 = []
    list_3_2020 = []
    list_4_2020 = []
    list_5_2020 = []
    list_6_2020 = []
    list_7_2020 = []
    list_8_2020 = []
    list_9_2020 = []
    list_10_2020 = []
    list_11_2020 = []
    list_12_2020 = []
    list_1_2021 = []
    list_2_2021 = []
    list_3_2021 = []
    list_4_2021 = []
    list_5_2021 = []
    list_6_2021 = []
    list_7_2021 = []
    list_8_2021 = []
    list_9_2021 = []
    list_10_2021= []
    list_11_2021= []
    list_12_2021= []
    for i in range(len(list_year)):
        if '2014' in list_year[i]:
            if '1' == list_month[i]:
                list_1_2014.append(list_net[i])
            if '2' == list_month[i]:
                list_2_2014.append(list_net[i])
            if '3' == list_month[i]:
                list_3_2014.append(list_net[i])
            if '4' == list_month[i]:
                list_4_2014.append(list_net[i])
            if '5' == list_month[i]:
                list_5_2014.append(list_net[i])
            if '6' == list_month[i]:
                list_6_2014.append(list_net[i])
            if '7' == list_month[i]:
                list_7_2014.append(list_net[i])
            if '8' == list_month[i]:
                list_8_2014.append(list_net[i])
            if '9' == list_month[i]:
                list_9_2014.append(list_net[i])
            if '10' == list_month[i]:
                list_10_2014.append(list_net[i])
            if '11' == list_month[i]:
                list_11_2014.append(list_net[i])
            if '12' == list_month[i]:
                list_12_2014.append(list_net[i])
        if '2015' in list_year[i]:
            if '1' == list_month[i]:
                list_1_2015.append(list_net[i])
            if '2' == list_month[i]:
                list_2_2015.append(list_net[i])
            if '3' == list_month[i]:
                list_3_2015.append(list_net[i])
            if '4' == list_month[i]:
                list_4_2015.append(list_net[i])
            if '5' == list_month[i]:
                list_5_2015.append(list_net[i])
            if '6' == list_month[i]:
                list_6_2015.append(list_net[i])
            if '7' == list_month[i]:
                list_7_2015.append(list_net[i])
            if '8' == list_month[i]:
                list_8_2015.append(list_net[i])
            if '9' == list_month[i]:
                list_9_2015.append(list_net[i])
            if '10' == list_month[i]:
                list_10_2015.append(list_net[i])
            if '11' == list_month[i]:
                list_11_2015.append(list_net[i])
            if '12' == list_month[i]:
                list_12_2015.append(list_net[i])

        if '2016' in list_year[i]:
            if '1' == list_month[i]:
                list_1_2016.append(list_net[i])
            if '2' == list_month[i]:
                list_2_2016.append(list_net[i])
            if '3' == list_month[i]:
                list_3_2016.append(list_net[i])
            if '4' == list_month[i]:
                list_4_2016.append(list_net[i])
            if '5' == list_month[i]:
                list_5_2016.append(list_net[i])
            if '6' == list_month[i]:
                list_6_2016.append(list_net[i])
            if '7' == list_month[i]:
                list_7_2016.append(list_net[i])
            if '8' == list_month[i]:
                list_8_2016.append(list_net[i])
            if '9' == list_month[i]:
                list_9_2016.append(list_net[i])
            if '10' == list_month[i]:
                list_10_2016.append(list_net[i])
            if '11' == list_month[i]:
                list_11_2016.append(list_net[i])
            if '12' == list_month[i]:
                list_12_2016.append(list_net[i])

        if '2017' in list_year[i]:
            if '1' == list_month[i]:
                list_1_2017.append(list_net[i])
            if '2' == list_month[i]:
                list_2_2017.append(list_net[i])
            if '3' == list_month[i]:
                list_3_2017.append(list_net[i])
            if '4' == list_month[i]:
                list_4_2017.append(list_net[i])
            if '5' == list_month[i]:
                list_5_2017.append(list_net[i])
            if '6' == list_month[i]:
                list_6_2017.append(list_net[i])
            if '7' == list_month[i]:
                list_7_2017.append(list_net[i])
            if '8' == list_month[i]:
                list_8_2017.append(list_net[i])
            if '9' == list_month[i]:
                list_9_2017.append(list_net[i])
            if '10' == list_month[i]:
                list_10_2017.append(list_net[i])
            if '11' == list_month[i]:
                list_11_2017.append(list_net[i])
            if '12' == list_month[i]:
                list_12_2017.append(list_net[i])

        if '2018' in list_year[i]:
            if '1' == list_month[i]:
                list_1_2018.append(list_net[i])
            if '2' == list_month[i]:
                list_2_2018.append(list_net[i])
            if '3' == list_month[i]:
                list_3_2018.append(list_net[i])
            if '4' == list_month[i]:
                list_4_2018.append(list_net[i])
            if '5' == list_month[i]:
                list_5_2018.append(list_net[i])
            if '6' == list_month[i]:
                list_6_2018.append(list_net[i])
            if '7' == list_month[i]:
                list_7_2018.append(list_net[i])
            if '8' == list_month[i]:
                list_8_2018.append(list_net[i])
            if '9' == list_month[i]:
                list_9_2018.append(list_net[i])
            if '10' == list_month[i]:
                list_10_2018.append(list_net[i])
            if '11' == list_month[i]:
                list_11_2018.append(list_net[i])
            if '12' == list_month[i]:
                list_12_2018.append(list_net[i])

        if '2019' in list_year[i]:
            if '1' == list_month[i]:
                list_1_2019.append(list_net[i])
            if '2' == list_month[i]:
                list_2_2019.append(list_net[i])
            if '3' == list_month[i]:
                list_3_2019.append(list_net[i])
            if '4' == list_month[i]:
                list_4_2019.append(list_net[i])
            if '5' == list_month[i]:
                list_5_2019.append(list_net[i])
            if '6' == list_month[i]:
                list_6_2019.append(list_net[i])
            if '7' == list_month[i]:
                list_7_2019.append(list_net[i])
            if '8' == list_month[i]:
                list_8_2019.append(list_net[i])
            if '9' == list_month[i]:
                list_9_2019.append(list_net[i])
            if '10' == list_month[i]:
                list_10_2019.append(list_net[i])
            if '11' == list_month[i]:
                list_11_2019.append(list_net[i])
            if '12' == list_month[i]:
                list_12_2019.append(list_net[i])

        if '2020' in list_year[i]:
            if '1' == list_month[i]:
                list_1_2020.append(list_net[i])
            if '2' == list_month[i]:
                list_2_2020.append(list_net[i])
            if '3' == list_month[i]:
                list_3_2020.append(list_net[i])
            if '4' == list_month[i]:
                list_4_2020.append(list_net[i])
            if '5' == list_month[i]:
                list_5_2020.append(list_net[i])
            if '6' == list_month[i]:
                list_6_2020.append(list_net[i])
            if '7' == list_month[i]:
                list_7_2020.append(list_net[i])
            if '8' == list_month[i]:
                list_8_2020.append(list_net[i])
            if '9' == list_month[i]:
                list_9_2020.append(list_net[i])
            if '10' == list_month[i]:
                list_10_2020.append(list_net[i])
            if '11' == list_month[i]:
                list_11_2020.append(list_net[i])
            if '12' == list_month[i]:
                list_12_2020.append(list_net[i])

        if '2021' in list_year[i]:
            if '1' == list_month[i]:
                list_1_2021.append(list_net[i])
            if '2' == list_month[i]:
                list_2_2021.append(list_net[i])
            if '3' == list_month[i]:
                list_3_2021.append(list_net[i])
            if '4' == list_month[i]:
                list_4_2021.append(list_net[i])
            if '5' == list_month[i]:
                list_5_2021.append(list_net[i])
            if '6' == list_month[i]:
                list_6_2021.append(list_net[i])
            if '7' == list_month[i]:
                list_7_2021.append(list_net[i])
            if '8' == list_month[i]:
                list_8_2021.append(list_net[i])
            if '9' == list_month[i]:
                list_9_2021.append(list_net[i])
            if '10' == list_month[i]:
                list_10_2021.append(list_net[i])
            if '11' == list_month[i]:
                list_11_2021.append(list_net[i])
            if '12' == list_month[i]:
                list_12_2021.append(list_net[i])


    if len(list_1_2014) > 0:
        avg_2014_1 = sum(list_1_2014) / len(list_1_2014)
        avg_2014.append(avg_2014_1)
    else:
        avg_2014.append(0)
    if len(list_2_2014) > 0:
        avg_2014_2 = sum(list_2_2014) / len(list_2_2014)
        avg_2014.append(avg_2014_2)
    else:
        avg_2014.append(0)
    if len(list_3_2014) > 0:
        avg_2014_3 = sum(list_3_2014) / len(list_3_2014)
        avg_2014.append(avg_2014_3)
    else:
        avg_2014.append(0)
    if len(list_4_2014) > 0:
        avg_2014_4 = sum(list_4_2014) / len(list_4_2014)
        avg_2014.append(avg_2014_4)
    else:
        avg_2014.append(0)
    if len(list_5_2014) > 0:
        avg_2014_5 = sum(list_5_2014) / len(list_5_2014)
        avg_2014.append(avg_2014_5)
    else:
        avg_2014.append(0)
    if len(list_6_2014) > 0:
        avg_2014_6 = sum(list_6_2014) / len(list_6_2014)
        avg_2014.append(avg_2014_6)
    else:
        avg_2014.append(0)
    if len(list_7_2014) > 0:
        avg_2014_7 = sum(list_7_2014) / len(list_7_2014)
        avg_2014.append(avg_2014_7)
    else:
        avg_2014.append(0)
    if len(list_8_2014) > 0:
        avg_2014_8 = sum(list_8_2014) / len(list_8_2014)
        avg_2014.append(avg_2014_8)
    else:
        avg_2014.append(0)
    if len(list_9_2014) > 0:
        avg_2014_9 = sum(list_9_2014) / len(list_9_2014)
        avg_2014.append(avg_2014_9)
    else:
        avg_2014.append(0)
    if len(list_10_2014) > 0:
        avg_2014_10 = sum(list_10_2014) / len(list_10_2014)
        avg_2014.append(avg_2014_10)
    else:
        avg_2014.append(0)
    if len(list_11_2014) > 0:
        avg_2014_11 = sum(list_11_2014) / len(list_11_2014)
        avg_2014.append(avg_2014_11)
    else:
        avg_2014.append(0)
    if len(list_12_2014) > 0:
        avg_2014_12 = sum(list_12_2014) / len(list_12_2014)
        avg_2014.append(avg_2014_12)
    else:
        avg_2014.append(0)

    if len(list_1_2015) > 0:
        avg_2015_1 = sum(list_1_2015) / len(list_1_2015)
        avg_2015.append(avg_2015_1)
    else:
        avg_2015.append(0)
    if len(list_2_2015) > 0:
        avg_2015_2 = sum(list_2_2015) / len(list_2_2015)
        avg_2015.append(avg_2015_2)
    else:
        avg_2015.append(0)
    if len(list_3_2015) > 0:
        avg_2015_3 = sum(list_3_2015) / len(list_3_2015)
        avg_2015.append(avg_2015_3)
    else:
        avg_2015.append(0)
    if len(list_4_2015) > 0:
        avg_2015_4 = sum(list_4_2015) / len(list_4_2015)
        avg_2015.append(avg_2015_4)
    else:
        avg_2015.append(0)
    if len(list_5_2015) > 0:
        avg_2015_5 = sum(list_5_2015) / len(list_5_2015)
        avg_2015.append(avg_2015_5)
    else:
        avg_2015.append(0)
    if len(list_6_2015) > 0:
        avg_2015_6 = sum(list_6_2015) / len(list_6_2015)
        avg_2015.append(avg_2015_6)
    else:
        avg_2015.append(0)
    if len(list_7_2015) > 0:
        avg_2015_7 = sum(list_7_2015) / len(list_7_2015)
        avg_2015.append(avg_2015_7)
    else:
        avg_2015.append(0)
    if len(list_8_2015) > 0:
        avg_2015_8 = sum(list_8_2015) / len(list_8_2015)
        avg_2015.append(avg_2015_8)
    else:
        avg_2015.append(0)
    if len(list_9_2015) > 0:
        avg_2015_9 = sum(list_9_2015) / len(list_9_2015)
        avg_2015.append(avg_2015_9)
    else:
        avg_2015.append(0)
    if len(list_10_2015) > 0:
        avg_2015_10 = sum(list_10_2015) / len(list_10_2015)
        avg_2015.append(avg_2015_10)
    else:
        avg_2015.append(0)
    if len(list_11_2015) > 0:
        avg_2015_11 = sum(list_11_2015) / len(list_11_2015)
        avg_2015.append(avg_2015_11)
    else:
        avg_2015.append(0)
    if len(list_12_2015) > 0:
        avg_2015_12 = sum(list_12_2015) / len(list_12_2015)
        avg_2015.append(avg_2015_12)
    else:
        avg_2015.append(0)

    if len(list_1_2016) > 0:
        avg_2016_1 = sum(list_1_2016) / len(list_1_2016)
        avg_2016.append(avg_2016_1)
    else:
        avg_2016.append(0)
    if len(list_2_2016) > 0:
        avg_2016_2 = sum(list_2_2016) / len(list_2_2016)
        avg_2016.append(avg_2016_2)
    else:
        avg_2016.append(0)
    if len(list_3_2016) > 0:
        avg_2016_3 = sum(list_3_2016) / len(list_3_2016)
        avg_2016.append(avg_2016_3)
    else:
        avg_2016.append(0)
    if len(list_4_2016) > 0:
        avg_2016_4 = sum(list_4_2016) / len(list_4_2016)
        avg_2016.append(avg_2016_4)
    else:
        avg_2016.append(0)
    if len(list_5_2016) > 0:
        avg_2016_5 = sum(list_5_2016) / len(list_5_2016)
        avg_2016.append(avg_2016_5)
    else:
        avg_2016.append(0)
    if len(list_6_2016) > 0:
        avg_2016_6 = sum(list_6_2016) / len(list_6_2016)
        avg_2016.append(avg_2016_6)
    else:
        avg_2016.append(0)
    if len(list_7_2016) > 0:
        avg_2016_7 = sum(list_7_2016) / len(list_7_2016)
        avg_2016.append(avg_2016_7)
    else:
        avg_2016.append(0)
    if len(list_8_2016) > 0:
        avg_2016_8 = sum(list_8_2016) / len(list_8_2016)
        avg_2016.append(avg_2016_8)
    else:
        avg_2016.append(0)
    if len(list_9_2016) > 0:
        avg_2016_9 = sum(list_9_2016) / len(list_9_2016)
        avg_2016.append(avg_2016_9)
    else:
        avg_2016.append(0)
    if len(list_10_2016) > 0:
        avg_2016_10 = sum(list_10_2016) / len(list_10_2016)
        avg_2016.append(avg_2016_10)
    else:
        avg_2016.append(0)
    if len(list_11_2016) > 0:
        avg_2016_11 = sum(list_11_2016) / len(list_11_2016)
        avg_2016.append(avg_2016_11)
    else:
        avg_2016.append(0)
    if len(list_12_2016) > 0:
        avg_2016_12 = sum(list_12_2016) / len(list_12_2016)
        avg_2016.append(avg_2016_12)
    else:
        avg_2016.append(0)

    if len(list_1_2017) > 0:
        avg_2017_1 = sum(list_1_2017) / len(list_1_2017)
        avg_2017.append(avg_2017_1)
    else:
        avg_2017.append(0)
    if len(list_2_2017) > 0:
        avg_2017_2 = sum(list_2_2017) / len(list_2_2017)
        avg_2017.append(avg_2017_2)
    else:
        avg_2017.append(0)
    if len(list_3_2017) > 0:
        avg_2017_3 = sum(list_3_2017) / len(list_3_2017)
        avg_2017.append(avg_2017_3)
    else:
        avg_2017.append(0)
    if len(list_4_2017) > 0:
        avg_2017_4 = sum(list_4_2017) / len(list_4_2017)
        avg_2017.append(avg_2017_4)
    else:
        avg_2017.append(0)
    if len(list_5_2017) > 0:
        avg_2017_5 = sum(list_5_2017) / len(list_5_2017)
        avg_2017.append(avg_2017_5)
    else:
        avg_2017.append(0)
    if len(list_6_2017) > 0:
        avg_2017_6 = sum(list_6_2017) / len(list_6_2017)
        avg_2017.append(avg_2017_6)
    else:
        avg_2017.append(0)
    if len(list_7_2017) > 0:
        avg_2017_7 = sum(list_7_2017) / len(list_7_2017)
        avg_2017.append(avg_2017_7)
    else:
        avg_2017.append(0)
    if len(list_8_2017) > 0:
        avg_2017_8 = sum(list_8_2017) / len(list_8_2017)
        avg_2017.append(avg_2017_8)
    else:
        avg_2017.append(0)
    if len(list_9_2017) > 0:
        avg_2017_9 = sum(list_9_2017) / len(list_9_2017)
        avg_2017.append(avg_2017_9)
    else:
        avg_2017.append(0)
    if len(list_10_2017) > 0:
        avg_2017_10 = sum(list_10_2017) / len(list_10_2017)
        avg_2017.append(avg_2017_10)
    else:
        avg_2017.append(0)
    if len(list_11_2017) > 0:
        avg_2017_11 = sum(list_11_2017) / len(list_11_2017)
        avg_2017.append(avg_2017_11)
    else:
        avg_2017.append(0)
    if len(list_12_2017) > 0:
        avg_2017_12 = sum(list_12_2017) / len(list_12_2017)
        avg_2017.append(avg_2017_12)
    else:
        avg_2017.append(0)

    if len(list_1_2018) > 0:
        avg_2018_1 = sum(list_1_2018) / len(list_1_2018)
        avg_2018.append(avg_2018_1)
    else:
        avg_2018.append(0)
    if len(list_2_2018) > 0:
        avg_2018_2 = sum(list_2_2018) / len(list_2_2018)
        avg_2018.append(avg_2018_2)
    else:
        avg_2018.append(0)
    if len(list_3_2018) > 0:
        avg_2018_3 = sum(list_3_2018) / len(list_3_2018)
        avg_2018.append(avg_2018_3)
    else:
        avg_2018.append(0)
    if len(list_4_2018) > 0:
        avg_2018_4 = sum(list_4_2018) / len(list_4_2018)
        avg_2018.append(avg_2018_4)
    else:
        avg_2018.append(0)
    if len(list_5_2018) > 0:
        avg_2018_5 = sum(list_5_2018) / len(list_5_2018)
        avg_2018.append(avg_2018_5)
    else:
        avg_2018.append(0)
    if len(list_6_2018) > 0:
        avg_2018_6 = sum(list_6_2018) / len(list_6_2018)
        avg_2018.append(avg_2018_6)
    else:
        avg_2018.append(0)
    if len(list_7_2018) > 0:
        avg_2018_7 = sum(list_7_2018) / len(list_7_2018)
        avg_2018.append(avg_2018_7)
    else:
        avg_2018.append(0)
    if len(list_8_2018) > 0:
        avg_2018_8 = sum(list_8_2018) / len(list_8_2018)
        avg_2018.append(avg_2018_8)
    else:
        avg_2018.append(0)
    if len(list_9_2018) > 0:
        avg_2018_9 = sum(list_9_2018) / len(list_9_2018)
        avg_2018.append(avg_2018_9)
    else:
        avg_2018.append(0)
    if len(list_10_2018) > 0:
        avg_2018_10 = sum(list_10_2018) / len(list_10_2018)
        avg_2018.append(avg_2018_10)
    else:
        avg_2018.append(0)
    if len(list_11_2018) > 0:
        avg_2018_11 = sum(list_11_2018) / len(list_11_2018)
        avg_2018.append(avg_2018_11)
    else:
        avg_2018.append(0)
    if len(list_12_2018) > 0:
        avg_2018_12 = sum(list_12_2018) / len(list_12_2018)
        avg_2018.append(avg_2018_12)
    else:
        avg_2018.append(0)

    if len(list_1_2019) > 0:
        avg_2019_1 = sum(list_1_2019) / len(list_1_2019)
        avg_2019.append(avg_2019_1)
    else:
        avg_2019.append(0)
    if len(list_2_2019) > 0:
        avg_2019_2 = sum(list_2_2019) / len(list_2_2019)
        avg_2019.append(avg_2019_2)
    else:
        avg_2019.append(0)
    if len(list_3_2019) > 0:
        avg_2019_3 = sum(list_3_2019) / len(list_3_2019)
        avg_2019.append(avg_2019_3)
    else:
        avg_2019.append(0)
    if len(list_4_2019) > 0:
        avg_2019_4 = sum(list_4_2019) / len(list_4_2019)
        avg_2019.append(avg_2019_4)
    else:
        avg_2019.append(0)
    if len(list_5_2019) > 0:
        avg_2019_5 = sum(list_5_2019) / len(list_5_2019)
        avg_2019.append(avg_2019_5)
    else:
        avg_2019.append(0)
    if len(list_6_2019) > 0:
        avg_2019_6 = sum(list_6_2019) / len(list_6_2019)
        avg_2019.append(avg_2019_6)
    else:
        avg_2019.append(0)
    if len(list_7_2019) > 0:
        avg_2019_7 = sum(list_7_2019) / len(list_7_2019)
        avg_2019.append(avg_2019_7)
    else:
        avg_2019.append(0)
    if len(list_8_2019) > 0:
        avg_2019_8 = sum(list_8_2019) / len(list_8_2019)
        avg_2019.append(avg_2019_8)
    else:
        avg_2019.append(0)
    if len(list_9_2019) > 0:
        avg_2019_9 = sum(list_9_2019) / len(list_9_2019)
        avg_2019.append(avg_2019_9)
    else:
        avg_2019.append(0)
    if len(list_10_2019) > 0:
        avg_2019_10 = sum(list_10_2019) / len(list_10_2019)
        avg_2019.append(avg_2019_10)
    else:
        avg_2019.append(0)
    if len(list_11_2019) > 0:
        avg_2019_11 = sum(list_11_2019) / len(list_11_2019)
        avg_2019.append(avg_2019_11)
    else:
        avg_2019.append(0)
    if len(list_12_2019) > 0:
        avg_2019_12 = sum(list_12_2019) / len(list_12_2019)
        avg_2019.append(avg_2019_12)
    else:
        avg_2019.append(0)

    if len(list_1_2020) > 0:
        avg_2020_1 = sum(list_1_2020) / len(list_1_2020)
        avg_2020.append(avg_2020_1)
    else:
        avg_2020.append(0)
    if len(list_2_2020) > 0:
        avg_2020_2 = sum(list_2_2020) / len(list_2_2020)
        avg_2020.append(avg_2020_2)
    else:
        avg_2020.append(0)
    if len(list_3_2020) > 0:
        avg_2020_3 = sum(list_3_2020) / len(list_3_2020)
        avg_2020.append(avg_2020_3)
    else:
        avg_2020.append(0)
    if len(list_4_2020) > 0:
        avg_2020_4 = sum(list_4_2020) / len(list_4_2020)
        avg_2020.append(avg_2020_4)
    else:
        avg_2020.append(0)
    if len(list_5_2020) > 0:
        avg_2020_5 = sum(list_5_2020) / len(list_5_2020)
        avg_2020.append(avg_2020_5)
    else:
        avg_2020.append(0)
    if len(list_6_2020) > 0:
        avg_2020_6 = sum(list_6_2020) / len(list_6_2020)
        avg_2020.append(avg_2020_6)
    else:
        avg_2020.append(0)
    if len(list_7_2020) > 0:
        avg_2020_7 = sum(list_7_2020) / len(list_7_2020)
        avg_2020.append(avg_2020_7)
    else:
        avg_2020.append(0)
    if len(list_8_2020) > 0:
        avg_2020_8 = sum(list_8_2020) / len(list_8_2020)
        avg_2020.append(avg_2020_8)
    else:
        avg_2020.append(0)
    if len(list_9_2020) > 0:
        avg_2020_9 = sum(list_9_2020) / len(list_9_2020)
        avg_2020.append(avg_2020_9)
    else:
        avg_2020.append(0)
    if len(list_10_2020) > 0:
        avg_2020_10 = sum(list_10_2020) / len(list_10_2020)
        avg_2020.append(avg_2020_10)
    else:
        avg_2020.append(0)
    if len(list_11_2020) > 0:
        avg_2020_11 = sum(list_11_2020) / len(list_11_2020)
        avg_2020.append(avg_2020_11)
    else:
        avg_2020.append(0)
    if len(list_12_2020) > 0:
        avg_2020_12 = sum(list_12_2020) / len(list_12_2020)
        avg_2020.append(avg_2020_12)
    else:
        avg_2020.append(0)

    if len(list_1_2021) > 0:
        avg_2021_1 = sum(list_1_2021) / len(list_1_2021)
        avg_2021.append(avg_2021_1)
    else:
        avg_2021.append(0)
    if len(list_2_2021) > 0:
        avg_2021_2 = sum(list_2_2021) / len(list_2_2021)
        avg_2021.append(avg_2021_2)
    else:
        avg_2021.append(0)
    if len(list_3_2021) > 0:
        avg_2021_3 = sum(list_3_2021) / len(list_3_2021)
        avg_2021.append(avg_2021_3)
    else:
        avg_2021.append(0)
    if len(list_4_2021) > 0:
        avg_2021_4 = sum(list_4_2021) / len(list_4_2021)
        avg_2021.append(avg_2021_4)
    else:
        avg_2021.append(0)
    if len(list_5_2021) > 0:
        avg_2021_5 = sum(list_5_2021) / len(list_5_2021)
        avg_2021.append(avg_2021_5)
    else:
        avg_2021.append(0)
    if len(list_6_2021) > 0:
        avg_2021_6 = sum(list_6_2021) / len(list_6_2021)
        avg_2021.append(avg_2021_6)
    else:
        avg_2021.append(0)
    if len(list_7_2021) > 0:
        avg_2021_7 = sum(list_7_2021) / len(list_7_2021)
        avg_2021.append(avg_2021_7)
    else:
        avg_2021.append(0)
    if len(list_8_2021) > 0:
        avg_2021_8 = sum(list_8_2021) / len(list_8_2021)
        avg_2021.append(avg_2021_8)
    else:
        avg_2021.append(0)
    if len(list_9_2021) > 0:
        avg_2021_9 = sum(list_9_2021) / len(list_9_2021)
        avg_2021.append(avg_2021_9)
    else:
        avg_2021.append(0)
    if len(list_10_2021) > 0:
        avg_2021_10 = sum(list_10_2021) / len(list_10_2021)
        avg_2021.append(avg_2021_10)
    else:
        avg_2021.append(0)
    if len(list_11_2021) > 0:
        avg_2021_11 = sum(list_11_2021) / len(list_11_2021)
        avg_2021.append(avg_2021_11)
    else:
        avg_2021.append(0)
    if len(list_12_2021) > 0:
        avg_2021_12 = sum(list_12_2021) / len(list_12_2021)
        avg_2021.append(avg_2021_12)
    else:
        avg_2021.append(0)



    return avg_2014,avg_2015,avg_2016,avg_2017,avg_2018,avg_2019,avg_2020,avg_2021


