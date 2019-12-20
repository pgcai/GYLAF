import pickle
import numpy as np
import random
import xlwt


def readfile(filePath):
    with open(filePath, 'rb') as f:
        Data = pickle.load(f)
        name = Data['name']
        sex = Data['sex']
    return name, sex


def makeAllData(name, sex):
    allData = []
    for i in range(len(name)):
        oneData = makeOneData(name[i], sex[i])
        allData.append(oneData)
    allData_r = np.array(allData)
    return allData_r


def makeOneData(name, sex):
    oneData = []
    oneData.append(name)
    oneData.append(sex)
    oneData.append(generateAge())
    heiget, weight = generateHeight_Weight(sex)
    oneData.append(heiget)
    oneData.append(weight)
    oneData.append(generateProvences())
    taste1, taste2 = generateTaste()
    oneData.append(taste1)
    oneData.append(taste2)
    oneData.append(generateAvoid())
    foodT1, foodT2 = generateTypeFood()
    oneData.append(foodT1)
    oneData.append(foodT2)
    return oneData


def generateAge():
    age = np.random.normal(20, scale=1, size=None)
    return int(age)


def generateHeight_Weight(sex):
    if sex == '男':
        height = np.random.normal(170, scale=7, size=None)
        weight = np.random.normal(loc=(int(height)-80)*0.7, scale=5, size=None)
    else:
        height = np.random.normal(159, scale=7, size=None)
        weight = np.random.normal(loc=(int(height) - 86) * 0.7, scale=5, size=None)
    return int(height), int(weight)


def generateProvences():
    provenceslist = ['北京市', '天津市', '上海市', '重庆市',
                     '河北省', '山西省', '辽宁省', '吉林省',
                     '黑龙江省', '江苏省', '浙江省', '安徽省',
                     '福建省', '江西省', '山东省', '河南省',
                     '湖北省', '湖南省', '广东省', '海南省',
                     '四川省', '贵州省', '云南省', '陕西省',
                     '甘肃省', '青海省', '内蒙古自治区',
                     '广西壮族自治区', '西藏自治区',
                     '宁夏回族自治区', '新疆维吾尔自治区']  # 31个 部分除外
# ['北京市/0.005', '天津市/0.08', '上海市0.012', '重庆市0.02',
# '河北省0.047', '山西省'0.040, '辽宁省0.039', '吉林省'0.039,
# '黑龙江省0.039', '江苏省'0.035, '浙江省0.035', '安徽省'0.035,
# '福建省0.035', '江西省'0.046, '山东省0.046', '河南省'0.047,
# '湖北省0.037', '湖南省'0.037, '广东省'0.035, '海南省'0.030,
# '四川省0.035', '贵州省'0.030, '云南省'0.035, '陕西省'0.035,
# '甘肃省'0.030, '青海省0.016', '内蒙古自治区0.020',
# '广西壮族自治区0.02', '西藏自治区0.01',
# '宁夏回族自治区0.01', '新疆维吾尔自治区0.02']
    RandomParameters = [0.005, 0.080, 0.012, 0.020,
                        0.047, 0.040, 0.039, 0.039,
                        0.035, 0.035, 0.035, 0.035,
                        0.039, 0.046, 0.046, 0.047,
                        0.037, 0.037, 0.035, 0.030,
                        0.035, 0.030, 0.035, 0.035,
                        0.030, 0.010, 0.020, 0.020,
                        0.010, 0.016, 0.020]

    provences = random_pick(provenceslist, RandomParameters)

    return provences


def random_pick(some_list, probabilities):
    x = random.uniform(0, 1)
    cumulative_probability = 0.0
    for item, item_probability in zip(some_list, probabilities):
        cumulative_probability += item_probability
        if x < cumulative_probability:
            break
    return item


def generateTaste():
    taste = ['T1', 'T2', 'T3', 'T4', 'T5']
    r1 = [0.32, 0.3, 0.22, 0.03, 0.1]
    peopleTaste1 = random_pick(taste, r1)
    n1 = ['T2', 'T3', 'T4', 'T5']  # 酸 T1
    t1 = [0.53, 0.39, 0.04, 0.04]
    n2 = ['T1', 'T3', 'T4', 'T5']  # 甜 T2
    t2 = [0.51, 0.36, 0.04, 0.09]
    n3 = ['T1', 'T2', 'T4', 'T5']  # 辣 T3
    t3 = [0.42, 0.40, 0.04, 0.14]
    n4 = ['T1', 'T2', 'T3', 'T5']  # 咸 T4
    t4 = [0.20, 0.20, 0.20, 0.40]
    n5 = ['T1', 'T2', 'T3', 'T4']  # 香 T5
    t5 = [0.13, 0.28, 0.37, 0.22]
    if peopleTaste1 == 'T1':
        peopleTaste2 = random_pick(n1, t1)
    elif peopleTaste1 == 'T2':
        peopleTaste2 = random_pick(n2, t2)
    elif peopleTaste1 == 'T3':
        peopleTaste2 = random_pick(n3, t3)
    elif peopleTaste1 == 'T4':
        peopleTaste2 = random_pick(n4, t4)
    else:
        peopleTaste2 = random_pick(n5, t5)
    return peopleTaste1, peopleTaste2


def generateAvoid():
    avo = ['A1', 'A2', 'A3', 'A4', 'A0']
    r = [0.05, 0.05, 0.05, 0.05, 0.8]
    avoid = random_pick(avo, r)
    return avoid


def generateTypeFood():
    typeFood = ['P1', 'P2', 'P3', 'P4', 'P5', 'P6', 'P7']
    r = [0.35, 0.20, 0.10, 0.20, 0.05, 0.1]
    love1 = random_pick(typeFood, r)
    for i in range(100):
        love2 = random_pick(typeFood, r)
        if love2 != love1:
            break
    return love1, love2


def main():
    print('------------------智取乐食数据生成----------------')
    name, sex = readfile('E:/Text folder/智取乐食开发/Name_Sex.pkl')
    print(name)
    print(sex)
    allPeople = makeAllData(name, sex)
    print(allPeople[100:150])
    print(len(allPeople))

    # ------------------------------------------------------
    # 利用xlwt模块对xls进行写的操作
    # 创建一个Workbook对象，相当于创建了一个Excel文件
    data = xlwt.Workbook(encoding='utf-8', style_compression=0)

    # 创建一个sheet对象，一个sheet对象对应Excel文件中的一张表格。
    sheet = data.add_sheet('test01', cell_overwrite_ok=True)
    # 其中的test是这张表的名字,cell_overwrite_ok，表示是否可以覆盖单元格
    # 其实是Worksheet实例化的一个参数，默认值是False

    # 填入第一行
    Project = ['学号', '姓名', '性别', '年龄', '身高', '体重', '籍贯',
               '口味1', '口味2', '忌口', '喜爱食物类型1', '喜爱食物类型2']
    for i in range(0, len(Project)):
        sheet.write(0, i, Project[i])

    # 填入第一列学号
    for i in range(0, len(allPeople)):
        sheet.write(i + 1, 0, '1020'+str(i+1).zfill(4))

    # 填入第2-n列
    for i in range(1, len(Project)):
        for j in range(len(allPeople)):
            # print(len(allPeople[:, i]))  # 测试用
            sheet.write(j + 1, i, allPeople[j, i-1])

    # 最后，将以上操作保存到指定的Excel文件中
    data.save('E:/Text folder/智取乐食开发/用户属性new2.xls')


if __name__ == '__main__':
    main()
