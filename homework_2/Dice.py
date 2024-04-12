import random
while True:
    x = random.randint(1,6)

    if x==6 :
        print('you are win')
        print('Roll the dice one more time')
        x = random.randint(1,6)
        
    else:
        break
print(x)   