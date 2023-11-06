from player import Player 
import random
'''
        # TODO: update this function to use some effective combination of techniques discussed in class
        # Aim to take <5sec/move on reasonably modern hardware.
        # You should *always* beat the random player, and will score points for beating weak AIs as well.
        # To launch a game using this AI, run $ python3 play.py
'''
class AIPlayer(Player):
    def __init__(self, p):
        self.playerN = p
        self.tile_cost={(0,0):1000000,(0,7):1000000,(7,0):1000000,(7,7):1000000,(1,1):-500000,(6,1):-500000,(1,6):-500000,(6,6):-500000,(0,1):-300000,(1,0):-300000,(0,6):-300000,(7,1):-300000,(6,0):-300000,(1,7):-300000,(6,7):-300000,(7,6):-300000}
    
    def rand_board_gen(self,board):
        # It does this untill the game has an outcome of a winner ,loser or draw for this boards 
        while not board.terminal():
            # Take a board and randomly selectly an action then once an action has been choosen then progess the game and then repeats the process with the newly played board 
            board=board.result(random.sample(sorted(board.actions()),1)[0])
        return board.utility(self.playerN)
    # This returns the staus of the board

    # Make a map of useful option the the bot can then decide to chose over the monte carlo choice then go back

    def taketurn(self, board):
        # board.print()
        # Itilize the best_move which the a.i bot has chosen
        best_move=None
        # Sets up the value of best_result with -inf to be chnaged later with an apporaite value
        best_result=float("-inf")
        # Here we loop through the possible actions that can be taken by the A.i.
        for action in board.actions():
            # This returns the result of the action played by the A.i.
            played_board=board.result(action)
            # This here is monte carlo  
            generated=[self.rand_board_gen(played_board) for _ in range(25)]
            # So we set up the range to be 25, This then allows 25 itteration of the game to be played with randomly selected moves by both parties untill it yeilds a utility score f winner loser or draw.

            check=sum(generated)/(25*1000000)
            # Here we get the outcomes of the games and genrante an average of vicotirs  for that action that was taken
            check += self.tile_cost.get(action ,0)
            # Here we check the title score database and get the value of the tile if it is inside and add it to the check average
            # print(check)

            # Here is an if statement to compare the value of the check to the best_result value
            if check>best_result:
                best_result=check
                best_move=action
        return best_move
    
    def player(self):
        return self.playerN
    
