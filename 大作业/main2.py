import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_csv('Australian import and export vs GDP.csv').loc[:,['Indicator Name','GDP (current US$)','Australia Export to China All Products Export (US$ Thousand)','Australia Export to United States All Products Export (US$ Thousand)','Australia Export to Japan All Products Export (US$ Thousand)','Australia World Export Raw materials Export (US$ Thousand)','Australia Ores and Metals Export (US$ Thousand)','Australia Ores and Metals Import (US$ Thousand)']]
year = df['Indicator Name']
GPD = df['GDP (current US$)']
Export = df['Australia Export to China All Products Export (US$ Thousand)']
Export2 = df['Australia Export to United States All Products Export (US$ Thousand)']
Export3 = df['Australia Export to Japan All Products Export (US$ Thousand)']
Export4 = df['Australia World Export Raw materials Export (US$ Thousand)']
Export5 = df['Australia Ores and Metals Export (US$ Thousand)']
Export6 = df['Australia Ores and Metals Import (US$ Thousand)']



def Import():
    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    ax1.plot(year,GPD,color='darkcyan',label='GDP')
    ax1.legend()
    ax1.set_ylabel('current US$')
    ax2 = ax1.twinx()# this is the important function
    plt.bar(year, height=Export6, width=0.3, color='c',label='Australia Ores and Metals Import')
    ax2.legend()
    ax1.set_xlabel('current years')
    plt.savefig('Import.jpg')
    plt.show()

def export():
    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    ax1.plot(year,GPD,color='darkcyan',label='GDP')
    ax1.legend()
    ax1.set_ylabel('current US$')
    ax2 = ax1.twinx()# this is the important function
    plt.bar(year, height=Export5, width=0.3, color='r',label='Australia Ores and Metals Export')
    ax2.legend()
    ax1.set_xlabel('current years')
    plt.savefig('export.jpg')
    plt.show()

if __name__ == '__main__':
    Import()
    export()
