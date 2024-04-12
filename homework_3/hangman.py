import random

words_bank = ['tree','book','blue','train','fish','woman','life','iran']

user_mistakes = 0
good_chars = []
bad_chars = []
score = 0
word = random.choice(words_bank)

while user_mistakes<6 :
    for i in range(len(word)):
        if word[i] in good_chars:
            print(word[i] , end=' ')
        else:
            print('_' , end=' ')
    user_char = input('please write your guess:')
    l_user_char=user_char.lower()
    
    if len(l_user_char)==1:
        if l_user_char in word:
            good_chars.append(l_user_char)
            print('✅')
            score +=1
        else:
            bad_chars.append(l_user_char)
            user_mistakes += 1
            print('❌')
    else:
        print('please write again')
    if score== len(word):
        print('you win')
        break
    if user_mistakes== 6:
        print('game over')
