from game import Game
from game_options import SQUARE_SIZE,NUMBER_OF_ROWS_AND_COLS,BOARD_SIZE,PLAYER_1_COLOR,PLAYER_2_COLOR
from minimaxAgent import MinimaxAgent
from pandas  import DataFrame
import copy
import time

display=None
aiPlayer1 = None
aiPlayer2 = None
game = Game(display)
aiPlayer1 = MinimaxAgent(game,PLAYER_1_COLOR)
aiPlayer2 = MinimaxAgent(game,PLAYER_2_COLOR)
checkWin = False
timerPlayer1=0
timerPlayer2=0
playsPlayer1=0
playsPlayer2=0

#Main AI vs AI
while(checkWin==False):
    if (aiPlayer1!=None and aiPlayer1.color==game.turn):
        playsPlayer1 = playsPlayer1 +1
        turn = 'RED' if game.turn==PLAYER_1_COLOR else 'BLUE'    
        t1 = time.time()
        move=aiPlayer1.alphaBetaSearch(game.copy(),float('-inf'),float('+inf'),2)
        t2 = time.time()
        
        tim = (t2-t1)
        timerPlayer1 = timerPlayer1 + tim
        print("timer red" + str(tim))
        if(move!=None):
            print(f"{turn}({move.path()})")
            game.moveAction(move,True,display)
            print(DataFrame(game.board.board))
        checkWin=game.checkWin()
    elif(aiPlayer2!=None and aiPlayer2.color==game.turn):
        playsPlayer2 = playsPlayer2 +1
        turn = 'RED' if game.turn==PLAYER_1_COLOR else 'BLUE'    
        t1 = time.time()
        move=aiPlayer2.alphaBetaSearch(game.copy(),float('-inf'),float('+inf'),2)
        t2 = time.time()
        tim = (t2-t1)
        
        timerPlayer2 = timerPlayer2 + tim
        print("timer blue" + str(tim))
        if(move!=None):
            print(f"{turn}({move.path()})")
            game.moveAction(move,True,display)
            print(DataFrame(game.board.board))
        checkWin=game.checkWin()
print("Player won " + ("RED" if checkWin==PLAYER_1_COLOR else "BLUE"))
print("Final Timer Red " + str(timerPlayer1))
print("Final Plays Red " + str(playsPlayer1))
print("Final Average Play Red " + str(timerPlayer1/playsPlayer1))
print("Final Timer Blue " + str(timerPlayer2))
print("Final Plays Blue " + str(playsPlayer2))
print("Final Average Blue " + str(timerPlayer2/playsPlayer2))