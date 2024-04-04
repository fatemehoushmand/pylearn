import random

score_computer = 0
score_user =  0



while True:
    x = random.randint(1,3)
    
    if x== 1 :
        computer_choice = 'paper'
    elif x== 2 :
        computer_choice = 'rock'
    elif x== 3 :
        computer_choice = 'scissors'
        
    user_choice = input('enter your choice:')
    
    print('💻',computer_choice)
    print('🙋‍♂️',user_choice)

    if computer_choice == user_choice :
        print('you are ewen!')
        break
    elif computer_choice == 'paper' and user_choice =='rock':
        print('💻 win')
        score_computer = score_computer + 1   
    elif computer_choice == 'rock' and user_choice=='paper' :
        print('🙋‍♂️ win')
        score_user = score_user + 1
    elif computer_choice =='scissors' and user_choice=='paper':
        print('💻 win')
        score_computer = score_computer + 1
    elif computer_choice=='paper' and user_choice=='scissors':
        print('🙋‍♂️ win')
        score_user = score_user + 1
    elif computer_choice=='rock' and user_choice=='scissors':
        print('💻 win')
        score_computer = score_computer+1
    elif computer_choice=='scissors' and user_choice=='rock':
        print('🙋‍♂️ win')
        score_user =score_user+1
        
print(score_user)
print(score_computer)    
        