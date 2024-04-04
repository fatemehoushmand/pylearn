a = int(input('enter your first num for triangle:'))
b = int(input('enter your second num for triangle:'))
c= int(input('enter your third num for triangle:'))

if a<(b+c) and  b<(a+c) and  c<(a+b) :
    print('It is possible to draw a triangle')
    
else:
    print('impossible')
    