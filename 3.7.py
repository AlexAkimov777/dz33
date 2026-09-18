# на ангеме матрицы обозначыают m*n, поэтому я так написал
# спросил у нейронки как считать детерминант
# для случая m > n - 1 я пока не знаю метода решения (еще не проходили)
import numpy as np


def linur(m, n):
    if m < n - 1:
        k = 'решений бесконечно много'
    else:
        a = np.zeros((m, n - 1), dtype=float)
        b = np.zeros((m, 1), dtype=float)
        for i in range(m):
            p = input().split()
            a[i] = np.array(p[:n - 1], dtype=float)
            b[i] = np.array(p[n - 1], dtype=float)
        det = np.linalg.det(a)
        k = []
        for i in range(n - 1):
            a1 = a.copy()
            for j in range(m):
                a1[j][i] = b[j][0]
            det1 = np.linalg.det(a1)
        k.append(det1 / det)
    return k
