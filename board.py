# Author:Silvio Orozco 18282
# Universidad del Valle
# Ingenieria en Ciencias de la Computación
# Hoppers game with AI
# board.py class
import pygame
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (248, 254, 159)
LIGHT_RED = (255, 117, 117 )
LIGHT_WHITE = (240, 240, 240)
BLUE = (0, 0, 255)
GREY = (128,128,128)
BOARD_SIZE=600
NUMBER_OF_ROWS_AND_COLS = 10
SQUARE_SIZE = BOARD_SIZE / NUMBER_OF_ROWS_AND_COLS 

class Board:
    def __init__(self,display):
        self.display = display
        self.board = []
        self.red_left = self.white_left = 12
        self.red_kings = self.white_kings = 0
        self.draw_squares()
    
    def draw_squares(self):
        self.display.fill(YELLOW)
        rowRed = 5
        for col in range(5):
            for row in range(rowRed):
                pygame.draw.rect( self.display,LIGHT_RED, (row*SQUARE_SIZE, col *SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
            rowRed= rowRed -1;
        rowWhite = 9
        for col in range(5,10):
            for row in range(rowWhite,10):
                pygame.draw.rect( self.display,LIGHT_WHITE, (row*SQUARE_SIZE, col *SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
            rowWhite= rowWhite -1;
        for row in range(NUMBER_OF_ROWS_AND_COLS):
            for col in range(NUMBER_OF_ROWS_AND_COLS):
                
                pygame.draw.rect( self.display,BLACK, (row*SQUARE_SIZE, col *SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE),1)