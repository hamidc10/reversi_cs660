
from reversiboard import *
from player import *
from aiplayer import *
from time import time


print("""
Welcome to an interface for playing Reversi!

Select an option
  1) You vs Yourself
  2) You vs AI
  3) Random vs You
  4) Random vs AI
""")
loss=0
tied=0
winner=0
# choice = int(input("? "))
for i in range(2):
    choice=4
    if 0 < choice < 5:
        ps = [None, None, None]
        if choice < 3:
            ps[1] = HumanPlayer(1)
        else:
            ps[1] = RandomPlayer(1)
        if choice % 2 == 1:
            ps[2] = HumanPlayer(2)
        else:
            ps[2] = AIPlayer(2)
        # Start game loop
        starttime = int(time())
        board = RBoard()
        while board.terminal() == False:
            act = ps[board.player()].taketurn(board)
            print("Player "+str(board.player())+" picked "+str(act[0])+","+str(act[1]))
            print("")
            board = board.result(act)
        print("")
        # Print terminal board
        board.print()
        print("")
        
        if board.utility(1) > board.utility(2):
            loss+=1
            print("\n\nPlayer 1 wins!",loss)
        elif board.utility(1) == 0:
            tied+=1
            print("\n\nPlayer 1 and 2 tied!",tied)
        else:
            winner+=1
            print("\n\nPlayer 2 wins!" ,winner)
        # If Random vs AI, print timing info
        if choice == 4:
            if starttime + (60*5) > int(time()):
                print("Great. Your AI averaged <5sec per move.")
            else:
                print("Uh oh. Your AI averaged >5sec per move!")
        #print(int(time())-starttime)
        print(winner,loss,tied)
    else:
        print("Sorry...")
        exit(1)

