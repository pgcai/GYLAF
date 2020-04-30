from keras.models import Sequential
from keras.layers import Embedding, LSTM, Flatten, Dense
from keras.utils import to_categorical  #one_hot
import pandas as pd
import numpy as np
from matplotlib import pyplot


def load_data():
    print('---------------------数据读取-------------------')
    data = pd.read_csv('F:/Github/ZhiQuLeShi/dataset/lstm_data2.csv')
    label = pd.read_csv('F:/Github/ZhiQuLeShi/dataset/lstm_label.csv')
    return np.array(data).reshape((126, 1, 8)), np.array(label)/25  # .astype(int)


def plot_img(data):
    values = data.values
    # specify columns to plot
    groups = [0, 1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    i = 1
    # plot each column
    pyplot.figure()
    for group in groups:
        pyplot.subplot(len(groups), 1, i)
        pyplot.plot(values[:, group])
        pyplot.title(data.columns[group], y=0.5, loc='right')
        i += 1
    pyplot.show()


def sale_model(train_x, train_y, test_x, test_y):
    # design network
    model = Sequential()
    model.add(LSTM(50, input_shape=(train_x.shape[1], train_x.shape[2])))
    model.add(Dense(1))
    model.compile(loss='mae', optimizer='adam')
    # fit network
    history = model.fit(train_x, train_y, epochs=40, batch_size=7, validation_data=(test_x, test_y), verbose=2,
                        shuffle=False)
    # # plot history
    # pyplot.plot(history.history['loss'], label='train')
    # pyplot.plot(history.history['val_loss'], label='test')
    # pyplot.legend()
    # pyplot.show()
    y = model.predict(test_x)
    # 保存到文件
    model.save('F:/Github/ZhiQuLeShi/model/model14.hdf5')
    # # 从文件读取
    # model = load_model('shallownet_wieght.hdf5')
    return y


def main():
    i = 13
    data, label = load_data()
    print(data.shape)
    print(label[:, 1].shape)
    # 划分训练集，测试集
    train_data = data[:, :, 1:3][:100]
    # train_data = to_categorical(train_data)
    train_label = label[:, i][:100]
    test_data = data[:, :, 1:3][100:]
    test_label = label[:, i][100:]
    print(train_data.shape)
    print(train_label.shape)
    # plot_img(label)
    y = sale_model(train_data, train_label, test_data, test_label)
    print(test_data)
    print(test_label.reshape(26, 1))
    print(y)


if __name__ == '__main__':
    main()