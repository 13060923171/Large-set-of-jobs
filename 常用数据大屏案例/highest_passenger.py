import pandas as pd
import numpy as np
import math

def highest_passenger():
    df = pd.read_excel("./data/历年客流.xlsx").loc[:,['年份','1号线客流量','2号线','3号线']]
    list_year = [str(l) for l in df['年份']]
    list_one = []
    list_two = []
    list_three = []
    sum_list = []
    for t in df['2号线']:
        if math.isnan(t):
            list_two.append(0)
        else:
            list_two.append(t)
    for t in df['1号线客流量']:
        if math.isnan(t):
            list_one.append(0)
        else:
            list_one.append(t)
    for t in df['3号线']:
        if math.isnan(t):
            list_three.append(0)
        else:
            list_three.append(t)

    list_2014_1 = []
    list_2014_2 = []
    list_2014_3 = []
    list_2015_1 = []
    list_2015_2 = []
    list_2015_3 = []
    list_2016_1 = []
    list_2016_2 = []
    list_2016_3 = []
    list_2017_1 = []
    list_2017_2 = []
    list_2017_3 = []
    list_2018_1 = []
    list_2018_2 = []
    list_2018_3 = []
    list_2019_1 = []
    list_2019_2 = []
    list_2019_3 = []
    list_2020_1 = []
    list_2020_2 = []
    list_2020_3 = []
    list_2021_1 = []
    list_2021_2 = []
    list_2021_3 = []


    for i in range(len(list_year)):
        if list_year[i] == '2014年':
            list_2014_1.append(list_one[i])
            list_2014_2.append(list_two[i])
            list_2014_3.append(list_three[i])
        if list_year[i] == '2015年':
            list_2015_1.append(list_one[i])
            list_2015_2.append(list_two[i])
            list_2015_3.append(list_three[i])
        if list_year[i] == '2016年':
            list_2016_1.append(list_one[i])
            list_2016_2.append(list_two[i])
            list_2016_3.append(list_three[i])
        if list_year[i] == '2017年':
            list_2017_1.append(list_one[i])
            list_2017_2.append(list_two[i])
            list_2017_3.append(list_three[i])
        if list_year[i] == '2018年':
            list_2018_1.append(list_one[i])
            list_2018_2.append(list_two[i])
            list_2018_3.append(list_three[i])
        if list_year[i] == '2019年':
            list_2019_1.append(list_one[i])
            list_2019_2.append(list_two[i])
            list_2019_3.append(list_three[i])
        if list_year[i] == '2020年':
            list_2020_1.append(list_one[i])
            list_2020_2.append(list_two[i])
            list_2020_3.append(list_three[i])
        if list_year[i] == '2021年':
            list_2021_1.append(list_one[i])
            list_2021_2.append(list_two[i])
            list_2021_3.append(list_three[i])



    sum_2014 = [max(list_2014_1),max(list_2014_2),max(list_2014_3)]
    sum_list.append(max(sum_2014))
    sum_2015= [max(list_2015_1), max(list_2015_2), max(list_2015_3)]
    sum_list.append(max(sum_2015))
    sum_2016 = [max(list_2016_1), max(list_2016_2), max(list_2016_3)]
    sum_list.append(max(sum_2016))
    sum_2017 = [max(list_2017_1), max(list_2017_2), max(list_2017_3)]
    sum_list.append(max(sum_2017))
    sum_2018 = [max(list_2018_1), max(list_2018_2), max(list_2018_3)]
    sum_list.append(max(sum_2018))
    sum_2019 = [max(list_2019_1), max(list_2019_2), max(list_2019_3)]
    sum_list.append(max(sum_2019))
    sum_2020 = [max(list_2020_1), max(list_2020_2), max(list_2020_3)]
    sum_list.append(max(sum_2020))
    sum_2021= [max(list_2021_1), max(list_2021_2), max(list_2021_3)]
    sum_list.append(max(sum_2021))

    return sum_list

