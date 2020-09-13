from pyecharts.charts import Pie
from pyecharts import options as opts
from pyecharts.globals import ThemeType

def getNumber(list_data):
    allNumber = 524835  # 山东省高考总人数
    list_sc = []
    #print(list)
    for i in list_data:
        #print(i)
        scale = i/allNumber
        list_sc.append(scale)
    # print(list_sc)
    return list_sc

def getUni(list_data):
    物理  = 143736
    化学 = 171462
    生物 = 174793
    政治 = 86114
    历史 = 94885
    地理 = 147029

    list_Uni = [物理,化学,生物,政治,历史,地理]
    list_Uni_new = []
    for i in range(len(list_Uni)):
        # print(list_Uni[i])
        # print(list_data[i])
        scale_uni = list_Uni[i]/list_data[i]
        # print(scale_uni)
        list_Uni_new.append(scale_uni)

    return list_Uni_new

def getPie(list_data):

    attr = ['物理','化学','生物','政治','历史','地理']
    SC = getNumber(list_data)
    SC_uni = getUni(list_data)
    Pie1 = (
        Pie(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))
        .add(
            "",
            [list(z) for z in zip(attr, SC)],
            radius=["30%", "75%"],
            center=["25%", "50%"],
            rosetype="radius",
            label_opts=opts.LabelOpts(is_show=True),
        )
            .add(
            "",
            [list(z) for z in zip(attr, SC_uni)],
            radius=["30%", "75%"],
            center=["75%", "50%"],
            rosetype="area",
            label_opts=opts.LabelOpts(is_show=True),
        )
            .set_global_opts(title_opts=opts.TitleOpts(title="山东省一本上线率饼图"))
            .render("E:/课程设计/2020-2021-1数据采集课设/高考数据分析/高考数据分析/Print_file/山东选考.html")

    )
    return Pie1


def main():
    allNumber = 524835  # 山东省高考总人数
    PNumber = 206326
    CNumber = 259283
    BNumber = 315106
    PLNumber = 169189
    HNumber = 252416
    GNumber = 344594

    list_data = [PNumber, CNumber, BNumber, PLNumber, HNumber, GNumber]

    getNumber(list_data)
    pie_new = getPie(list_data)

main()

