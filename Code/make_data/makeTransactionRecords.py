import pickle
import numpy as np
import random
import xlrd
import math


def allDay(date, people, food):
    TsData = []
    for i in range(5):  # 测试用
    # for i in range(len(date[0])):
        oneDayData = oneDay(date[:, i], people, food)
        TsData.extend(oneDayData)
    TsData = np.array(TsData)
    return TsData


def oneDay(date, people, food):
    oneDayDate = []
    # date[0]日期 date[1]星期 date[2]是否工作日
    for i in range(len(people[0])):  # allPeople
        onepeopleData = onePeople(date, people[:, i], food)
        oneDayDate.append(onepeopleData)
    return oneDayDate


def onePeople(date, people, food):
    # people[[学号], [身高], [体重], [口味1], [口味2], [忌口], [喜爱类型1], [喜爱类型2]]
    # food[[餐品id],[餐品口味],[餐品忌口],[餐品类型1],[餐品类型2],[价格],[备注]]
    peopleData = []
    # return[[用户id],[消费食物id],[消费质量],[消费金额],[消费时间]]

    # 用户id
    peopleData.append(people[0])

    # 消费食物id
    selectfd = selectFood(people[3:], food)
    peopleData.append(selectfd)

    # 消费质量
    height = people[1].astype(int)
    weight = people[2].astype(int)
    foodweight = calculateWeight(height, weight)
    peopleData.append(foodweight)

    # 消费金额
    thefood = food[food[:, 0] == selectfd]
    price = float(thefood[:,5])
    money = foodweight*price
    peopleData.append(price)
    peopleData.append(format(money, '.3f'))

    # 消费时间


    return peopleData


def calculateWeight(height, weight):  # 餐品质量/重量
    BMI = weight/(math.pow(height/100, 2))
    foodweight = np.random.normal(loc=250 + (BMI - 21.2)*6, scale=5, size=None)
    # print(BMI)
    return int(foodweight)


def selectFood(people, food):
    # people[[口味1], [口味2], [忌口], [喜爱类型1], [喜爱类型2]]
    # food[[餐品id],[餐品口味],[餐品忌口],[餐品类型1],[餐品类型2],[价格],[备注]]
    # 喜爱食物类型1包含的食物
    thefood0 = food[food[:, 3] == people[3]]
    thefood1 = food[food[:, 4] == people[3]]
    thefoodone = np.vstack((thefood0, thefood1))

    # 喜爱食物类型2包含的食物
    thefood0 = food[food[:, 3] == people[4]]
    thefood1 = food[food[:, 4] == people[3]]
    thefoodtwo = np.vstack((thefood0, thefood1))
    # print('-----------h---------')  # 测试用
    # print(thefoodone)
    # print(thefoodtwo)
    # print('-----------t-----------')
    if np.random.random_sample() < 0.90:  # 0.9:0.1   按规律饮食 ：随机选一个
        if np.random.random_sample() < 0.70 and thefoodone.size != 0:
            s = np.random.randint(0, high=len(thefoodone), dtype='l')
            selectfood = thefoodone[s, 0:3]
            # print('哈哈哈哈')  # 测试用
        elif thefoodtwo.size != 0:
            s = np.random.randint(0, high=len(thefoodtwo), dtype='l')
            selectfood = thefoodtwo[s, 0:3]
            # print('啦啦啦')  # 测试用
        else:
            s = np.random.randint(0, high=len(food), dtype='l')
            selectfood = food[s, 0:3]
    else:
        s = np.random.randint(0, high=len(food), dtype='l')
        selectfood = food[s, 0:3]
        # print('嘻嘻嘻嘻嘻')  # 测试用
    while(selectfood[2] == people[2]):  # 判断忌口
        if people[2]=='A0':
            break
        s = np.random.randint(0, high=len(food), dtype='l')
        # print(s)
        selectfood = food[s, 0:3]
    return selectfood[0]


def readfile(filePath):
    workbook = xlrd.open_workbook(filePath)  # 文件路径
    return workbook


def readPeopleList(filePath):
    data = []
    workbook = readfile(filePath)
    # 通过sheet索引获得sheet对象
    worksheet = workbook.sheet_by_index(0)
    col_data = worksheet.col_values(0)  # 获取第一列的内容 学号
    data.append(col_data[1:])
    col_data = worksheet.col_values(4)  # 身高
    data.append(col_data[1:])
    col_data = worksheet.col_values(5)  # 体重
    data.append(col_data[1:])
    col_data = worksheet.col_values(7)  # 口味1
    data.append(col_data[1:])
    col_data = worksheet.col_values(8)  # 口味2
    data.append(col_data[1:])
    col_data = worksheet.col_values(9)  # 忌口
    data.append(col_data[1:])
    col_data = worksheet.col_values(10)  # 喜爱类型1
    data.append(col_data[1:])
    col_data = worksheet.col_values(11)  # 喜爱类型2
    data.append(col_data[1:])
    data = np.array(data)  # [[学号], [身高], [体重], [口味1], [口味2], [忌口], [喜爱类型1], [喜爱类型2]]
    return data


def readFoodList(filePath):
    data = []
    workbook = readfile(filePath)
    # 通过sheet索引获得sheet对象
    worksheet = workbook.sheet_by_index(0)
    col_data = worksheet.col_values(0)  # 获取第一列的内容 餐品id
    data.append(col_data[1:])
    col_data = worksheet.col_values(2)  # 餐品口味
    data.append(col_data[1:])
    col_data = worksheet.col_values(3)  # 餐品忌口
    data.append(col_data[1:])
    col_data = worksheet.col_values(4)  # 餐品类型1
    data.append(col_data[1:])
    col_data = worksheet.col_values(5)  # 餐品类型2
    data.append(col_data[1:])
    col_data = worksheet.col_values(6)  # 价格
    data.append(col_data[1:])
    col_data = worksheet.col_values(7)  # 备注
    data.append(col_data[1:])

    data = np.array(data)  # [[餐品id],[餐品口味],[餐品忌口],[餐品类型1],[餐品类型2],[价格],[备注]]
    return data


def readDateList(filePath):
    data = []
    workbook = readfile(filePath)
    # 通过sheet索引获得sheet对象
    worksheet = workbook.sheet_by_index(0)
    col_data = worksheet.col_values(0)  # 获取第一列的内容 日期
    data.append(col_data[1:])
    col_data = worksheet.col_values(1)  # 星期
    data.append(col_data[1:])
    col_data = worksheet.col_values(2)  # 是否工作日
    data.append(col_data[1:])

    data = np.array(data)  # [[日期],[星期],[是否工作日]]
    return data.astype(int)  # 将数组中字符都转换为整形


def main():
    print('------------------智取乐食交易记录生成----------------')

    print('--------------------一、读取需要数据------------------')
    people = readPeopleList('E:/Text folder/智取乐食开发/用户属性new.xls')
    # people[[学号], [身高], [体重], [口味1], [口味2], [忌口], [喜爱类型1], [喜爱类型2]]
    # print(people)

    foodold = readFoodList('E:/Text folder/智取乐食开发/dataset/data.xlsx')
    # food[[餐品id],[餐品口味],[餐品忌口],[餐品类型1],[餐品类型2],[价格],[备注]]
    # foodreshape
    food = []
    for i in range(len(foodold[0])):
        food.append(foodold[:, i])
    food = np.array(food)  # 将List转换为Array便于处理

    date = readDateList('E:/Text folder/智取乐食开发/dataset/date.xlsx')
    # date[[日期],[星期],[是否工作日]]
    # print(date)
    print('数据读取完成')

    print('--------------------二、生成交易数据------------------')
    TsData = allDay(date, people, food)
    # print(TsData)  # 测试
    # print(TsData.shape)
    print(TsData[0:30])
    # print(TsData[1])


if __name__ == '__main__':
    main()
