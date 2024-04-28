def show_chess(n, m):
    for i in range(n):
        for j in range(m):
            if (i + j) % 2 == 0:
                print("*", end="")
            else:
                print("#", end="")
        print()

n = 4
m = 8
show_chess(n, m)
   
           

