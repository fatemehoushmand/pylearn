import random

computer_number = random.randint(10,40)
count_user_number = 0
while True:
    user_number = int(input('enter your num?'))
    count_user_number = count_user_number + 1
    if computer_number== user_number :
        print('you win🥳')
        break
        
    elif computer_number>user_number:
        print('⬆️')
        
    elif computer_number<user_number:
        print('⬇️')
    
print(count_user_number)
