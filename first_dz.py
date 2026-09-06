#номер 2
a = int(input())
print(a%10)
#номер 4
f = open('input.txt')
k = 0
p = 1
r = 0
for line in f:
    r+=1
    if r == 1:
        l1 = line.strip()
    elif r == 2:
        l2 = line.strip()
l1 = [int(i) for i in l1.split()]
h = l1[0]
if l2 == '+':
    for i in l1:
        k += i 
if l2 == '-':
    for i in l1[1:]:
        h -= i
if l2 == '*':
    for i in l1:
        p *= i
f2 = open('output.txt', 'w')
if l2 == '+':
    f2.write(str(k))
if l2 == '-':
    f2.write(str(h))
if l2 == '*':
    f2.write(str(p))
f2.close()
f.close()
#номер 6
f = open('input.txt')
k = 0
p = 1
r = 0
n = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
k1 = ''
p1 = ''
h1 = ''
for line in f:
    r+=1
    if r == 1:
        l1 = line.strip()
    elif r == 2:
        l2 = line.strip()
    elif r == 3:
        l3 = line.strip()
l3 = int(l3)
t = [int(i, l3) for i in l1.split()]
h = t[0]
if l2 == '+':
    for i in t:
        k += i
    if k == 0:
        e1 = 1
        k1 = '0'
    elif k < 0:
        e1 = -1
    else:
        e1 = 1
    k = k*e1
    while k!=0:
        k1 = n[k%(l3)] + k1
        k = k//(l3)
    if e1 == -1:
        k1 = '-' + k1
if l2 == '-':
    for i in t[1:]:
        h -= i
    if h == 0:
        e1 = 1
        h1 = '0'
    elif h < 0:
        e1 = -1
    else:
        e1 = 1
    h = h*e1
    while h!=0:
        h1 = n[h%(l3)] + h1
        h = h//(l3)
    if e1 == -1:
        h1 = '-' + h1
if l2 == '*':
    for i in t:
        p *= i
    if p == 0:
        e1 = 1
        p1 = '0'
    elif p < 0:
        e1 = -1
    else:
        e1 = 1
    p = p*e1
    while p>0:
        p1 = n[p%(l3)] + p1
        p = p//(l3)
    if e1 == -1:
        p1 = '-' + p1
f2 = open('output.txt', 'w')
if l2 == '+':
    f2.write(k1)
if l2 == '-':
    f2.write(h1)
if l2 == '*':
    f2.write(p1)
f2.close()
f.close()