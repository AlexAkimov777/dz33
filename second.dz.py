#a = [int(i) for i in input().split()]
#n = a[0]
#del a[0]
#k = 0
#p = 0
#for i in a:
#    k += i
#for i in range (1, n+1):
#    p += i
#print(p-k)

#a = input().split()
#n = int(a[0])
#del a[0]
#p = []
#for i in range (len(a[0])):
#    p.append(a[0][i])
#n1 = len(p)
#k = []
#for i in range (n):
#    for j in range (n):
#        k.append(p[n*(i+1)-j-1])
#print("".join(k))

# я спросил у нейронке расшифровать условие(я понял)
"""
a = input()
p = []
n = len(a)
k = 0
for i in range (len(a)):
    p.append(a[i])
y = p.count('E')+p.count('J')+p.count('S')+p.count('Z')
for i in range (len(p)):
    if p[i] == 'E' and p[n-1-i] == '3':
        k += 1
    if p[i] == 'J' and p[n-1-i] == 'L':
            k += 1
    if p[i] == 'S' and p[n-1-i] == '2':
            k += 1
    if p[i] == 'Z' and p[n-1-i] == '5':
            k += 1
p1 = p.reverse()
if p == p1:
    if k == y and k != 0:
        print(f"{a} is a mirrored palindrome.")
    else:
        print(f"{a} is not a palindrome.")
elif k == y and k != 0:
    print(f"{a} is a mirrored string.")
else:
    print(f"{a} is not a palindrome.")
"""

"""
a = input().split()
for i in range (len(a)//2):
     a[2*(i)], a[2*(i)+1] = a[2*(i)+1], a[2*(i)]
print(''.join(a))
"""

"""
a = input().split()
a[0], a[1:len(a)] = a[len(a)-1], a[0:len(a)-1]
print("".join(a))
"""

a = input().split()
for i in a:
    if a.count(i) == 1:
        print(i)