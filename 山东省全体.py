import matplotlib.pyplot as plt
import scipy.signal as ss
from pyecharts.charts import Line  #折线图所导入的包
from pyecharts.charts import Bar
from pyecharts import options as opts  #全局设置所导入的包
from pyecharts.charts import Timeline #设置地区轴
from pyecharts.faker import Faker
from pyecharts.globals import ThemeType

import os
import pandas as pd
import re

#设定中文字体
# plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
# plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
# # 设定图像尺寸 与分辨率
# plt.rcParams['figure.figsize'] = (8.0, 4.0) # 设置figure_size尺寸
# plt.rcParams['image.interpolation'] = 'nearest' # 设置 interpolation style
# plt.rcParams['savefig.dpi'] = 300 #图片像素
# plt.rcParams['figure.dpi'] = 300 #分辨率
#
# # 将成绩统一到 [0，100] 区间
# MAX_SCORE = 100
# MIN_SCORE = 0
#
# data_file = 'E:/课程设计/2020-2021-1数据采集课设/高考数据分析/高考数据分析/Data/山东省-全体.xlsx'
# res_file = 'E:/课程设计/2020-2021-1数据采集课设/高考数据分析/高考数据分析/Data/res-山东省-全体.xlsx'
#
# # 读取excel , 获取所有表单名字
# excel_info = pd.ExcelFile(data_file)
#
# all_data = {}
# all_data_ratio = {}
# # 获取表中的每一个数据文件 并将数据归一化到 0-500
# for index in range(len(excel_info.sheet_names)):
#     # 读取每一个表单
#     cur_sheetname = excel_info.sheet_names[index]
#     df_sheet = pd.read_excel(data_file, sheet_name=cur_sheetname)
#
#     # 获取每一个表中的 总分数 和对应分数的人数
#     scores = df_sheet[df_sheet.columns.values[0]]
#     #print(scores)
#     nums = df_sheet[df_sheet.columns.values[1]]
#
#     # 数据 对应 每个分数的人数 表
#     ROWS = MAX_SCORE - MIN_SCORE + 1
#     trans_scores_nums = [0] * ROWS
#
#     rows = len(scores)
#     cur_max_score = scores[0]
#     cur_min_score = scores[rows - 1]
#
#     cur_index = 0
#     for s in scores:
#         #计算 变换之后的分数 四舍五入
#         #print(s)
#         trans_score = (int)(round(s - cur_min_score) / (cur_max_score - cur_min_score)* (MAX_SCORE - MIN_SCORE))
#         #print(trans_score)
#         # 在计算分数的位置上 加上对应分数的人数
#         trans_scores_nums[trans_score - 1] += nums[cur_index]
#         cur_index += 1
#     # 数据稍微处理一下， 做简单的平滑处理, 去除最低分数据
#     except0data = [0] * (ROWS - 1)
#     for i in range(ROWS - 1):
#         except0data[i] = trans_scores_nums[i + 1]
#
#     # 中值滤波去除噪点
#     smooth_trans = ss.medfilt(except0data, 7)
#
#     # 将数据转换成比例， 更具有一般性
#     sum = 0
#     smooth_trans_ratio = [0] * (ROWS - 1)
#     for i in range(ROWS - 1):
#         sum += smooth_trans[i]
#
#     for i in range(ROWS - 1):
#         smooth_trans_ratio[i] = smooth_trans[i] / sum
#
#     all_data[cur_sheetname] = smooth_trans
#     all_data_ratio[cur_sheetname] = smooth_trans_ratio
#
#     print('正在进行 {0}/{1}， 表名：{2}'.format(index + 1, len(excel_info.sheet_names), cur_sheetname))
#
#     #plt.plot(smooth_trans2)
# # write_data = pd.DataFrame(all_data)
# # write_data.to_excel(res_file,sheet_name='res')
# write_data_ratio = pd.DataFrame(all_data_ratio)
# write_data_ratio.to_excel(res_file, sheet_name='ratio')

# print('已经完成，存储文件：{0}'.format(res_file))

def bar():
    bar1 = (
        Bar({"theme": ThemeType.MACARONS})
            .add_xaxis(list)
            .add_yaxis("比率",list1 )
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

data = pd.read_excel("E:/课程设计/2020-2021-1数据采集课设/高考数据分析/高考数据分析/Data/res-山东省-全体.xlsx")
#print(data)
list = []
for i in range(100):
    list.append(i)
data_new = data.iloc[ :, 1:]
for i in data_new:
    list1 = data_new[i].tolist()
#print(data_new)
#line1().render("E:/课程设计/2020-2021-1数据采集设/高考数据分析/高考数据分析/Print_file/高考大省（理）.html")
bar().render("E:/课程设计/2020-2021-1数据采集课设/高考数据分析/高考数据分析/Print_file/山东省全体.html")