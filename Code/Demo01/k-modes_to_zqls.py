import numpy as np
from kmodes import kmodes

'''生成互相无交集的离散属性样本集'''
data1 = np.random.randint(1, 6, (10000, 10))
data2 = np.random.randint(7, 12, (10000, 10))

print(data1.shape)
print(data2.shape)
data = np.concatenate((data2, data1))

print(data.shape)

'''进行K-modes聚类'''
km = kmodes.KModes(n_clusters=2)
clusters = km.fit_predict(data)

# 打印聚类中心
print(km.cluster_centroids_)
'''计算正确归类率'''
score = np.sum(clusters[:int(len(clusters)/2)])+(len(clusters)/2-np.sum(clusters[int(len(clusters)/2):]))
print("np.sum(clusters[:int(len(clusters)/2)]):{}".format(np.sum(clusters[:int(len(clusters)/2)])))
print(clusters[:int(len(clusters)/2)])
print("np.sum(clusters[int(len(clusters)/2):]):{}".format(np.sum(clusters[int(len(clusters)/2):])))
print(clusters[int(len(clusters)/2):])
score = score/len(clusters)
score = score/len(clusters)
if score >= 0.5:
    print('正确率：' + str(score))
else:
    print('正确率：' + str(1-score))