from math import factorial as fact 


def calc_number(n, k):
    number = fact(n) / (fact(k) * fact(n-k))

    return number


def pascal_triangle(n):
    row_list = []

    for row in range(n):
        for k in range(row+1):
            number = calc_number(row, k)
            row_list.append(int(number))
        print(row_list)
        row_list.clear()


pascal_triangle(10)

