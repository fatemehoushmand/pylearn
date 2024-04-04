import math

print('welcom to my calc')

print('+ :sum')
print('-:sub')
print('/:div')
print('*:mul')
print('sin')
print('log')
print('sqrt')
print('cos')
print('tan')
print('cot')
print('factorial')
op = input('enter your op:')
if op=='+' or op=='-' or op=='/' or op=='*':
    a = float(input('enter the first num:'))
    b= float(input('enter the second num:'))
elif op== 'factorial':
    a = int(input('enter your num:'))

else:
    a = float(input('enter your num:'))
    
if op=='+':
    result = a+b
elif op == '-':
    result = a-b
elif op== '*':
    result = a*b
elif op== '/':
    if op== 0 :
        result = 'cannot num'
    else:
        result = a/b
elif op== 'sin':
    a = a*(math.pi/180)
    result = math.sin(a)
elif op== 'log':
    result = math.log(a)
elif op== 'sqrt':
    result = math.sqrt(a)
elif op== 'cos':
    result = math.cos(a)
elif op== 'tan':
    a = a*(math.pi/180)
    result = math.tan(a)
elif op== 'cot':
    result = 1/math.tan(a)
elif op== 'factorial':
    result = math.factorial(a)
    
print(result)
    
