from pyecharts.charts import Bar,Timeline
from pyecharts.options import LabelOpts
from pyecharts.globals import ThemeType

bar1 = Bar()
bar1.add_xaxis(["中国","美国","英国"])
bar1.add_yaxis("GDP", [30,20,10], label_opts=LabelOpts(position="right"))
bar1.reversal_axis()

bar2 = Bar()
bar2.add_xaxis(["中国","美国","英国"])
bar2.add_yaxis("GDP", [40,30,20], label_opts=LabelOpts(position="right"))
bar2.reversal_axis()

bar3 = Bar()
bar3.add_xaxis(["中国","美国","英国"])
bar3.add_yaxis("GDP", [100,20,50], label_opts=LabelOpts(position="right"))
bar3.reversal_axis()

timeline=Timeline(
    {"theme": ThemeType.LIGHT}
)
timeline.add(bar1,"点1")
timeline.add(bar2,"点2")
timeline.add(bar3,"点3")

timeline.add_schema(
    is_timeline_show=True,
    play_interval=1000,
    is_auto_play=True,
    is_loop_play=True,
)

timeline.render("bar.html")