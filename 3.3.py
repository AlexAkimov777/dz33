a = [int(i) for i in input().split()]
b = a[0]
c = a[1]
mi = min(a)


def nod(b, c, mi):
    if b % mi == 0 and c % mi == 0:
        return mi
    else:
        return nod(b, c, mi - 1)


d = nod(b, c, mi)
k = []
k1 = []
for i in range(-b, b + 1):
    for j in range(-c, c + 1):
        if b * j + c * i == d:
            k.append([j, i, d])
            k1.append(abs(i) + abs(j))
mi1 = min(k1)
ind1 = k1.index(mi1)
mi2 = k1[ind1]
p = k[ind1][0]
if k1.count(mi1) != 1:
    for i in range(len(k1)):
        if k1[i] == mi1:
            if k[i][0] < p:
                p = k[i][0]
                ind1 = i
print(*k[ind1])
