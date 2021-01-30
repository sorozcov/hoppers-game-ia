# Author:Silvio Orozco 18282
# Universidad del Valle
# Ingenieria en Ciencias de la Computación
# Hoppers game with AI
# Main.py

# Help and examples using pygame to build the board and game in python
# https://github.com/techwithtim/Python-Checkers/blob/master/main.py

import pygame
from board import Board
BOARD_SIZE=600
NUMBER_OF_ROWS_AND_COLS = 10
SQUARE_SIZE = BOARD_SIZE / NUMBER_OF_ROWS_AND_COLS 

display=pygame.display.set_mode((BOARD_SIZE,BOARD_SIZE))
pygame.display.set_caption('HOPPERS')


def getSquareFromMouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col
board = Board(display)
def main():
    gameRunning = True
    while gameRunning:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameRunning = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = getSquareFromMouse(pos)
                # game.select(row, col)
        pygame.display.update()

main()