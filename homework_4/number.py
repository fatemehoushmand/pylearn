import math

number = int(input('please enter your num:  '))


if number<=2 :
    print('no')
else:
    result = math.factorial(number)
    print('yes') 
    print(result)