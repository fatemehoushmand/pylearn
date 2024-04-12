array_1 = []

while True:
    x = input('please enter your num:')
    if x=='end':
        break
    else:
        x = int(input('please enter your num:'))
        array_1.append(x)

flag= True
n = len(array_1)    

for i in range(n-1):
    if array_1[i]>array_1[i+1]:
        flag=False
        break
if flag== True:
    print('array_1 is sorted') 
else:
    print('array_1 is not sorted') 
   
