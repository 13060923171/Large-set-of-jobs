import pandas as pd

def new_week():
    df = pd.read_excel("./data/历年客流.xlsx").loc[:, ['月','日','周','1号线客流量','2号线','3号线','线网出行量']]
    df.dropna(axis=0, how='any', inplace=True)
    list_day = [str(l) for l in df['日']][-10:]
    list_week = [str(m) for m in df['周']][-10:]
    list_one = [int(n) for n in df['1号线客流量']][-10:]
    list_two = [int(t) for t in df['2号线']][-10:]
    list_three = [int(t) for t in df['3号线']][-10:]
    list_trip = [int(t) for t in df['线网出行量']][-10:]
    for l in range(len(list_week)):
        try:
            if list_week[l] == '星期一' and list_week[l+1] == '星期二' and list_week[l+2] == '星期三' and list_week[l+3] == '星期四' and list_week[l+4] == '星期五' and list_week[l+5] == '星期六' and list_week[l+6] == '星期日':
                week_trip = [list_trip[l],list_trip[l+1],list_trip[l+2],list_trip[l+3],list_trip[l+4],list_trip[l+5],list_trip[l+6]]
                week = [list_week[l],list_week[l+1],list_week[l+2],list_week[l+3],list_week[l+4],list_week[l+5],list_week[l+6]]
                one = sum([list_one[l]+list_two[l]+list_three[l]]) / 3
                two = sum([list_one[l+1] + list_two[l+1] + list_three[l]]) / 3
                three = sum([list_one[l+2] + list_two[l+2] + list_three[l]]) / 3
                four = sum([list_one[l+3] + list_two[l+3] + list_three[l]]) / 3
                five = sum([list_one[l+4] + list_two[l+4] + list_three[l]]) / 3
                six = sum([list_one[l+5] + list_two[l+5] + list_three[l]]) / 3
                seven = sum([list_one[l+6] + list_two[l+6] + list_three[l]]) / 3
                ridership = [one,two,three,four,five,six,seven]
                return week,ridership,week_trip
        except:
            pass
