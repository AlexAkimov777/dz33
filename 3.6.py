# я не знаю все возможности numpy, но я подумал что он умеет суммировать
# квадраты и т.д., поэтому я спрашивал у нейронки как это делать можно
import numpy as np


def mnk(x, y):
    x = np.array(x, dtype=float)
    y = np.array(y, dtype=float)
    n = len(x)
    sredx = np.sum(x) / n
    sredy = np.sum(y) / n
    sredx2 = np.sum(x ** 2) / n
    sredxy = np.sum(x * y) / n
    k = (sredxy - sredx * sredy) / (sredx2 - sredx ** 2)
    b = sredy - k * sredx
    return k, b
