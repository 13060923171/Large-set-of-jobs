import requests
import json
from pyecharts.commons.utils import JsCode
import math
from pyecharts.charts import BMap
from pyecharts import options as opts
from pyecharts.globals import BMapType, ChartType


headers = {
    "Referer": "http://map.amap.com/subway/index.html?&1100",
    "Host": "map.amap.com",
    "Cookie": "UM_distinctid=17ab3a3f67b81f-0e0bfdfebdbf0a-6373260-e1000-17ab3a3f67c80d; CNZZDATA1255672570=1256503294-1626511415-%7C1626511415; connect.sess=s%3Aj%3A%7B%7D.DffclZ%2FN%2BAiqU5kXMjqg3VQHapScLmBFjbTUDpqgPVQ",
    "X-Requested-With": "XMLHttpRequest",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36",
}

results = []
def parse_url(url):
    html = requests.get(url,headers=headers)
    if html.status_code ==200:
        get_html(html)
    else:
        print(html.status_code)


def get_html(html):
    global results
    content = html.text
    result = json.loads(content)
    stations = []
    for i in result['l']:
        station = []
        for a in i['st']:
            station.append([float(b) for b in a['sl'].split(',')])
        stations.append(station)
    for station in stations:
        results.append([gcj02_bd09(*point) for point in station])


pi = 3.1415926535897932384 #π
r_pi = pi * 3000.0/180.0

def gcj02_bd09(lon_gcj02,lat_gcj02):
    b = math.sqrt(lon_gcj02 * lon_gcj02 + lat_gcj02 * lat_gcj02) + 0.00002 * math.sin(lat_gcj02 * r_pi)
    o = math.atan2(lat_gcj02 , lon_gcj02) + 0.000003 * math.cos(lon_gcj02 * r_pi)
    lon_bd09 = b * math.cos(o) + 0.0065
    lat_bd09 = b * math.sin(o) + 0.006
    return [lon_bd09,lat_bd09]



def path_BMap():
    map_b = (
        BMap(init_opts=opts.InitOpts(width="800px", height="600px"))
        .add_schema(
            baidu_ak='XdSmvztdgmWV2MRVuVCte6xZtYTQHAxG',  # 百度地图开发应用appkey
            center=[120.30319840554199, 31.581367566873144],  # 当前视角的中心点
            zoom=12.5,  # 当前视角的缩放比例
            is_roam=True,  # 开启鼠标缩放和平移漫游
            map_style={
                "styleJson": [
                    {
                        "featureType": "water",
                        "elementType": "all",
                        "stylers": {"color": "#d1d1d1"},
                    },
                    {
                        "featureType": "land",
                        "elementType": "all",
                        "stylers": {"color": "#f3f3f3"},
                    },
                    {
                        "featureType": "railway",
                        "elementType": "all",
                        "stylers": {"visibility": "off"},
                    },
                    {
                        "featureType": "highway",
                        "elementType": "all",
                        "stylers": {"color": "#999999"},
                    },
                    {
                        "featureType": "highway",
                        "elementType": "labels",
                        "stylers": {"visibility": "off"},
                    },
                    {
                        "featureType": "arterial",
                        "elementType": "geometry",
                        "stylers": {"color": "#fefefe"},
                    },
                    {
                        "featureType": "arterial",
                        "elementType": "geometry.fill",
                        "stylers": {"color": "#fefefe"},
                    },
                    {
                        "featureType": "poi",
                        "elementType": "all",
                        "stylers": {"visibility": "off"},
                    },
                    {
                        "featureType": "green",
                        "elementType": "all",
                        "stylers": {"visibility": "off"},
                    },
                    {
                        "featureType": "subway",
                        "elementType": "all",
                        "stylers": {"visibility": "off"},
                    },
                    {
                        "featureType": "manmade",
                        "elementType": "all",
                        "stylers": {"color": "#d1d1d1"},
                    },
                    {
                        "featureType": "local",
                        "elementType": "all",
                        "stylers": {"color": "#d1d1d1"},
                    },
                    {
                        "featureType": "arterial",
                        "elementType": "labels",
                        "stylers": {"visibility": "off"},
                    },
                    {
                        "featureType": "boundary",
                        "elementType": "all",
                        "stylers": {"color": "#fefefe"},
                    },
                    {
                        "featureType": "building",
                        "elementType": "all",
                        "stylers": {"color": "#d1d1d1"},
                    },
                    {
                        "featureType": "label",
                        "elementType": "labels.text.fill",
                        "stylers": {"color": "rgba(0,0,0,0)"},
                    },
                ]
            },
        )
        .add_js_funcs(
            """
        var lngExtent = [39.5, 40.6];
        var latExtent = [115.9, 116.8];
        var cellCount = [50, 50];
        var cellSizeCoord = [
            (lngExtent[1] - lngExtent[0]) / cellCount[0],
            (latExtent[1] - latExtent[0]) / cellCount[1]
        ];
        var gapSize = 0;

        function renderItem(params, api) {
            var lngIndex = api.value(0);
            var latIndex = api.value(1);
            var pointLeftTop = getCoord(params, api, lngIndex, latIndex);
            var pointRightBottom = getCoord(params, api, lngIndex + 1, latIndex + 1);

            return {
                type: 'rect',
                shape: {
                    x: pointLeftTop[0],
                    y: pointLeftTop[1],
                    width: pointRightBottom[0] - pointLeftTop[0],
                    height: pointRightBottom[1] - pointLeftTop[1]
                },
                style: api.style({
                    stroke: 'rgba(0,0,0,0.1)'
                }),
                styleEmphasis: api.styleEmphasis()
            };
        }

        function getCoord(params, api, lngIndex, latIndex) {
            var coords = params.context.coords || (params.context.coords = []);
            var key = lngIndex + '-' + latIndex;
            return coords[key] || (coords[key] = api.coord([
                +(latExtent[0] + lngIndex * cellSizeCoord[0]).toFixed(6),
                +(lngExtent[0] + latIndex * cellSizeCoord[1]).toFixed(6)
            ]));
        }
        """
        )
        .add(
            series_name="",
            type_=ChartType.LINES,  # 设置Geo图类型
            data_pair=results,  # 数据项
            is_polyline=True,  # 是否是多段线，在画lines图情况下#
            render_item=JsCode("renderItem"),
            encode={"tooltip": 2},
            itemstyle_opts=opts.ItemStyleOpts(color="yellow"),
            linestyle_opts=opts.LineStyleOpts(color="blue", opacity=0.5, width=1),  # 线样式配置项
        )
        .add_control_panel(
            maptype_control_opts=opts.BMapTypeControlOpts(type_=BMapType.MAPTYPE_CONTROL_DROPDOWN),  # 切换地图类型的控件
            scale_control_opts=opts.BMapScaleControlOpts(),  # 比例尺控件
            overview_map_opts=opts.BMapOverviewMapControlOpts(is_open=True),  # 添加缩略地图
            navigation_control_opts=opts.BMapNavigationControlOpts()  # 地图的平移缩放控件
        )
    )
    # map_b.render(path='subway_beijing.html')
    return results


if __name__ == '__main__':
    url = 'http://map.amap.com/service/subway?_1626511538138&srhdata=3202_drw_wuxi.json'
    parse_url(url)
    path_BMap()