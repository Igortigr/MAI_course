import numpy as np
import pandas as pd
import time


def initListWithRandomNumbers():
    arr = np.random.randint(0, 999, size=1000000)
    return arr


def calcHist(arr):
    arr_freq = pd.cut(arr, bins=10, include_lowest=True, precision=0, right=False)
    return arr_freq.value_counts()


count_time = []
for i in range(10):
    start = time.time()
    arr = initListWithRandomNumbers()
    calcHist(arr)
    end = time.time()
    count_time.append(end - start)
print('Максимальное время выполнения: ', np.array(count_time).max())
print('Минимальное время выполнения: ', np.array(count_time).min())
print('Среднее время выполнения: ', np.array(count_time).mean())
print('Весь массив: ', np.array(count_time))
