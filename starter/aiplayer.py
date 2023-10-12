

from player import Player 
import random

class AIPlayer(Player):
    def __init__(self, p):
        self.playerN = p
    
    def rand_board_gen(self,board):
        while not board.terminal():
            board=board.result(random.sample(sorted(board.actions()),1)[0])
        return board.utility(self.playerN)
    # Make a map of useful option the the bot can then decide to chose over the monte carlo choice then go back

    def taketurn(self, board):
        board.print()
        # TODO: update this function to use some effective combination of techniques discussed in class
        # Aim to take <5sec/move on reasonably modern hardware.
        # You should *always* beat the random player, and will score points for beating weak AIs as well.
        # To launch a game using this AI, run $ python3 play.py
        data={(0,0):10000000,(0,7):10000000,(7,0):10000000,(7,7):10000000}
        best_move=None
        best_result=float("-inf")
        for action in board.actions():
            played_board=board.result(action)
            generated=[self.rand_board_gen(played_board) for _ in range(50)]
            check=sum(generated)/(50*1000000)
            check += data.get(action ,0)
            print(check)
            if check>best_result:
                best_result=check
                best_move=action
        return best_move
    

        # return random.sample(sorted(board.actions()),1)[0]
    def player(self):
        return self.playerN
    
