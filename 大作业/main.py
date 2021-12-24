import pandas as pd
import numpy as np
df = pd.read_csv('Australian import and export vs GDP.csv').loc[:,['Indicator Name','GDP (current US$)','Australia Export to China All Products Export (US$ Thousand)','Australia Export to United States All Products Export (US$ Thousand)','Australia Export to Japan All Products Export (US$ Thousand)','Australia World Export Raw materials Export (US$ Thousand)','Australia Ores and Metals Export (US$ Thousand)','Australia Ores and Metals Import (US$ Thousand)']]
year = df['Indicator Name']
GPD = df['GDP (current US$)']
Export = df['Australia Export to China All Products Export (US$ Thousand)']
Export2 = df['Australia Export to United States All Products Export (US$ Thousand)']
Export3 = df['Australia Export to Japan All Products Export (US$ Thousand)']
Export4 = df['Australia World Export Raw materials Export (US$ Thousand)']
Export5 = df['Australia Ores and Metals Export (US$ Thousand)']
Export6 = df['Australia Ores and Metals Import (US$ Thousand)']


def get_data(data):
    number = 0
    list1 = []
    list2 = []
    for d in data:
        list1.append(d)
        number += 1
        if number == 10:
            list2.append(list1)
            number = 0
            list1 = []
    sum_max = []
    sum_min = []
    sum_mean = []
    for l in list2:
        a = max(l)
        sum_max.append(a)
        b = min(l)
        sum_min.append(b)
        c = np.mean(l)
        sum_mean.append(c)
    return sum_max,sum_min,sum_mean


sum_max,sum_min,sum_mean = get_data(GPD)
sum_max1,sum_min1,sum_mean1 = get_data(Export)
sum_max2,sum_min2,sum_mean2 = get_data(Export2)
sum_max3,sum_min3,sum_mean3 = get_data(Export3)
sum_max4,sum_min4,sum_mean4 = get_data(Export4)
sum_max5,sum_min5,sum_mean5 = get_data(Export5)
sum_max6,sum_min6,sum_mean6 = get_data(Export6)

#求最大值
df_max = pd.DataFrame(data={
    'GDP (current US$)-max':sum_max,
    'Export to China All Products Export-max':sum_max1,
    'Export to United States All Products Export-max':sum_max2,
    'Export to Japan All Products Export-max':sum_max3,
    'Ores and Metals Export-max':sum_max4,
    'World Export Raw materials Export-max':sum_max5,
    'Ores and Metals Import-max':sum_max6,
},index=['90s','00s','10s'])

df_max.to_csv('max.csv')
#求最小值
df_min = pd.DataFrame(data={
    'GDP (current US$)-min':sum_min,
    'Export to China All Products Export-min':sum_min1,
    'Export to United States All Products Export-min':sum_min2,
    'Export to Japan All Products Export-min':sum_max3,
    'Ores and Metals Export-min':sum_min4,
    'World Export Raw materials Export-min':sum_min5,
    'Ores and Metals Import-min':sum_min6,
},index=['90s','00s','10s'])
df_min.to_csv('min.csv')
#求平均值
df_mean = pd.DataFrame(data={
    'GDP (current US$)-min':sum_mean,
    'Export to China All Products Export-mean':sum_mean1,
    'Export to United States All Products Export-mean':sum_mean2,
    'Export to Japan All Products Export-mean':sum_mean3,
    'World Export Raw materials Export-mean':sum_mean4,
    'Ores and Metals Export-mean':sum_mean5,
    'Ores and Metals Import-mean':sum_mean6,
},index=['90s','00s','10s'])
df_mean.to_csv('mean.csv')
