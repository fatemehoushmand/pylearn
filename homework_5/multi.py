def multi(n, m):
    for i in range(1, n+1):
        for j in range(1, m+1):
            print(i * j, end=" ")
        print()


n = 10
m=10
multi(n,m)