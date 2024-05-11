import pyfiglet
import time
import random
from termcolor import colored

def show():
    for row in game_board:
        for cell in row:
            print(cell,end='')
        print()
        
def check_game():
    num=0
    for i in range(3):
        if game_board[row][0]==game_board[row][1]==game_board[row][2]!="_" or game_board[0][col]==game_board[1][col]==game_board[2][col]!="_":
            print ('player-1', "✅")
            end = time.time()
            print ("Time:",end-start)
            exit()
        elif game_board[0][0]==game_board[1][1]==game_board[2][2]!="_" or game_board[0][2]==game_board[1][1]==game_board[2][0]!="_":
            print ('player-2', "✅")
            end = time.time()
            print ( "Time:",end-start)
            exit()
        for j in range(3):
            if game_board[i][j]=="-":
                num=num+1
    if num==0:
        if not(game_board[i][0]==game_board[i][1]==game_board[i][2]=="X" or game_board[0][i]==game_board[1][i]==game_board[2][i]=="X" or game_board[0][0]==game_board[1][1]==game_board[2][2]=="X" or game_board[0][2]==game_board[1][1]==game_board[2][0]=="X" or game_board[i][0]==game_board[i][1]==game_board[i][2]=="O" or game_board[0][i]==game_board[1][i]==game_board[2][i]=="O" or game_board[0][0]==game_board[1][1]==game_board[2][2]=="O" or game_board[0][2]==game_board[1][1]==game_board[2][0]=="O"):
            print("no one wins")
            end=time.time()
            print("Time:",end-start)
            exit()
      
        
title = pyfiglet.figlet_format('Tic Tac Toe',font ='slant')
print(title)

print ("new game:")
com_player = int(input("1) computer   \n2) player \n"))

game_board = [['-','-','-'],
              ['-','-','-'],
              ['-','-','-']]

show()
start=time.time()

while True:
    print('player 1')
    
    while True:
        row = int(input('row: '))
        col = int(input('col: '))
        
        if 0 <= row <= 2 and 0 <= col <= 2:
            if game_board[row][col] == '-':
                game_board[row][col] = colored("X", "red")
                break
            else:
                print('jer nazan!')
        else:
            print('please write again!')
            
    show()
    check_game()
    
    print('player 2')
    while True:
        if com_player==2:
            row=int(input(" row:"))
            col=int(input(" col:"))
        else:
            row=random.randint(0,2)
            col=random.randint(0,2)
        
        
        if 0 <= row  and row <= 2 and  0 <= col and col <= 2:
            if game_board[row][col] == '-':
                game_board[row][col] = colored("O","blue")
                break
            else:
                print('jer nazan!')
        else:
            print('please write again!')
    show()
    check_game()        

    
