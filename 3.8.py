# спросил у нейронки про модуль random и условие задачи
# + random.gauss(0, 1) обозначает что-то типа крестов погрешности
import random


def mnkdan(n, a, b):
    x = []
    y = []
    for _ in range(n):
        x1 = random.gauss(0, 100)
        x1 = random.gauss(0, 1) + x1
        y1 = a * x1 + b + random.gauss(0, 1)
        x.append(x1)
        y.append(y1)
    return x, y
