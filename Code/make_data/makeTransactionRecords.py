import pickle
import numpy as np
import random
import xlrd
import xlwt
import math
import csv


def allDay(date, people, food):
    # date[0]日期 date[1]星期 date[2]是否工作日
    TsData = []
    # for i in range(5):  # 测试用
    for i in range(len(date[0])):
        oneDayData = oneDay(date[:, i], people, food)
        TsData.extend(oneDayData)
    TsData = np.array(TsData)
    return TsData


def oneDay(date, people, food):
    oneDayDate = []
    # date[0]日期 date[1]星期 date[2]是否工作日
    i = 0
    while i < (len(people[0])):  # allPeople
        if skip(date[2], people[8][i]):  # 根据日期选择是否不在餐厅
            # print("跳过这个人") # test
            i += 1
            continue
        onepeopleData = onePeople(date, people[:, i], food)
        oneDayDate.append(onepeopleData)
        if np.random.random_sample() < 0.8:  # 0.8概率再打二份菜
            onepeopleData = onePeople(date, people[:, i], food)
            oneDayDate.append(onepeopleData)
        if np.random.random_sample() < 0.1:  # 0.1概率再打三份菜
            onepeopleData = onePeople(date, people[:, i], food)
            oneDayDate.append(onepeopleData)
        i += 1
    return oneDayDate


def skip(date, region):
    # print(date)  # test
    if date == 0:
        # print('双休')
        if region == '天津市':
            # print('天津市')  # test
            if np.random.random_sample() < 0.50:  # 天津 0.2概率不在餐厅吃
                # print('跳过')  # test
                return True
            else:
                return False
        else:
            if np.random.random_sample() < 0.08:  # 外地 0.03概率不在餐厅吃
                return True
            else:
                return False
    elif date == 1:
        # print('工作日')
        if region == '天津':
            if np.random.random_sample() < 0.08:  # 天津 0.05概率不在餐厅吃
                return True
            else:
                return False
        else:
            if np.random.random_sample() < 0.05:  # 外地 0.01概率不在餐厅吃
                return True
            else:
                return False
    elif date == 3:
        # print("??")
        if region == '天津':
            if np.random.random_sample() < 0.30:  # 天津 0.2概率不在餐厅吃
                return True
            else:
                return False
        else:
            if np.random.random_sample() < 0.10:  # 外地 0.03概率不在餐厅吃
                return True
            else:
                return False
    else:  # 强节日
        if region == '天津':
            if np.random.random_sample() < 0.70:  # 天津 0.2概率不在餐厅吃
                return True
            else:
                return False
        else:
            if np.random.random_sample() < 0.30:  # 外地 0.03概率不在餐厅吃
                return True
            else:
                return False


def onePeople(date, people, food):
    # people[[学号], [身高], [体重], [口味1], [口味2], [忌口], [喜爱类型1], [喜爱类型2], [地区]]
    # food[[餐品id],[餐品口味],[餐品忌口],[餐品类型1],[餐品类型2],[价格],[备注]]
    peopleData = []
    # return[[用户id],[消费食物id],[消费质量],[消费金额],[消费时间]]

    # 用户id
    peopleData.append(people[0])

    # 消费食物id
    selectfd = selectFood(people[3:], food)
    peopleData.append(selectfd)

    # 消费食物的单价
    thefood = food[food[:, 0] == selectfd]
    price = float(thefood[:, 5])
    peopleData.append(price)

    # 消费质量
    height = people[1].astype(int)
    weight = people[2].astype(int)
    foodweight = calculateWeight(height, weight)
    peopleData.append(foodweight)

    # 消费金额
    money = foodweight*price
    peopleData.append(format(money, '.3f'))

    # 消费时间
    consumeDate = date[0]
    peopleData.append(consumeDate)
    return peopleData


def calculateWeight(height, weight):  # 餐品质量/重量
    BMI = weight/(math.pow(height/100, 2))
    foodweight = np.random.normal(loc=200 + (BMI - 21.2)*9, scale=50, size=None)
    # print(BMI)
    return int(foodweight)


def selectFood(people, food):
    # people[[口味1], [口味2], [忌口], [喜爱类型1], [喜爱类型2]]
    # food[[餐品id],[餐品口味],[餐品忌口],[餐品类型1],[餐品类型2],[价格],[备注]]
    # 喜爱食物类型1包含的食物
    thefood0 = food[food[:, 3] == people[3]]
    thefood1 = food[food[:, 4] == people[3]]
    thefoodone = np.vstack((thefood0, thefood1))
    if people[2] != 'A0':
        thefoodone = thefoodone[~(thefoodone[:, 2] == people[2])]
    # print('----------h1--------')  # test
    # print(thefoodone)
    # print(people[2])
    # print('----------t1--------')

    # 喜爱食物类型2包含的食物
    thefood0 = food[food[:, 3] == people[4]]
    thefood1 = food[food[:, 4] == people[3]]
    thefoodtwo = np.vstack((thefood0, thefood1))
    if people[2] != 'A0':
        thefoodtwo = thefoodtwo[~(thefoodtwo[:, 2] == people[2])]
    # print('----------h2--------')  # test
    # print(thefoodtwo)
    # print(people[2])
    # print('----------t2--------')
    if np.random.random_sample() < 0.90:  # 0.9:0.1   按规律饮食 ：随机选一个
        if np.random.random_sample() < 0.70 and thefoodone.size != 0:
            s = np.random.randint(0, high=len(thefoodone), dtype='l')
            selectfood = thefoodone[s, 0:3]
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
    # while(selectfood[2] == people[2]):  # 判断忌口
    #     if people[2] == 'A0':
    #         break
    #     s = np.random.randint(0, high=len(food), dtype='l')
    #     # print(s)
    #     selectfood = food[s, 0:3]
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
    col_data = worksheet.col_values(6)  # 地区
    data.append(col_data[1:])
    data = np.array(data)  # [[学号], [身高], [体重], [口味1], [口味2], [忌口], [喜爱类型1], [喜爱类型2], [地区]]
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


def saveDataxls(alldata):
    # 利用xlwt模块对xls进行写的操作
    # 创建一个Workbook对象，相当于创建了一个Excel文件
    data = xlwt.Workbook(encoding='utf-8', style_compression=0)

    # 创建一个sheet对象，一个sheet对象对应Excel文件中的一张表格。
    sheet = data.add_sheet('test01', cell_overwrite_ok=True)
    # 其中的test是这张表的名字,cell_overwrite_ok，表示是否可以覆盖单元格
    # 其实是Worksheet实例化的一个参数，默认值是False

    # 填入第一行
    Project = ['学号', '食物id', '食物单价', '盛取质量', '消费金额', '消费时间']
    for i in range(0, len(Project)):
        sheet.write(0, i, Project[i])

    # 填入第一列学号
    for i in range(0, len(alldata)):
        sheet.write(i + 1, 0, alldata[i, 0])

    # 填入第2-n列
    for i in range(1, len(Project)):
        for j in range(len(alldata)):
            # print(len(allPeople[:, i]))  # 测试用
            sheet.write(j + 1, i, alldata[j, i])

    # 最后，将以上操作保存到指定的Excel文件中
    data.save('F:/Github/ZhiQuLeShi/dataset/交易记录.xls')


def saveDatacsv(alldata):
    with open('F:/Github/ZhiQuLeShi/dataset/交易记录.csv', 'w', newline='') as f:  # 采用二进制的方式处理可以省去很多问题
        # 实例化csv.writer对象
        writer = csv.writer(f)
        # 用writerows方法将数据以指定形式保存
        writer.writerows(alldata)

def main():
    print('------------------智取乐食交易记录生成----------------')

    print('--------------------一、读取需要数据------------------')
    people = readPeopleList('E:/Text folder/智取乐食开发/用户属性new.xls')
    # people[[学号], [身高], [体重], [口味1], [口味2], [忌口], [喜爱类型1], [喜爱类型2], [地区]]
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
    TsData = allDay(date[:, 63:190], people, food)
    # print(TsData)  # 测试
    # print(TsData.shape)
    print(TsData[0:30])
    # print(TsData[1])

    print('--------------------三、保存数据------------------')
    # saveDataxls(TsData)  # emmm保存为xls会越界
    saveDatacsv(TsData)  # 保存为csv格式
    print(TsData.shape)


if __name__ == '__main__':
    main()
