import pandas as pd
import numpy as np
import xlrd
import pickle


def readfile(filePath):
    workbook = xlrd.open_workbook(filePath)  # 文件路径
    return workbook

# print(weather_data.shape)  # 测试用
# print(weather_data.columns)
# print(weather_data.index)
# print(rice_data.columns)


def main():
    print("-----------inputNameData-----------")
    filePath = 'E:/Text folder/智取乐食开发/师大名单.xlsx'
    peopleData = readfile(filePath)

    # 获取所有sheet的名字
    names = peopleData.sheet_names()
    print(names)  # ['各省市', '测试表']  输出所有的表名，以列表的形式

    # 通过sheet索引获得sheet对象
    worksheet = peopleData.sheet_by_index(0)
    print(worksheet)  # <xlrd.sheet.Sheet object at 0x000001B98D99CFD0>

    # 通过sheet名获得sheet对象
    worksheet = peopleData.sheet_by_name("全校住宿信息比对6.21")
    print(worksheet)  # <xlrd.sheet.Sheet object at 0x000001B98D99CFD0>

    # 由上可知，workbook.sheet_names() 返回一个list对象，可以对这个list对象进行操作
    sheet0_name = peopleData.sheet_names()[0]  # 通过sheet索引获取sheet名称
    print(sheet0_name)  # 各省市

    '''对sheet对象进行操作'''
    name = worksheet.name  # 获取表的姓名
    print(name)  # 各省市

    nrows = worksheet.nrows  # 获取该表总行数
    print(nrows)  # 32

    ncols = worksheet.ncols  # 获取该表总列数
    print(ncols)  # 13

    for i in range(nrows):  # 循环打印每一行
        print(worksheet.row_values(i))  # 以列表形式读出，列表中的每一项是str类型

    col_data = worksheet.col_values(1)  # 获取第一列的内容
    print(col_data)

    col_data_sex = worksheet.col_values(2)  # 获取第一列的内容
    print(col_data_sex)

    # --------------------------------------------------
    # 查看男女比例
    femalenum = 0
    malenum = 0
    for i in range(1, len(col_data_sex[1:5001])):
        if(col_data_sex[i] == '女'):
            femalenum += 1
        else:
            malenum += 1
    print(femalenum/(femalenum+malenum))
    # print(malenum)
    # --------------------------------------------------

    # ----------------------------------------------
    # pkl文件读取
    # labelspath = 'F:/情感计算/Results/labels.pkl'
    # with open(labelspath, 'rb') as f:
    #     labelData = pickle.load(f)
    # labels = labelData['labels']
    # # print(labels[0])
    # print(labels.shape)
    # ----------------------------------------------
    print(col_data[1:5001])
    print(col_data_sex[1:5001])
    # ----------------------------------------------
    # pkl文件写入
    dict_data = {"name": col_data[1:5001], "sex": col_data_sex[1:5001]}
    with open('E:/Text folder/智取乐食开发/Name_Sex.pkl', 'wb') as f:
        pickle.dump(dict_data, f, pickle.HIGHEST_PROTOCOL)
    # ----------------------------------------------


if __name__ == "__main__":
    main()
