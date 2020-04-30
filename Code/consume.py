import pandas as pd
import numpy as np
import csv


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
    yDataOne = np.array(yDataOne) / 1000  # 重量以kg为单位
    return yDataOne


def foodList():
    print('---------------------数据读取-------------------')
    csv_data = pd.read_csv('F:/Github/ZhiQuLeShi/dataset/交易记录.csv')
    date = pd.read_excel('E:/Text folder/智取乐食开发/dataset/date.xlsx')
    csv_data = np.array(csv_data)
    date = np.array(date)[:, 0:3]
    print(date[63:190])  # test
    print(csv_data.shape)
    print(csv_data)
    xData = date[63:190, 0].astype(str)
    yData = []
    for i in range(14):
        foodname = 'F' + str(i+1).zfill(3)
        fooddata = readFoodDay(xData, csv_data, foodname)
        yData.append(fooddata)
    yData = np.array(yData)
    print(yData[0][:10])
    print(yData.shape)

    return date[63:190], yData.T


def saveDatacsv(data, path):
    with open(path, 'w', newline='') as f:  # 采用二进制的方式处理可以省去很多问题
        # 实例化csv.writer对象
        writer = csv.writer(f)
        # 用writerows方法将数据以指定形式保存
        writer.writerows(data)


def main():
    date, food = foodList()
    saveDatacsv(date, 'F:/Github/ZhiQuLeShi/dataset/lstm_data.csv')  # 保存为csv格式
    saveDatacsv(food, 'F:/Github/ZhiQuLeShi/dataset/lstm_label.csv')  # 保存为csv格式
    print("食物消耗信息已保存")


if __name__ == '__main__':
    main()