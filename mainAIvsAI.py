from game import Game
from game_options import SQUARE_SIZE,NUMBER_OF_ROWS_AND_COLS,BOARD_SIZE,PLAYER_1_COLOR,PLAYER_2_COLOR
from minimaxAgent import MinimaxAgent
from pandas  import DataFrame
import copy

display=None
aiPlayer1 = None
aiPlayer2 = None
game = Game(display)
aiPlayer1 = MinimaxAgent(game,PLAYER_1_COLOR)
aiPlayer2 = MinimaxAgent(game,PLAYER_2_COLOR)
checkWin = False
while(checkWin==False):
    if (aiPlayer1!=None and aiPlayer1.color==game.turn):
        turn = 'RED' if game.turn==PLAYER_1_COLOR else 'BLUE'    
        move=aiPlayer1.alphaBetaSearch(game.copy(),float('-inf'),float('+inf'),2)
        print(f"{turn}({move.path()})")
        game.moveAction(move,True,display)
        print(DataFrame(game.board.board))
    elif(aiPlayer2!=None and aiPlayer2.color==game.turn):
        turn = 'RED' if game.turn==PLAYER_1_COLOR else 'BLUE'    
        move=aiPlayer2.alphaBetaSearch(game.copy(),float('-inf'),float('+inf'),2)
        print(f"{turn}({move.path()})")
        game.moveAction(move,True,display)
        print(DataFrame(game.board.board))