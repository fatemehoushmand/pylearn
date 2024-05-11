from math import factorial as fact



def calc_number(n, k):
    row_list = []
    
    for k in range(n+1):
        number = fact(n) / (fact(k) * fact(n-k))
            
        row_list.append(int(number))
        print(row_list)
        row_list.clear()
calc_number(3,3)