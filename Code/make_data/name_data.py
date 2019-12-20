import pandas as pd
import numpy as np


def readfile():
    People_data = pd.read_csv('data/train_weather.csv', encoding='gb18030', low_memory=False)
    return People_data

# print(weather_data.shape)  # 测试用
# print(weather_data.columns)
# print(weather_data.index)
# print(rice_data.columns)

# 将训练数据读入并以列表形式返回


def re_train_data(weather_data):
    weather_data_re = []
    cols = weather_data[['区县id', '站名id', '年份', '月份', '日期', '日照时数（单位：h)', '日降水量（mm）',
                         '日最高温度（单位：℃）', '日最低温度（单位：℃）', '日平均温度（单位：℃）',
                         '日相对湿度（单位：%）']]
    # print(cols)  # 测试用
    for i in range(1, 89):
        # print(i)  # 测试用
        county_name = 'county' + str(int(i))
        # print(county_name)  # 测试用
        one_county = cols[(cols['区县id'] == county_name)]
        # print(county_name, one_county.shape)  # 测试用
        for j in range(2015, 2018):
            # print(j)  # 测试用
            one_county_year = one_county[(one_county['年份'] == j) & (one_county['站名id'] == 1)]
            # one_county_year_id1 = one_county_year[(one_county_year['站名id'] == 1)]
            if (((j % 4 == 0) and (j % 100 != 0)) or (j % 400 == 0)):
                # print(i,j)  # 测试用
                one_county_year = one_county_year[~((one_county_year['日期'] == 29) & (one_county_year['月份'] == 2))]
                # print(one_county_year)
            # print(one_county_year.shape)  # 测试用
            one_county_year = one_county_year[['区县id', '月份', '日期', '日照时数（单位：h)', '日降水量（mm）',
                                               '日最高温度（单位：℃）', '日最低温度（单位：℃）', '日平均温度（单位：℃）',
                                               '日相对湿度（单位：%）']]
            weather_data_re_one = one_county_year.values.tolist()
            # print(weather_data_re_one)
            weather_data_re.append(weather_data_re_one)
            # print(weather_data_re_one.shape)
            # weather_data_re += [one_county_year.values.tolist()]
    # print(weather_data_re)  # 测试用
    # print(np.array(weather_data_re).shape)  # 测试用
    return weather_data_re

# 将训练标签读入并以列表返回


def re_train_label(rice_data):
    rice_data_re = []
    cols = rice_data[['区县id', '2015年早稻', '2016年早稻', '2017年早稻', '2015年晚稻',
                      '2016年晚稻', '2017年晚稻']]
    for i in range(1, 89):
        # print(i)  # 测试用
        county_name = 'county' + str(int(i))
        # print(county_name)  # 测试用
        one_county = cols[(cols['区县id'] == county_name)]
        # print(one_county)
        # print(county_name, one_county.shape)  # 测试用
        for j in range(2015, 2018):
            year_name1 = str(int(j)) + '年早稻'
            year_name2 = str(int(j)) + '年晚稻'
            # print(year_name1)  # 测试用
            label_one = one_county[['区县id', year_name1, year_name2]]
            label_one_list = label_one.values.tolist()
            rice_data_re.extend(label_one_list)
            # print(label_one_list)

    # print(rice_data_re)  # 测试用
    # print(np.array(rice_data_re).shape)  # 测试用
    return rice_data_re

# 将无用数据剔除


def train_data(weather_data, rice_data):
    data_re = []
    data_re_new = []
    data = re_train_data(weather_data)  # 测试用
    label = re_train_label(rice_data)  # 测试用
    for i in range(len(data)):
        # print(i)  # 测试
        for j in range(len(label)):
            if data[i][0][0] == label[j][0]:
                # 写入数据
                data_re.append(data[i])
                break
    # print(np.array(data_re).shape)
    for k in range(len(data_re)):
        data_re_one = np.delete(data_re[k], 0, axis=1)
        data_re_one = data_re_one.tolist()
        data_re_new.append(data_re_one)
    # print(data_re_new)
    print(np.array(data_re_new).shape)
    label_re = np.delete(label, 0, axis=1)
    label_re = np.delete(label_re, 0, axis=1)
    # print(label_re)
    print(label_re.shape)
    data_re_new = np.array(data_re_new)
    label_re = np.array(label_re)
    # 数据清洗
    for i in range(len(data_re_new)):
        for j in range(len(data_re_new[0])):
            for k in range(len(data_re_new[0][0])):
                if(data_re_new[i][j][k] == "/" or data_re_new[i][j][k] == "*"):
                    data_re_new[i][j][k] = 0
                    print("数据清洗中....")
    return np.array(data_re_new), np.array(label_re)

weather_data, rice_data = readfile()
weather_data_re, rice_data_re = train_data(weather_data, rice_data)
print(weather_data_re)
print(rice_data_re)
