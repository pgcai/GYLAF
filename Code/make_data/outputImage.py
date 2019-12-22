import pyecharts.options as opts
from pyecharts.faker import  Faker
from pyecharts.charts import Line, Bar
from pyecharts.globals import ThemeType  # 内置主题
import numpy as np
import pandas as pd


def line_smooth(xData, yData) -> Line:
    c = (
        Line(init_opts=opts.InitOpts(theme=ThemeType.ROMA))
        .add_xaxis(xData)
        .add_yaxis("炖排骨", list(yData[0]), is_smooth=True)
        .add_yaxis("酸菜鱼", list(yData[1]), is_smooth=True)
        .add_yaxis("可乐鸡翅", list(yData[2]), is_smooth=True)
        # .add_yaxis("蒜蓉小油菜", list(yData[3]), is_smooth=True)
        # .add_yaxis("醋溜土豆丝", list(yData[4]))
        # .add_yaxis("拍黄瓜", list(yData[5]))
        # .add_yaxis("芹菜炒肉", list(yData[6]))
        # .add_yaxis("蒜苔肉丝", list(yData[7]))
        .set_global_opts(title_opts=opts.TitleOpts(title="食物销量"),
                         datazoom_opts=opts.DataZoomOpts())
    )
    # print(Faker.choose())
    return c


def bar_datazoom_slider(xData, yData) -> Bar:
    c = (
        Bar(init_opts=opts.InitOpts(theme=ThemeType.ROMA))
        .add_xaxis(xData)
        .add_yaxis("炖排骨",  list(yData[0]))
        .add_yaxis("酸菜鱼", list(yData[1]))
        .add_yaxis("可乐鸡翅", list(yData[2]))
        .add_yaxis("蒜蓉小油菜", list(yData[3]))
        .add_yaxis("醋溜土豆丝", list(yData[4]))
        .add_yaxis("拍黄瓜", list(yData[5]))
        .add_yaxis("芹菜炒肉", list(yData[6]))
        .add_yaxis("蒜苔肉丝", list(yData[7]))
        .set_global_opts(
            title_opts=opts.TitleOpts(title="Bar-DataZoom（slider-水平）"),
            datazoom_opts=opts.DataZoomOpts(),
        )
    )
    return c


def readFoodDay(xData, data, foodName):  # 返回foodName食物的日销量列表
    yDataOne = []
    for i in range(len(xData)):
        Datai = data[(data[:, 5] == xData[i].astype(int))]
        Datai = Datai[(Datai[:, 1] == foodName)]
        # print(Datai)  # test
        # print('---------第{0}天---------'.format(i))
        # print(Datai)
        # print(len(Datai))
        yDatai = sum(Datai[:, 3])
        # print(len(Datai))  # test
        yDataOne.append(yDatai)
    yDataOne = np.array(yDataOne) / 1000000  # 重量以吨为单位
    return yDataOne


def main():
    print('---------------------数据读取-------------------')
    csv_data = pd.read_csv('F:/Github/ZhiQuLeShi/dataset/交易记录.csv')
    date = pd.read_excel('E:/Text folder/智取乐食开发/dataset/date.xlsx')
    csv_data = np.array(csv_data)
    date = np.array(date)[:, 0:3]
    # print(date[63:190])  # test
    # print(csv_data.shape)
    # print(csv_data)
    xData = date[63:190, 0].astype(str)
    yData = []

    for i in range(14):
        foodname = 'F' + str(i+1).zfill(3)
        fooddata = readFoodDay(xData, csv_data, foodname)
        yData.append(fooddata)
    yData = np.array(yData)
    # print(xData)
    # print(xData.shape)
    # print(list(yData[0]))
    print(yData.shape)
    line_smooth(list(xData), list(yData)).render("mycharts.html")
    bar_datazoom_slider(list(xData), yData).render()


if __name__ == '__main__':
    main()