# я недавно писал этот код для заполнения спиралью, найти его было нетрудно
# на ангеме матрицы обозначаются m*n, поэтому я так написал
import numpy as np
a = [int(i) for i in input().split()]
m = a[0]
n = a[1]
s = np.zeros((m, n), dtype=int)
s[0][0] = 1
if m >= n:
    p = 2 * n
else:
    p = 2 * m - m % 2
for g in range(p):
    k = g // 4
    if g % 2 == 0:
        if g % 4 == 0:
            for j in range(k, n - k):
                if j != 0 or k != 0:
                    s[k][j] = s[k][j - 1] + 1
        else:
            for j in range(n - k - 2, k - 1, -1):
                s[m - 1 - k][j] = s[m - 1 - k][j + 1] + 1
    else:
        if g % 4 == 1:
            for i in range(k + 1, m - k):
                s[i][n - k - 1] = s[i - 1][n - k - 1] + 1
        else:
            for i in range(m - k - 2, k, -1):
                s[i][k] = s[i + 1][k] + 1
for i in range(m):
    s[i] = s[i] * i
    print(*s[i])
