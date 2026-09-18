a = input().split()
size = int(a[0])
symb = a[1]


def tre(si, sy):
    k = size - si + 1
    if k > size:
        return
    if k > (size + 1) / 2:
        k = size - k + 1
    print(k * sy)
    tre(si - 1, sy)


tre(size, symb)
