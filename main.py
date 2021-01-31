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

display=pygame.display.set_mode((BOARD_SIZE,BOARD_SIZE))
pygame.display.set_caption('HOPPERS')


def getSquareFromMouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col
game = Game(display)
def main():
    gameRunning = True
    while gameRunning:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameRunning = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                print(pos)
                row, col = getSquareFromMouse(pos)
                row = int(row)
                col = int(col)
                print(row)
                print(col)
                if(game.selectedPiece==0 or game.turn!=game.selectedPiece.color or (game.turn==game.selectedPiece.color and (row,col) not in game.possibleDestinations)):
                    game.selectPiece(row,col)
                elif(game.turn==game.selectedPiece.color and (row,col) in game.possibleDestinations):
                    game.move(game.selectedPiece.row,game.selectedPiece.col,int(row),int(col))
                
                
               
                    
                # game.select(row, col)
        pygame.display.update()

main()