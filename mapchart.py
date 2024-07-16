from pyecharts.charts import Map
from pyecharts.options import VisualMapOpts
map=Map()
data=[
    ("北京市",99),
    ("上海市",199),
    ("湖南省",299),
    ("湖北省",399),
    ("广东省",499),
]
map.add("测试地图",data,"洪山")
map.set_global_opts(
    visualmap_opts=VisualMapOpts(
        is_show=True,
        is_piecewise=True,
        pieces=[
            {"min":1,"max":9,"lable":"1-9人","color":"blue"},
            {"min":10,"max":888,"lable":"1-9人","color":"red"},
            {"min":100,"max":999,"lable":"1-9人","color":"green"},
            {"min":1000,"max":9999,"lable":"1-9人","color":"yellow"},
        ]
    )
)
map.render()