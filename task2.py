from main import calcHist, initListWithRandomNumbers
import numpy as np

a = 3

'''Рисование треугольника'''


def triangle(a):
    tr = ''
    for i in range(1, a * 2 + 2, 2):
        tr += ' ' * (a - i // 2) + '*' * i + '\n'
    return tr


hist1 = calcHist(initListWithRandomNumbers())
hist2 = calcHist(initListWithRandomNumbers())

'''Декаортово расстояние гистограмм'''


def histDistance(hist1, hist2):
    S = np.sqrt(np.sum((hist1 - hist2) ** 2))
    return S


'''Сохранение гистограмма'''


def saveHist(hist):
    name = input('Введите название файла: ')
    np.save(name, hist)
    print('Гистограмма: ', hist)
    print('Гистограмма сохранилась в файл: ', name)


'''Загрузка гистограммы'''


def loadHist():
    namefile = input('Введите название файла: ')
    return np.load(namefile)


if '__main__':
    print('Декартово расстояние: ', histDistance(hist1, hist2))
    print('Треугольник:')
    print(triangle(a))