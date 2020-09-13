import json
import pandas as pd
import numpy as np
import jieba
import jieba.analyse
from pyecharts import options as opts
from pyecharts.charts import Geo,Map,Bar, Line, Page,Pie, Boxplot
from pyecharts.globals import ChartType, SymbolType,ThemeType
from pyecharts.globals import ThemeType
from pyecharts.charts import Line  #折线图所导入的包
from pyecharts import options as opts  #全局设置所导入的包
from pyecharts.charts import Timeline #设置地区轴

#绘制高考大省文科图表

def getnumber():
    data = pd.read_excel("E:/课程设计/2020-2021-1数据采集课设/高考数据分析/高考数据分析/Data/res-大省（文）.xlsx")
    # print(data)
    list1 = []
    data_new = data.iloc[ :, 1:]

    for i in data_new:
        list1.append(data_new[i].tolist())
    #line1().render("E:/课程设计/2020-2021-1数据采集设/高考数据分析/高考数据分析/Print_file/高考大省（理）.html")
    return list1

def line1():
    t = Timeline()
    list1 = getnumber()
    data_city = ["云南","四川","安徽","广东","广西","江西",
            "河北","河南","湖北","湖南","贵州","陕西"]
    for i in range(len(data_city)):
            #print(i,list1[i])
        line = (
            Line()#实例化Line
            .add_xaxis(list)#加入X轴数据
            .add_yaxis(i,list1[i])#加入Y轴数据
            .set_global_opts(title_opts=opts.TitleOpts(title="高考大省文科对比图"))#全局设置项
            .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
                )
        t.add(line,data_city[i])
        # file_chi = t.render("E:/课程设计/2020-2021-1数据采集课设/高考数据分析/高考数据分析/Print_file/高考大省（文）.html")
    return t




#绘制高考大省理科图表
def line2():
    t = Timeline()
    list2 = getnumber2()
    data_city = ["云南","四川","安徽","广东","广西","江西",
            "河北","河南","湖北","湖南","贵州","陕西"]
    for i in range(len(data_city)):
            #print(i,list1[i])
        line = (
            Line()#实例化Line
            .add_xaxis(list)#加入X轴数据
            .add_yaxis(i,list2[i])#加入Y轴数据
            .set_global_opts(title_opts=opts.TitleOpts(title="高考大省理科对比图"))#全局设置项
            .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
                )

        t.add(line,data_city[i])
        # file_math = t.render("E:/课程设计/2020-2021-1数据采集课设/高考数据分析/高考数据分析/Print_file/高考大省（理）.html")

    return t
def getnumber2():
    data = pd.read_excel("E:/课程设计/2020-2021-1数据采集课设/高考数据分析/高考数据分析/Data/res-大省（理）.xlsx")
    #print(data)

    list2 = []
    data_new = data.iloc[ :, 1:]

    for i in data_new:
        list2.append(data_new[i].tolist())
    return list2
    #line1().render("E:/课程设计/2020-2021-1数据采集设/高考数据分析/高考数据分析/Print_file/高考大省（理）.html")
#保存图片为HTML网页

#山东省全体
def bar():
    list3 = getNumber3()
    bar1 = (
        Bar({"theme": ThemeType.MACARONS})
            .add_xaxis(list)
            .add_yaxis("比率",list3 )
            .set_global_opts(
            title_opts={"text": "山东省高考人数比率"},
            toolbox_opts=opts.ToolboxOpts(),
            legend_opts = opts.LegendOpts(is_show=False),
        )
            .set_series_opts(
            label_opts=opts.LabelOpts(is_show=False),

        )
    )
    return bar1

def getNumber3():
    data = pd.read_excel("E:/课程设计/2020-2021-1数据采集课设/高考数据分析/高考数据分析/Data/res-山东省-全体.xlsx")
    #print(data)
    data_new = data.iloc[ :, 1:]
    for i in data_new:
        list3 = data_new[i].tolist()
    return list3

#山东省六科
def line3():
    t = Timeline()
    list4 = getNumber4()
    data_city = ["物理","化学","生物","政治","历史","地理"]
    for i in range(len(data_city)):
            #print(i,list1[i])
        line = (
            Line()#实例化Line
            .add_xaxis(list)#加入X轴数据
            .add_yaxis(i,list4[i])#加入Y轴数据
            .set_global_opts(title_opts=opts.TitleOpts(title="山东省六科成绩对比图"))#全局设置项
            .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
                )
        t.add(line,data_city[i])

    return t

def getNumber4():
    data = pd.read_excel("E:/课程设计/2020-2021-1数据采集课设/高考数据分析/高考数据分析/Data/res-山东省-六科.xlsx")
    #print(data)
    list4 = []
    data_new = data.iloc[ :, 1:]

    for i in data_new:
        list4.append(data_new[i].tolist())
    return list4


list = []
for i in range(100):
    list.append(i)
page = Page(layout=Page.DraggablePageLayout)
page.add(line1(),line2(),bar(),line3())
page.render("E:/课程设计/2020-2021-1数据采集课设/高考数据分析/高考数据分析/Print_file/可视化展示.html")
