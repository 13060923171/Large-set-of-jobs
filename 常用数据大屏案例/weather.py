import requests
from lxml import etree


sum_hight = []
sum_low = []
sum_day = []


def weather_data():
    global sum_hight, sum_low, sum_day
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Cookie": "Hm_lvt_080dabacb001ad3dc8b9b9049b36d43b=1626600382; f_city=%E5%8C%97%E4%BA%AC%7C101010100%7C; Hm_lpvt_080dabacb001ad3dc8b9b9049b36d43b=1626602207",
    }
    list_url = ['http://www.weather.com.cn/weather/101190201.shtml',
                'http://www.weather.com.cn/weather15d/101190201.shtml']
    for url in list_url:
        html = requests.get(url,headers=headers)
        html.encoding = html.apparent_encoding
        if html.status_code == 200:
            content = html.text
            soup = etree.HTML(content)
            tem = soup.xpath("//ul[@class='t clearfix']/li/p[@class='tem']")
            for t in tem:
                hight = t.xpath("./span/text()")[0]
                sum_hight.append(hight)
                low = t.xpath("./i/text()")[0].replace("â", "").replace("℃", "")
                sum_low.append(low)
            tem_15 = soup.xpath("//ul[@class='t clearfix']/li/span[@class='tem']")
            for t in tem_15:
                hight = t.xpath("./em/text()")[0].replace("℃", "")
                sum_hight.append(hight)
                low = t.xpath("./text()")[0].replace("℃", "").replace('/', '')
                sum_low.append(low)
            time = soup.xpath("//ul[@class='t clearfix']/li")
            for t in time:
                day = t.xpath("./span[@class='time']/text()")
                if len(day) == 0:
                    day = t.xpath("./h1/text()")[0].replace("（", "").replace(" )", "")
                    sum_day.append(day[0:3])
                else:
                    sum_day.append(day[0][-4:-1].replace("（", "").replace(" )", ""))
        else:
            print(html.status_code)
    return sum_day,sum_hight, sum_low
