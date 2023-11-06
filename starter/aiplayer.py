from player import Player 
import random

class AIPlayer(Player):
    def __init__(self, p):
        self.playerN = p
        self.tile_cost={(0,0):1000000,(0,7):1000000,(7,0):1000000,(7,7):1000000,(1,1):-500000,(6,1):-500000,(1,6):-500000,(6,6):-500000,(0,1):-300000,(1,0):-300000,(0,6):-300000,(7,1):-300000,(6,0):-300000,(1,7):-300000,(6,7):-300000,(7,6):-300000}
    
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
        tile_score=self.tile_cost
        best_move=None
        best_result=float("-inf")
        for action in board.actions():
            played_board=board.result(action)
            generated=[self.rand_board_gen(played_board) for _ in range(25)]
            check=sum(generated)/(25*1000000)
            check += tile_score.get(action ,0)
            # print(check)
            if check>best_result:
                best_result=check
                best_move=action
        return best_move
    

        # return random.sample(sorted(board.actions()),1)[0]
    def player(self):
        return self.playerN
    
