import numpy as np
from kmodes.kprototypes import KPrototypes

# stocks with their market caps, sectors and countries
syms = np.genfromtxt('stocks.csv', dtype=str, delimiter=',')[:, 0]  # 编号
# print(syms)
X = np.genfromtxt('stocks.csv', dtype=object, delimiter=',')[:, 1:]  # data
X[:, 0] = X[:, 0].astype(float)

kproto = KPrototypes(n_clusters=5, init='Cao', verbose=2)
clusters = kproto.fit_predict(X, categorical=[1, 2])

# Print cluster centroids of the trained model.打印聚类中心的训练模型。
print(kproto.cluster_centroids_)
# Print training statistics打印训练统计
print(kproto.cost_)
print(kproto.n_iter_)

for s, c in zip(syms, clusters):
    print("Symbol: {}, cluster:{}".format(s, c))