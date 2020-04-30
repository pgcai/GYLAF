import xlrd
import pickle
import numpy as np
from kmodes import kmodes
import csv


def saveDatacsv(data, path):
    with open(path, 'w', newline='') as f:  # 采用二进制的方式处理可以省去很多问题
        # 实例化csv.writer对象
        writer = csv.writer(f)
        # 用writerows方法将数据以指定形式保存
        writer.writerows(data)


def readfile(filePath):
    workbook = xlrd.open_workbook(filePath)  # 文件路径
    return workbook


def readPeopleList(filePath):
    data = []
    workbook = readfile(filePath)
    # 通过sheet索引获得sheet对象
    worksheet = workbook.sheet_by_index(0)
    nrows = worksheet.nrows  # 获取表的行数
    for i in range(1, nrows):  # 循环逐行打印
        data.append(worksheet.row_values(i)[3:12])
    return data


def model(data):
    # 进行K-modes聚类
    km = kmodes.KModes(n_clusters=32)
    clusters = km.fit_predict(data)
    return km, clusters


def main():
    print("main")
    peopledata = readPeopleList('E:/Text folder/智取乐食开发/用户属性new.xls')
    km, cluster = model(peopledata)
    print(peopledata[0:10])
    print(km.cluster_centroids_)
    cluster = np.array(cluster)
    print(cluster[0:1000])
    print(cluster.reshape(5000, 1))
    saveDatacsv(cluster.astype(str), 'F:/Github/ZhiQuLeShi/dataset/personal_category.csv')


if __name__ == '__main__':
    main()