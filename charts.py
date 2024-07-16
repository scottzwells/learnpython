from pyecharts.charts import Line
from pyecharts.options import TitleOpts,ToolboxOpts
line = Line()
line.add_xaxis(["中国","美国","英国"])
line.add_yaxis("GDP",[30,20,10])

line.set_global_opts(
    title_opts=TitleOpts(title="GDP展示",pos_left="left"),
    toolbox_opts=ToolboxOpts(is_show=True),
)

line.render()
