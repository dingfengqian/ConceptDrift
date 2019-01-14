import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def SMA(data, window):
    result = []
    for i in range(len(data) - window + 1):
        each = data[i : window + i]
        result.append(np.mean(each))
    return np.array(result)

def WMA(data, window):
    result = []
    for i in range(len(data) - window + 1):
        each = data[i : window + i]
        each_w = []
        for j in range(window):
            sigma = 2*(window - j) / (window * (window + 1))   #线性权重
            each_w.append(each[window - j - 1] * sigma)
        wma_value = np.sum(each_w)
        result.append(wma_value)
    return np.array(result)

def EMA(data, window):
    a = 2 / (window + 1)
    result = []
    for i in range(len(data)):
        if i == 0:
            result.append(data[i])
        else:
            result.append(a * data[i] + (1-a) * result[-1])
    return np.array(result)

def HMA(data, window):
    a = 2 * WMA(data, int(window/2))[(window - int(window/2)):]
    b = WMA(data, window)

    result = WMA(a - b, int(np.sqrt(window)))
    return np.array(result)

if __name__ == '__main__':
    df = pd.read_csv('../data/000001_Daily_2006_2018.csv')
    close = df['Close'].as_matrix()[:100]


    window = 20
    MA20 = SMA(close, window)
    WMA20 = WMA(close, window)
    EMA20 = EMA(close, window)
    HMA20 = HMA(close, window)

    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.plot(range(len(close)), close)
    ax.plot(range(window - 1, len(MA20) + window - 1), MA20)
    ax.plot(range(window - 1, len(WMA20) + window - 1), WMA20)
    ax.plot(range(len(EMA20)), EMA20)
    ax.plot(range(int(np.sqrt(window)) - 1, len(HMA20) + int(np.sqrt(window)) - 1), HMA20)
    ax.legend(['000001','MA20', 'WMA20', 'EMA20', 'HMA20'])

    plt.show()
