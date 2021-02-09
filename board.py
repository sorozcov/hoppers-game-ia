# Author:Silvio Orozco 18282
# Universidad del Valle
# Ingenieria en Ciencias de la Computación
# Hoppers game with AI
# board.py class
import pygame
from game_options import SQUARE_SIZE,NUMBER_OF_ROWS_AND_COLS,BOARD_BACKGROUND_COLOR,BOARD_BORDER_COLOR,PLAYER_1_COLOR,PLAYER_2_COLOR,PLAYER_1_HOUSE_COLOR,PLAYER_2_HOUSE_COLOR,POSSIBLE_MOVE_COLOR
from piece import Piece,BlankSpace

# Class board
class Board:
    def __init__(self,display=None):
        
        self.backgroundColor = BOARD_BACKGROUND_COLOR
        self.borderColor = BOARD_BORDER_COLOR
        self.player1Color = PLAYER_1_COLOR
        self.player2Color = PLAYER_2_COLOR
        self.player1HouseColor = PLAYER_1_HOUSE_COLOR
        self.player2HouseColor = PLAYER_2_HOUSE_COLOR
        self.board = []
        self.selectedPiecce = None
        self.initBoard()
        self.drawBoard(display)
        
    
    # Init Board
    def initBoard(self):
        self.board = []
        self.clearBoard()
        self.createPieces()
        
    # Clear board to a new board
    def clearBoard(self):
        # We generate whole board with 0s
        self.board = []
        self.piecesPlayer1 = []
        self.piecesPlayer2 = []
        for row in range(NUMBER_OF_ROWS_AND_COLS):
            self.board.append([])
            for col in range(NUMBER_OF_ROWS_AND_COLS):
                self.board[row].append(Piece(row=row,col=col,blanckSpace=True))

    # Create pieces in board
    def createPieces(self):
        colPlayer1 = 5
        pieceNumber = 0
        for row in range(5):
            for col in range(colPlayer1):
                piece=Piece(row,col,self.player1Color,pieceNumber)
                self.board[row][col] = piece
                self.piecesPlayer1.append(piece)
                pieceNumber = pieceNumber + 1
            colPlayer1= colPlayer1 -1;
        colWhite = 9
        pieceNumber = 0
        for row in range(5,10):
            for col in range(colWhite,10):
                piece=Piece(row,col,self.player2Color,pieceNumber)
                self.board[row][col] = piece
                self.piecesPlayer2.append(piece)
                pieceNumber = pieceNumber + 1
            colWhite= colWhite -1;

    #Draw board on display of pygame
    def drawBoard(self,display=None):
        if display!=None:
            display.fill(self.backgroundColor)
            colPlayer1 = 5
            for row in range(5):
                for col in range(colPlayer1):
                    pygame.draw.rect( display,self.player1HouseColor, (col*SQUARE_SIZE, row *SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
                colPlayer1= colPlayer1 -1;
            colWhite = 9
            for row in range(5,10):
                for col in range(colWhite,10):
                    pygame.draw.rect( display,self.player2HouseColor, (col*SQUARE_SIZE, row *SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
                colWhite= colWhite -1;
            for row in range(NUMBER_OF_ROWS_AND_COLS):
                for col in range(NUMBER_OF_ROWS_AND_COLS):
                    if self.board[row][col]!=0:
                        piece = self.board[row][col]
                        piece.draw(display)
                        
                    pygame.draw.rect( display,self.borderColor, (col*SQUARE_SIZE, row *SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE),1)


    #Move on board
    def move(self,fromRow,fromCol,row,col,display=None):
        piece =self.board[fromRow][fromCol]
        if(piece!=0):
            piece.move(row,col)
            self.board[fromRow][fromCol] = Piece(row=fromRow,col=fromCol,blanckSpace=True)
            
            if(piece.color ==PLAYER_1_COLOR):
                self.piecesPlayer1[piece.pieceNumber] = piece
            else:
                self.piecesPlayer2[piece.pieceNumber] = piece
            self.board[row][col]= piece
            
            if(display!=None):
                self.drawBoard(display)
         
    #Get piece in position of board
    def getPiece(self,row,col):
        if(row>NUMBER_OF_ROWS_AND_COLS-1 or row<0):
            return None
        elif(col<0 or col>NUMBER_OF_ROWS_AND_COLS-1):
            return None
        return self.board[row][col]
    
    # Get spaces near a piece functions

    def getPieceTopSpace(self,row,col):
        return self.getPiece(row-1,col)

    def getPieceBottomSpace(self,row,col):
        return self.getPiece(row+1,col)

    def getPieceRightSpace(self,row,col):
        return self.getPiece(row,col+1)
    
    def getPieceLeftSpace(self,row,col):
        return self.getPiece(row,col-1)

    def getPieceTopRightSpace(self,row,col):
        return self.getPiece(row-1,col+1)

    def getPieceTopLeftSpace(self,row,col):
        return self.getPiece(row-1,col-1)

    def getPieceBottomRightSpace(self,row,col):
        return self.getPiece(row+1,col+1)
    
    def getPieceBottomLeftSpace(self,row,col):
        return self.getPiece(row+1,col-1)

    #Draw possible moves on pygame for selected piece
    def drawPossibleMoves(self,piece,display):
        posibleDestinations = []
        possibleMoves = piece.checkPossibleMoves(self)
        for move in possibleMoves:
            if(move!=None):
                if(self.getPiece(move.currentRow,move.currentCol)==0):
                    posibleDestinations.append((move.currentRow,move.currentCol))
                    if(display!=None):
                        pygame.draw.circle(display,POSSIBLE_MOVE_COLOR , (int(move.currentCol*SQUARE_SIZE+SQUARE_SIZE/2), int(move.currentRow *SQUARE_SIZE+SQUARE_SIZE/2) ), int(SQUARE_SIZE/3))
        return posibleDestinations,possibleMoves

    #Return possible moves for a piece
    def possibleMoves(self,piece):
        posibleDestinations = []
        possibleMoves = piece.checkPossibleMoves(self)
        for move in possibleMoves:
            if(move!=None):
                if(self.getPiece(move.currentRow,move.currentCol)==0):
                    posibleDestinations.append((move.currentRow,move.currentCol))
        return possibleMoves
    
