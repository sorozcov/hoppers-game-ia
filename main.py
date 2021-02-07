# Author:Silvio Orozco 18282
# Universidad del Valle
# Ingenieria en Ciencias de la Computación
# Hoppers game with AI
# Main.py

# Help and examples using pygame to build the board and game in python
# https://github.com/techwithtim/Python-Checkers/blob/master/main.py

import pygame
from game import Game
from game_options import SQUARE_SIZE,NUMBER_OF_ROWS_AND_COLS,BOARD_SIZE,PLAYER_1_COLOR,PLAYER_2_COLOR
from minimaxAgent import MinimaxAgent
from pandas  import DataFrame
import copy

display=pygame.display.set_mode((BOARD_SIZE,BOARD_SIZE))
pygame.display.set_caption('HOPPERS')

def getSquareFromMouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col
game = Game(display)
aiPlayer1 = None
aiPlayer2 = None
aiPlayer1 = MinimaxAgent(game,PLAYER_1_COLOR)
# aiPlayer2 = MinimaxAgent(game,PLAYER_2_COLOR)


def main():
    checkWin=False
    gameRunning = True
    while gameRunning:
        if(checkWin==False):
            if((aiPlayer1==None and aiPlayer2==None) or (aiPlayer1!=None and aiPlayer2==None and aiPlayer1.color!=game.turn) or (aiPlayer2!=None and aiPlayer1==None and aiPlayer2.color!=game.turn)):
                pygame.display.update()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        gameRunning = False
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        pos = pygame.mouse.get_pos()
                        
                        row, col = getSquareFromMouse(pos)
                        row = int(row)
                        col = int(col)

                        if(game.selectedPiece==0 or game.turn!=game.selectedPiece.color or (game.turn==game.selectedPiece.color and (row,col) not in game.possibleDestinations)):
                            game.selectPiece(row,col,display)
                        elif(game.turn==game.selectedPiece.color and (row,col) in game.possibleDestinations):
                            r=row+1
                            c=col+1
                            turn = 'RED' if game.turn==PLAYER_1_COLOR else 'BLUE'
                            move = game.possibleMoves[game.possibleDestinations.index((row,col))]

                            print(f"{turn}({move.path()})")
                            game.move(game.selectedPiece.row,game.selectedPiece.col,int(row),int(col),display)
                            # print(DataFrame(game.board.piecesPlayer1)) if game.turn!=PLAYER_1_COLOR else print(DataFrame(game.board.piecesPlayer2))
                            checkWin = game.checkWin()
                        pygame.display.update()
            elif (aiPlayer1!=None and aiPlayer1.color==game.turn):
                turn = 'RED' if game.turn==PLAYER_1_COLOR else 'BLUE'    
                move=aiPlayer1.alphaBetaSearch(game.copy(),float('-inf'),float('+inf'),2)
                print(f"{turn}({move.path()})")
                game.moveAction(move,True,display)
                print(DataFrame(game.board.board))
                pygame.display.update()
            elif(aiPlayer2!=None and aiPlayer2.color==game.turn):
                turn = 'RED' if game.turn==PLAYER_1_COLOR else 'BLUE'    
                move=aiPlayer2.alphaBetaSearch(game.copy(),float('-inf'),float('+inf'),2)
                print(f"{turn}({move.path()})")
                game.moveAction(move,True,display)
                print(DataFrame(game.board.board))
                pygame.display.update()
                    
               
                    
                # game.select(row, col)
     
        

main()