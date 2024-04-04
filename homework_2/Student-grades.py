while True:
    
    math = float(input('enter your Math grade:'))
    chem = float(input('enter your Chemistry grade:'))
    his = float(input('enter your history grade:'))
    x = input('Enter the (exit) word if you finish the scores:')
    average = (math + chem + his) / 3
    if x=='exit':
        break
    
print(average)