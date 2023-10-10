

from player import Player 
import random

class AIPlayer(Player):
    def __init__(self, p):
        self.playerN = p
    def taketurn(self, board):
        board.print()
        # TODO: update this function to use some effective combination of techniques discussed in class
        # Aim to take <5sec/move on reasonably modern hardware.
        # You should *always* beat the random player, and will score points for beating weak AIs as well.
        # To launch a game using this AI, run $ python3 play.py
        return random.sample(board.actions(),1)[0]
    def player(self):
        return self.playerN
    
