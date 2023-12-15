import pyfiglet
import random
from colorama import Fore, Back, Style, init
import time
init()
print("If you want to play with PC Enter = 1")
print("If you want to play with ypur friend Enter = 2")

while True:
    choice = int(input("Enter Your Game Mood: "))
    start_time = time.time()
    if choice == 2:
        title = pyfiglet.figlet_format("TicTacToe - Friendship",font="slant")
        print(title)

        def show():
            for row in game_board:
                for cell in row:
                    if cell == "X":
                        print(Fore.BLUE + cell + Style.RESET_ALL, end=" ")
                    elif cell == "O":
                        print(Fore.RED + cell + Style.RESET_ALL, end=" ")
                    else:
                        print(cell, end=" ")
                print()

        def check_game():
            game_over = False
            
            for i in range(3):
                if game_board[i][0] == game_board[i][1] == game_board[i][2] == "X":
                    print("Player 1 win 🎉")
                    game_over = True

                if game_board[0][i] == game_board[1][i] == game_board[2][i] == "X":
                    print("Player 1 win 🎉")
                    game_over = True
            for i in range(3):
                if game_board[i][0] == game_board[i][1] == game_board[i][2] == "O":
                    print("Player 2 win 🎉")
                    game_over = True

                if game_board[0][i] == game_board[1][i] == game_board[2][i] == "O":
                    print("Player 2 win 🎉")
                    game_over = True

            if game_board[0][0] == game_board[1][1] == game_board[2][2] == "X":
                print("Player 1 win 🎉")
                game_over = True
            if game_board[0][2] == game_board[1][1] == game_board[2][0] == "X":
                print("Player 1 win 🎉")
                game_over = True
            if game_board[0][0] == game_board[1][1] == game_board[2][2] == "O":
                print("Player 2 win 🎉")
                game_over = True
            if game_board[0][2] == game_board[1][1] == game_board[2][0] == "O":
                print("Player 2 win 🎉")
                game_over = True

            if all(cell != "-" for row in game_board for cell in row) and game_over == False:
                print("It's a tie! 😐")
                game_over = True
            return game_over

        game_board = [["-" ,"-", "-"],
                    ["-" ,"-", "-"],
                    ["-" ,"-", "-"],]
        show()

        while True:
            print("Player 1: ")

            while True:
                row = int(input("row: "))
                col = int(input("col: "))

                if 0 <=row <= 2 and 0 <=col <= 2:
                    if game_board[row][col] == "-":
                        game_board[row][col] = "X"
                        break  
                    else:
                        print("Dont try to cheat😡 ")
                else:
                    print("Enter the write value between 0,1,2 ")
            show()
            if check_game():
                break

            print("Player 2: ")

            while True:
                row = int(input("row: "))
                col = int(input("col: "))

                if 0 <=row <= 2 and 0 <=col <= 2:
                    if game_board[row][col] == "-":
                        game_board[row][col] = "O"
                        break
                    else:
                        print("Dont try to cheat😡 ")
                else:
                    print("Enter the write value between 0,1,2 ")
            show()
            if check_game():
                break
        end_time = time.time()
        total_time = end_time - start_time
        print("Game Duration is(s):" ,total_time)
        break
    elif choice == 1:
        title = pyfiglet.figlet_format("TicTacToe - PC Mood",font="slant")
        print(title)

        def show():
            for row in game_board:
                for cell in row:
                    if cell == "X":
                        print(Fore.BLUE + cell + Style.RESET_ALL, end=" ")
                    elif cell == "O":
                        print(Fore.RED + cell + Style.RESET_ALL, end=" ")
                    else:
                        print(cell, end=" ")
                print()

        def check_game():
            game_over = False
            
            for i in range(3):
                if game_board[i][0] == game_board[i][1] == game_board[i][2] == "X":
                    print("Player 1 win 🎉")
                    game_over = True

                if game_board[0][i] == game_board[1][i] == game_board[2][i] == "X":
                    print("Player 1 win 🎉")
                    game_over = True
            for i in range(3):
                if game_board[i][0] == game_board[i][1] == game_board[i][2] == "O":
                    print("PC win 💻")
                    game_over = True

                if game_board[0][i] == game_board[1][i] == game_board[2][i] == "O":
                    print("PC win 💻")
                    game_over = True

            if game_board[0][0] == game_board[1][1] == game_board[2][2] == "X":
                print("Player 1 win 🎉")
                game_over = True
            if game_board[0][2] == game_board[1][1] == game_board[2][0] == "X":
                print("Player 1 win 🎉")
                game_over = True
            if game_board[0][0] == game_board[1][1] == game_board[2][2] == "O":
                print("PC win 💻")
                game_over = True
            if game_board[0][2] == game_board[1][1] == game_board[2][0] == "O":
                print("PC win 💻")
                game_over = True

            if all(cell != "-" for row in game_board for cell in row) and game_over == False:
                print("It's a tie! 😐")
                game_over = True
            return game_over

        game_board = [["-" ,"-", "-"],
                    ["-" ,"-", "-"],
                    ["-" ,"-", "-"],]
        show()

        while True:
            print("Player 1: ")

            while True:
                row = int(input("row: "))
                col = int(input("col: "))

                if 0 <=row <= 2 and 0 <=col <= 2:
                    if game_board[row][col] == "-":
                        game_board[row][col] = "X"
                        break  
                    else:
                        print("Dont try to cheat😡 ")
                else:
                    print("Enter the write value between 0,1,2 ")
            show()
            if check_game():
                break

            print("PC: ")

            while True:
                row = random.randint(0,2)
                col = random.randint(0,2)

                if game_board[row][col] == "-":
                    game_board[row][col] = "O"
                    break
            
            show()
            if check_game():
                break
        end_time = time.time()
        total_time = end_time - start_time
        print("Game Duration is(s):" ,total_time)
        break
    else:
        print("Please chose the correct mood for your game !!")