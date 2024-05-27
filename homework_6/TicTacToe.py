import pyfiglet
import random
from termcolor import colored, cprint
import time

def show_game_board():
    for row in game_board:
        for cell in row:
            print (cell, end=" ")
        print ()
    print ()

def check_game():
    if game_board[row][0]==game_board[row][1]==game_board[row][2]!="_" or game_board[0][col]==game_board[1][col]==game_board[2][col]!="_":
        print (player, "won.✅")
        end = time.time()
        print ("Elapsed time:", end-start, "seconds")
        exit()
    elif game_board[0][0]==game_board[1][1]==game_board[2][2]!="_" or game_board[0][2]==game_board[1][1]==game_board[2][0]!="_":
        print (player, "won.✅")
        end = time.time()
        print ("Elapsed time:", end-start, "seconds")
        exit()
    elif sum(row.count("_") for row in game_board) == 0: 
        print ("Draw")
        end = time.time()
        print ("play duration:", end-start, "seconds")
        exit()
      

title = pyfiglet.figlet_format ("Tic Tac Toe", font="slant")
print (title)
print ("Welcome. Please select game mode:")
mode = int(input("1) One Player:  \n2) Two Players: \n"))

start = time.time()

game_board = [["_", "_", "_"],
              ["_", "_", "_"],
              ["_", "_", "_"]]

show_game_board()

while True:

    if mode == 1:
        print ("Player")
        while True:
            row = int (input("row: "))
            col = int (input("col: "))
            if 0 <= row <= 2 and 0 <= col <= 2:
                if game_board [row][col] == "_":
                    game_board [row][col] = colored("X", "red")
                    break
                else:
                    print ("This cell is filled.")
            else:
                print ("The input number must be between 0 and 2.")

        show_game_board()
        player = "Player"
        check_game()

        print ("CPU")
        while True:
            row = random.randint(0,2)
            col = random.randint(0,2)
            if game_board [row][col] == "_":
                game_board [row][col] = colored("O", "blue")
                break
        
        show_game_board()
        player = "CPU"
        check_game()

    elif mode == 2:
            print ("Player 1")
            while True:
                row = int (input("row: "))
                col = int (input("col: "))
                if 0 <= row <= 2 and 0 <= col <= 2:
                    if game_board [row][col] == "_":
                        game_board [row][col] = colored("X", "red")
                        break
                    else:
                        print ("This cell is filled.")
                else:
                    print ("The input number must be between 0 and 2.")

            show_game_board()
            player = "Player 1"
            check_game()

            print ("Player 2")
            while True:
                row = int (input("row: "))
                col = int (input("col: "))
                if 0 <= row <= 2 and 0 <= col <= 2:
                    if game_board [row][col] == "_":
                        game_board [row][col] = colored("O", "blue")
                        break
                    else:
                        print ("This cell is filled.")
                else:
                    print ("The input number must be between 0 and 2.")
            show_game_board()
            player = "Player 2"
            check_game()
    else:
        while mode != 1 or 2:
            print ("Select between 1 and 2.")
            mode = int(input("1) One Player:  \n2) Two Players: \n"))
            break