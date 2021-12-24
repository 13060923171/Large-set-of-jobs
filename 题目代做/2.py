from pyecharts.charts import Bar,Line,Grid
from pyecharts import options as opts
from pyecharts.faker import Faker

x_data = ['鼠标','键盘','显示器','主机','硬盘','光驱']
zhekou = ['2','5','6','5','6','6']
bar = (
    Bar()
    .add_xaxis(x_data)
    .add_yaxis("销售额",Faker.values())

)

line = (
    Line()
    .add_xaxis(x_data)
    .add_yaxis("销量",Faker.values(),label_opts=opts.LabelOpts(is_show=False))
    .add_yaxis("折扣",zhekou,label_opts=opts.LabelOpts(is_show=False))
    .set_global_opts(
            title_opts=opts.TitleOpts(title=" "),
            legend_opts=opts.LegendOpts(type_="scroll", pos_left="left", orient="vertical")
        )

)

grid = (
    #设置页面的宽度
    Grid(init_opts=opts.InitOpts(width='1200px'))
    #GridOpts就是为grid布局而生的一个配置项,常用的几个参数pos_top，pos_bottom，pos_left，pos_right
    .add(bar,grid_opts=opts.GridOpts(is_show=True,pos_left="55%"))
    .add(line,grid_opts=opts.GridOpts(is_show=True,pos_right='55%'))
    .render()
)
