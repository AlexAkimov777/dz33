def pr(n):
    for i in range(2, n):
        if n % i == 0:
            print(i, end="*")
            pr(n // i)
            return
    print(n)


pr(int(input()))           