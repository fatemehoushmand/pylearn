name = input('enter your name:')
family = input('enter your family:')
math = float(input('enter your Math grade:'))
chem = float(input('enter your Chemistry grade:'))
his = float(input('enter your history grade:'))

average = (math + chem + his) / 3
print(average)

if average>= 17:
    print('great')
elif 17>average>=12:
    print('normal')
elif average<12:
    print('fail')
