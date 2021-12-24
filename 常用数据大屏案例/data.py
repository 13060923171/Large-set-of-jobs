#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from new_data import new_data
from line_net import net
from new_line_net import new_net
from new_week import new_week
from highest_passenger import highest_passenger
from weather import weather_data
from path import parse_url,path_BMap

class SourceDataDemo:
    def __init__(self):
        self.title = '无锡地铁客流数据展示'
        list_net,list_trip = new_data()
        self.counter = {'name': '最新客运量', 'value': list_net}
        self.counter2 = {'name': '最新出行量', 'value': list_trip}
        avg_2014, avg_2015, avg_2016, avg_2017, avg_2018, avg_2019, avg_2020, avg_2021 = net()
        self.echart1_data = {
            'title': '每一年月均线网客流',
            'data': [
                {"name": "2014年", "value": avg_2014},
                {"name": "2015年", "value": avg_2015},
                {"name": "2016年", "value": avg_2016},
                {"name": "2017年", "value": avg_2017},
                {"name": "2018年", "value": avg_2018},
                {"name": "2019年", "value": avg_2019},
                {"name": "2020年", "value": avg_2020},
                {"name": "2021年", "value": avg_2021},
            ],
            'xAxis': ['{}月'.format(x) for x in range(1,13)],
        }
        avg_2021_net, avg_2021_trip = new_net()
        self.echart2_data = {
            'title': '最新一年各月客流、出行量',
            'data': [
                {"name": "客流", "value": avg_2021_net},
                {"name": "出行量", "value": avg_2021_trip},
            ],
            'xAxis': ['{}月'.format(x) for x in range(1,13)],
        }
        week, ridership, week_trip = new_week()
        self.echart3_data = {
            'title': '最新一周客流、出行量',
            'data': [
                {"name": "客流", "value": ridership},
                {"name": "出行量", "value": week_trip},
            ],
            'xAxis': week,
        }
        sum_day,sum_hight, sum_low = weather_data()

        self.echart4_data = {
            'title': '无锡15天内的天气预报',
            'data': [
                {"name": "最高温", "value": sum_hight},
                {"name": "最低温", "value": sum_low},
            ],
            'xAxis': sum_day,
        }
        sum_list = highest_passenger()
        self.echart5_data = {
            'title': '历年最高客流',
            'data': [
                {"name": "2014", "value":sum_list[0]},
                {"name": "2015", "value":sum_list[1]},
                {"name": "2016", "value":sum_list[2]},
                {"name": "2017", "value":sum_list[3]},
                {"name": "2018", "value":sum_list[4]},
                {"name": "2019", "value":sum_list[5]},
                {"name": "2020", "value":sum_list[6]},
                {"name": "2021", "value":sum_list[7]},
            ]
        }
        url = 'http://map.amap.com/service/subway?_1626511538138&srhdata=3202_drw_wuxi.json'
        parse_url(url)
        results = path_BMap()
        self.echart6_data = {
            'title': '无锡地铁路线图',
            'data': results
        }

    @property
    def echart1(self):
        data = self.echart1_data
        echart = {
            'title': data.get('title'),
            'names': [i.get("name") for i in data.get('data')],
            'xAxis': data.get('xAxis'),
            'data': data.get('data'),
        }
        return echart

    @property
    def echart2(self):
        data = self.echart2_data
        echart = {
            'title': data.get('title'),
            'names': [i.get("name") for i in data.get('data')],
            'xAxis': data.get('xAxis'),
            'data': data.get('data'),
        }
        return echart

    @property
    def echart3(self):
        data = self.echart3_data
        echart = {
            'title': data.get('title'),
            'names': [i.get("name") for i in data.get('data')],
            'xAxis': data.get('xAxis'),
            'data': data.get('data'),
        }
        return echart

    @property
    def echart4(self):
        data = self.echart4_data
        echart = {
            'title': data.get('title'),
            'names': [i.get("name") for i in data.get('data')],
            'xAxis': data.get('xAxis'),
            'data': data.get('data'),
        }
        return echart

    @property
    def echart5(self):
        data = self.echart5_data
        echart = {
            'title': data.get('title'),
            'xAxis': [i.get("name") for i in data.get('data')],
            'series': [i.get("value") for i in data.get('data')],
            'data': data.get('data'),
        }
        return echart

    @property
    def echart6(self):
        data = self.echart6_data
        echart = {
            'title': data.get('title'),
            'data': data.get('data'),
        }
        return echart


class SourceData(SourceDataDemo):

    def __init__(self):
        """
        按照 SourceDataDemo 的格式覆盖数据即可
        """
        super().__init__()
        self.title = '无锡地铁客流数据展示'


