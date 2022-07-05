import random
import time

gamerunning = True

print()
print("     *** Let's play Naughts and Crosses! *** ")

board = [[" ","a","b","c"],
         ["1","-","-","-"],
         ["2","-","-","-"],
         ["3","-","-","-"]]

def print_board():
    print()
    for x in board:
        print(x)
    print()

def add_cross():
    x = input("""Player 'Cross' - Where do you want to place a cross? 
Choose location and press enter: """).strip().lower()
    if (x == "a1") and (board[1][1] == "-"):
        board[1][1] = "X"
    elif (x == "a2") and (board[2][1] == "-"):
        board[2][1] = "X"
    elif (x == "a3") and (board[3][1] == "-"):
        board[3][1] = "X"

    elif (x == "b1") and (board[1][2] == "-"):
        board[1][2] = "X"
    elif (x == "b2") and (board[2][2] == "-"):
        board[2][2] = "X"
    elif (x == "b3") and (board[3][2] == "-"):
        board[3][2] = "X"

    elif (x == "c1") and (board[1][3] == "-"):
        board[1][3] = "X"
    elif (x == "c2") and (board[2][3] == "-"):
        board[2][3] = "X"
    elif (x == "c3") and (board[3][3] == "-"):
        board[3][3] = "X"
    else:
        time.sleep(0.5)
        print()
        print("Sorry, invalid input")
        time.sleep(0.5)
        print()
        add_cross()

def add_naught():
    x = input("""Player 'Naught' - Where do you want to place a naught?
Choose location and press enter: """).strip().lower()
    if (x == "a1") and (board[1][1] == "-"):
        board[1][1] = "O"
    elif (x == "a2") and (board[2][1] == "-"):
        board[2][1] = "O"
    elif (x == "a3") and (board[3][1] == "-"):
        board[3][1] = "O"

    elif (x == "b1") and (board[1][2] == "-"):
        board[1][2] = "O"
    elif (x == "b2") and (board[2][2] == "-"):
        board[2][2] = "O"
    elif (x == "b3") and (board[3][2] == "-"):
        board[3][2] = "O"

    elif (x == "c1") and (board[1][3] == "-"):
        board[1][3] = "O"
    elif (x == "c2") and (board[2][3] == "-"):
        board[2][3] = "O"
    elif (x == "c3") and (board[3][3] == "-"):
        board[3][3] = "O"
    else:
        time.sleep(0.5)
        print()
        print("Sorry, invalid input")
        time.sleep(0.5)
        print()
        add_naught()

def computer_player():
    # computer is always O
    # try to get middle if can
    if board[2][2] == "-":
        board[2][2] = "O"

    # try to win itself
    # try for horizontal win
    # line 1
    elif (board[1][1] == "O") and (board[1][2] == "O") and (board[1][3] == "-"):
        board[1][3] = "O"
    elif (board[1][1] == "O") and (board[1][2] == "-") and (board[1][3] == "O"):
        board[1][2] = "O"
    elif (board[1][1] == "-") and (board[1][2] == "O") and (board[1][3] == "O"):
        board[1][1] = "O"
    # line 2
    elif (board[2][1] == "O") and (board[2][2] == "O") and (board[2][3] == "-"):
        board[2][3] = "O"
    elif (board[2][1] == "O") and (board[2][2] == "-") and (board[2][3] == "O"):
        board[2][2] = "O"
    elif (board[2][1] == "-") and (board[2][2] == "O") and (board[2][3] == "O"):
        board[2][1] = "O"
    # line 3
    elif (board[3][1] == "O") and (board[3][2] == "O") and (board[3][3] == "-"):
        board[3][3] = "O"
    elif (board[3][1] == "O") and (board[3][2] == "-") and (board[3][3] == "O"):
        board[3][2] = "O"
    elif (board[3][1] == "-") and (board[3][2] == "O") and (board[3][3] == "O"):
        board[3][1] = "O"

    # try for vertical win
    # row 1
    elif (board[1][1] == "O") and (board[2][1] == "O") and (board[3][1] == "-"):
        board[3][1] = "O"
    elif (board[1][1] == "O") and (board[2][1] == "-") and (board[3][1] == "O"):
        board[2][1] = "O"
    elif (board[1][1] == "-") and (board[2][1] == "O") and (board[3][1] == "O"):
        board[1][1] = "O"
        # row 2
    elif (board[1][2] == "O") and (board[2][2] == "O") and (board[3][2] == "-"):
        board[3][2] = "O"
    elif (board[1][2] == "O") and (board[2][2] == "-") and (board[3][2] == "O"):
        board[2][2] = "O"
    elif (board[1][2] == "-") and (board[2][2] == "O") and (board[3][2] == "O"):
        board[1][2] = "O"
        # row 3
    elif (board[1][3] == "O") and (board[2][3] == "O") and (board[3][3] == "-"):
        board[3][3] = "O"
    elif (board[1][3] == "O") and (board[2][3] == "-") and (board[3][3] == "O"):
        board[3][2] = "O"
    elif (board[1][3] == "-") and (board[2][3] == "O") and (board[3][3] == "O"):
        board[3][1] = "O"

    # try for diagonal win
    # from top left to bottom right
    elif (board[1][1] == "O") and (board[2][2] == "O") and (board[3][3] == "-"):
        board[3][3] = "O"
    elif (board[1][1] == "O") and (board[2][2] == "-") and (board[3][3] == "O"):
        board[2][2] = "O"
    elif (board[1][1] == "-") and (board[2][2] == "O") and (board[3][3] == "O"):
        board[1][1] = "O"

        # from bottom left to top right
    elif (board[3][1] == "O") and (board[2][2] == "O") and (board[1][3] == "-"):
        board[1][3] = "O"
    elif (board[3][1] == "O") and (board[2][2] == "-") and (board[1][3] == "O"):
        board[2][2] = "O"
    elif (board[3][1] == "-") and (board[2][2] == "O") and (board[1][3] == "O"):
        board[3][1] = "O"

    # try to stop you winning
    # stop X horizontal win
    #line 1
    elif (board[1][1] == "X") and (board[1][2] == "X") and (board[1][3] == "-"):
        board[1][3] = "O"
    elif (board[1][1] == "X") and (board[1][2] == "-") and (board[1][3] == "X"):
        board[1][2] = "O"
    elif (board[1][1] == "-") and (board[1][2] == "X") and (board[1][3] == "X"):
        board[1][1] = "O"
    #line 2
    elif (board[2][1] == "X") and (board[2][2] == "X") and (board[2][3] == "-"):
        board[2][3] = "O"
    elif (board[2][1] == "X") and (board[2][2] == "-") and (board[2][3] == "X"):
        board[2][2] = "O"
    elif (board[2][1] == "-") and (board[2][2] == "X") and (board[2][3] == "X"):
        board[2][1] = "O"
    # line 3
    elif (board[3][1] == "X") and (board[3][2] == "X") and (board[3][3] == "-"):
        board[3][3] = "O"
    elif (board[3][1] == "X") and (board[3][2] == "-") and (board[3][3] == "X"):
        board[3][2] = "O"
    elif (board[3][1] == "-") and (board[3][2] == "X") and (board[3][3] == "X"):
        board[3][1] = "O"

    # stop X vertical win
    # row 1
    elif (board[1][1] == "X") and (board[2][1] == "X") and (board[3][1] == "-"):
        board[3][1] = "O"
    elif (board[1][1] == "X") and (board[2][1] == "-") and (board[3][1] == "X"):
        board[2][1] = "O"
    elif (board[1][1] == "-") and (board[2][1] == "X") and (board[3][1] == "X"):
        board[1][1] = "O"
    # row 2
    elif (board[1][2] == "X") and (board[2][2] == "X") and (board[3][2] == "-"):
        board[3][2] = "O"
    elif (board[1][2] == "X") and (board[2][2] == "-") and (board[3][2] == "X"):
        board[2][2] = "O"
    elif (board[1][2] == "-") and (board[2][2] == "X") and (board[3][2] == "X"):
        board[1][2] = "O"
    # row 3
    elif (board[1][3] == "X") and (board[2][3] == "X") and (board[3][3] == "-"):
        board[3][3] = "O"
    elif (board[1][3] == "X") and (board[2][3] == "-") and (board[3][3] == "X"):
        board[3][2] = "O"
    elif (board[1][3] == "-") and (board[2][3] == "X") and (board[3][3] == "X"):
        board[3][1] = "O"

    # stop diagonal win
    # from top left to bottom right
    elif (board[1][1] == "X") and (board[2][2] == "X") and (board[3][3] == "-"):
        board[3][3] = "O"
    elif (board[1][1] == "X") and (board[2][2] == "-") and (board[3][3] == "X"):
        board[2][2] = "O"
    elif (board[1][1] == "-") and (board[2][2] == "X") and (board[3][3] == "X"):
        board[1][1] = "O"

    # from bottom left to top right
    elif (board[3][1] == "X") and (board[2][2] == "X") and (board[1][3] == "-"):
        board[1][3] = "O"
    elif (board[3][1] == "X") and (board[2][2] == "-") and (board[1][3] == "X"):
        board[2][2] = "O"
    elif (board[3][1] == "-") and (board[2][2] == "X") and (board[1][3] == "X"):
        board[1][1] = "O"


    # go for a random option otherwise!
    else:
        global z
        global notfound
        notfound = True
        while notfound == True:
            x = random.randint(1, 3)
            y = random.randint(1, 3)
            if board[x][y] == "-":
                board[x][y] = "O"
                notfound = False

        notfound = True

    time.sleep(0.5)
    print("The computer makes a move.")
    time.sleep(0.5)


def check_win_vertical():
    global gamerunning

    # check X vertical win
    if (board[1][1] == "X") and (board[2][1] == "X") and (board[3][1] == "X"):
        print_board()
        time.sleep(0.5)
        print("     *** X wins! *** ")
        gamerunning = False
    if (board[1][2] == "X") and (board[2][2] == "X") and (board[3][2] == "X"):
        print_board()
        time.sleep(0.5)
        print("     *** X wins! *** ")
        gamerunning = False
    if (board[1][3] == "X") and (board[2][3] == "X") and (board[3][3] == "X"):
        print_board()
        time.sleep(0.5)
        print("     *** X wins! *** ")
        gamerunning = False

    # check O vertical win
    if (board[1][1] == "O") and (board[2][1] == "O") and (board[3][1] == "O"):
        print_board()
        time.sleep(0.5)
        print("     *** O wins! *** ")
        gamerunning = False
    if (board[1][2] == "O") and (board[2][2] == "O") and (board[3][2] == "O"):
        print_board()
        time.sleep(0.5)
        print("     *** O wins! *** ")
        gamerunning = False
    if (board[1][3] == "O") and (board[2][3] == "O") and (board[3][3] == "O"):
        print_board()
        time.sleep(0.5)
        print("     *** O wins! *** ")
        gamerunning = False

def check_win_horizontal():
    global gamerunning

    # check X horizontal win
    if (board[1][1] == "X") and (board[1][2] == "X") and (board[1][3] == "X"):
        print_board()
        time.sleep(0.5)
        print("     *** X wins! *** ")
        gamerunning = False
    if (board[2][1] == "X") and (board[2][2] == "X") and (board[2][3] == "X"):
        print_board()
        time.sleep(0.5)
        print("     *** X wins! *** ")
        gamerunning = False
    if (board[3][1] == "X") and (board[3][2] == "X") and (board[3][3] == "X"):
        print_board()
        time.sleep(0.5)
        print("     *** X wins! *** ")
        gamerunning = False

    # check O horizontal win
    if (board[1][1] == "O") and (board[1][2] == "O") and (board[1][3] == "O"):
        print_board()
        time.sleep(0.5)
        print("     *** O wins! *** ")
        gamerunning = False
    if (board[2][1] == "O") and (board[2][2] == "O") and (board[2][3] == "O"):
        print_board()
        time.sleep(0.5)
        print("     *** O wins! *** ")
        gamerunning = False
    if (board[3][1] == "O") and (board[3][2] == "O") and (board[3][3] == "O"):
        print_board()
        time.sleep(0.5)
        print("     *** O wins! *** ")
        gamerunning = False

def check_win_diagonal():
    global gamerunning

    # check X diagonal win
    if (board[1][1] == "X") and (board[2][2] == "X") and (board[3][3] == "X"):
        print_board()
        time.sleep(0.5)
        print("     *** X wins! *** ")
        gamerunning = False
    if (board[3][1] == "X") and (board[2][2] == "X") and (board[1][3] == "X"):
        print_board()
        time.sleep(0.5)
        print("     *** X wins! *** ")
        gamerunning = False

    # check X diagonal win
    if (board[1][1] == "O") and (board[2][2] == "O") and (board[3][3] == "O"):
        print_board()
        time.sleep(0.5)
        print("     *** O wins! *** ")
        gamerunning = False
    if (board[3][1] == "O") and (board[2][2] == "O") and (board[1][3] == "O"):
        print_board()
        time.sleep(0.5)
        print("     *** O wins! *** ")
        gamerunning = False

def check_draw():
    global gamerunning
    spaces_left = 0
    for x in board:
         for y in x:
            if y == "-":
                spaces_left += 1
    if spaces_left == 0:
        time.sleep(0.5)
        print_board()
        time.sleep(0.5)
        print("It's a draw!")
        gamerunning = False
        time.sleep(0.5)








current_player = ""

# randomly select starting player
x = random.randint(0, 1)
if x == 0:
    current_player = "X"
else:
    current_player = "O"

# change player and take turn
def change_player():
    global current_player
    if current_player == "X":
        current_player = "O"
        add_naught()
    else:
        current_player = "X"
        add_cross()

def change_player_with_computer():
    global current_player
    if current_player == "X":
        current_player = "O"
        computer_player()
    else:
        current_player = "X"
        add_cross()




# main game loop
def play_game():
    global gamerunning
    global board

    time.sleep(1)
    reply = input("""
Which mode do you want to play?
(t) two player?
(c) vs. computer?
please type in (t/c) and press enter: """).strip().lower()
    if reply == "t":

        while gamerunning:

            time.sleep(0.5)
            print_board()
            time.sleep(0.5)
            change_player()

            check_win_vertical()
            check_win_horizontal()
            check_win_diagonal()
            if gamerunning == True:
                check_draw()
            if gamerunning == False:
                print()
                x = input("Do you want to play again (y/n)? ").strip().lower()
                if x == "y":
                    gamerunning = True
                    # global board
                    board = [[" ", "a", "b", "c"],
                             ["1", "-", "-", "-"],
                             ["2", "-", "-", "-"],
                             ["3", "-", "-", "-"]]
                    play_game()
                else:
                    print("Okay, bye bye.")

    elif reply == "c":
        global computer_mode

        while gamerunning:
            time.sleep(0.5)
            print_board()
            time.sleep(0.5)
            change_player_with_computer()


            check_win_vertical()
            check_win_diagonal()
            check_win_horizontal()
            if gamerunning == True:
                check_draw()
            if gamerunning == False:
                print()
                x = input("Do you want to play again (y/n)? ").strip().lower()
                if x == "y":
                    gamerunning = True
                    # global board # is this even needed?
                    board = [[" ", "a", "b", "c"],
                             ["1", "-", "-", "-"],
                             ["2", "-", "-", "-"],
                             ["3", "-", "-", "-"]]
                    play_game()
                else:
                    print("Okay, bye bye.")

        pass
    else:
        play_game()

play_game()





