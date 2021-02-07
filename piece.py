# Author:Silvio Orozco 18282
# Universidad del Valle
# Ingenieria en Ciencias de la Computación
# Hoppers game with AI
# Piece.py
from game_options import SQUARE_SIZE,NUMBER_OF_ROWS_AND_COLS,PLAYER_1_COLOR,BLACK
from move import NodeMove
import pygame 

class Piece:
    def __init__(self,row,col,color=None,pieceNumber=None,blanckSpace=False):
        self.row = row
        self.col = col
        self.color = color
        self.pieceNumber = pieceNumber
        self.inside = False
        self.blanckSpace = blanckSpace
    
    def move(self,row,col):
        self.row = row
        self.col = col


    def draw(self,display):
        pygame.draw.circle(display, self.color, (int(self.col*SQUARE_SIZE+SQUARE_SIZE/2), int(self.row *SQUARE_SIZE+SQUARE_SIZE/2) ), int(SQUARE_SIZE/3))
    
    def checkRightSpace(self,board,move):
        
        newSpace = board.getPieceRightSpace(self.row,self.col)
        if(newSpace!=None and newSpace==0):
            leafNode = move.addChildNodeMove(newSpace)
            return [leafNode]
        return []

    def checkLeftSpace(self,board,move):
        
        newSpace = board.getPieceLeftSpace(self.row,self.col)
        if(newSpace!=None and newSpace==0):
            leafNode = move.addChildNodeMove(newSpace)
            return [leafNode]
        return []
    
    def checkTopSpace(self,board,move):
        
        newSpace = board.getPieceTopSpace(self.row,self.col)
        if(newSpace!=None and newSpace==0):
            leafNode = move.addChildNodeMove(newSpace)
            return [leafNode]
        return []

    def checkBottomSpace(self,board,move):
        
        newSpace = board.getPieceBottomSpace(self.row,self.col)
        if(newSpace!=None and newSpace==0):
            leafNode = move.addChildNodeMove(newSpace)
            return [leafNode]
        return []
    
    def checkTopRightSpace(self,board,move):
        
        newSpace = board.getPieceTopRightSpace(self.row,self.col)
        if(newSpace!=None and newSpace==0):
            leafNode = move.addChildNodeMove(newSpace)
            return [leafNode]
        return []

    def checkTopLeftSpace(self,board,move):
        
        newSpace = board.getPieceTopLeftSpace(self.row,self.col)
        if(newSpace!=None and newSpace==0):
            leafNode = move.addChildNodeMove(newSpace)
            return [leafNode]
        return []

    def checkBottomRightSpace(self,board,move):
        
        newSpace = board.getPieceBottomRightSpace(self.row,self.col)
        if(newSpace!=None and newSpace==0):
            leafNode = move.addChildNodeMove(newSpace)
            return [leafNode]
        return []

    def checkBottomLeftSpace(self,board,move):
        
        newSpace = board.getPieceBottomLeftSpace(self.row,self.col)
        if(newSpace!=None and newSpace==0):
            leafNode = move.addChildNodeMove(newSpace)
            return [leafNode]
        return []

    def checkRightSpaceJump(self,board,move=None):
        possibleJumpMoves = []
        
        newSpaceBeside = board.getPieceRightSpace(self.row,self.col)
        newSpaceJump=None
        if(newSpaceBeside!=None and newSpaceBeside!=0):
            newSpaceJump = board.getPieceRightSpace(newSpaceBeside.row,newSpaceBeside.col)
        if(newSpaceJump!=None and newSpaceJump==0 and newSpaceBeside!=0):
            leafNode = move.addChildNodeMove(newSpaceJump)
            newLeafJumps = []
            if(leafNode!=None):
                possibleJumpMoves.append(leafNode)
                newLeafJumps=newSpaceJump.checkNewJumpMoves(board,leafNode)
            return newLeafJumps + possibleJumpMoves
        else:
            return possibleJumpMoves
        return []

    def checkLeftSpaceJump(self,board,move=None):
        possibleJumpMoves = []
        
        newSpaceBeside = board.getPieceLeftSpace(self.row,self.col)
        newSpaceJump=None
        if(newSpaceBeside!=None and newSpaceBeside!=0):
            newSpaceJump = board.getPieceLeftSpace(newSpaceBeside.row,newSpaceBeside.col)
        if(newSpaceJump!=None and newSpaceJump==0 and newSpaceBeside!=0):
            leafNode = move.addChildNodeMove(newSpaceJump)
            newLeafJumps = []
            if(leafNode!=None):
                possibleJumpMoves.append(leafNode)
                newLeafJumps=newSpaceJump.checkNewJumpMoves(board,leafNode)
            return newLeafJumps + possibleJumpMoves
        else:
            return possibleJumpMoves
        return []

    def checkTopSpaceJump(self,board,move=None):
        possibleJumpMoves = []
        
        newSpaceBeside = board.getPieceTopSpace(self.row,self.col)
        newSpaceJump=None
        if(newSpaceBeside!=None and newSpaceBeside!=0):
            newSpaceJump = board.getPieceTopSpace(newSpaceBeside.row,newSpaceBeside.col)
        if(newSpaceJump!=None and newSpaceJump==0 and newSpaceBeside!=0):
            leafNode = move.addChildNodeMove(newSpaceJump)
            newLeafJumps = []
            if(leafNode!=None):
                possibleJumpMoves.append(leafNode)
                newLeafJumps=newSpaceJump.checkNewJumpMoves(board,leafNode)
            return newLeafJumps + possibleJumpMoves
        else:
            return possibleJumpMoves
        return []

    def checkBottomSpaceJump(self,board,move=None):
        possibleJumpMoves = []
        
        newSpaceBeside = board.getPieceBottomSpace(self.row,self.col)
        newSpaceJump=None
        if(newSpaceBeside!=None and newSpaceBeside!=0):
            newSpaceJump = board.getPieceBottomSpace(newSpaceBeside.row,newSpaceBeside.col)
        if(newSpaceJump!=None and newSpaceJump==0 and newSpaceBeside!=0):
            leafNode = move.addChildNodeMove(newSpaceJump)
            newLeafJumps = []
            if(leafNode!=None):
                possibleJumpMoves.append(leafNode)
                newLeafJumps=newSpaceJump.checkNewJumpMoves(board,leafNode)
            return newLeafJumps + possibleJumpMoves
        else:
            return possibleJumpMoves
        return []

    def checkTopRightSpaceJump(self,board,move=None):
        possibleJumpMoves = []
        
        newSpaceBeside = board.getPieceTopRightSpace(self.row,self.col)
        newSpaceJump=None
        if(newSpaceBeside!=None and newSpaceBeside!=0):
            newSpaceJump = board.getPieceTopRightSpace(newSpaceBeside.row,newSpaceBeside.col)
        if(newSpaceJump!=None and newSpaceJump==0 and newSpaceBeside!=0):
            leafNode = move.addChildNodeMove(newSpaceJump)
            newLeafJumps = []
            if(leafNode!=None):
                possibleJumpMoves.append(leafNode)
                newLeafJumps=newSpaceJump.checkNewJumpMoves(board,leafNode)
            return newLeafJumps + possibleJumpMoves
        else:
            return possibleJumpMoves
        return []

    def checkTopLeftSpaceJump(self,board,move=None):
        possibleJumpMoves = []
        
        newSpaceBeside = board.getPieceTopLeftSpace(self.row,self.col)
        newSpaceJump=None
        if(newSpaceBeside!=None and newSpaceBeside!=0):
            newSpaceJump = board.getPieceTopLeftSpace(newSpaceBeside.row,newSpaceBeside.col)
        if(newSpaceJump!=None and newSpaceJump==0 and newSpaceBeside!=0):
            leafNode = move.addChildNodeMove(newSpaceJump)
            newLeafJumps = []
            if(leafNode!=None):
                possibleJumpMoves.append(leafNode)
                newLeafJumps=newSpaceJump.checkNewJumpMoves(board,leafNode)
            return newLeafJumps + possibleJumpMoves
        else:
            return possibleJumpMoves
        return []
    
    def checkBottomRightSpaceJump(self,board,move=None):
        possibleJumpMoves = []
        
        newSpaceBeside = board.getPieceBottomRightSpace(self.row,self.col)
        newSpaceJump=None
        if(newSpaceBeside!=None and newSpaceBeside!=0):
            newSpaceJump = board.getPieceBottomRightSpace(newSpaceBeside.row,newSpaceBeside.col)
        if(newSpaceJump!=None and newSpaceJump==0 and newSpaceBeside!=0):
            leafNode = move.addChildNodeMove(newSpaceJump)
            newLeafJumps = []
            if(leafNode!=None):
                possibleJumpMoves.append(leafNode)
                newLeafJumps=newSpaceJump.checkNewJumpMoves(board,leafNode)
            return newLeafJumps + possibleJumpMoves
        else:
            return possibleJumpMoves
        return []

    def checkBottomLeftSpaceJump(self,board,move=None):
        possibleJumpMoves = []
        
        newSpaceBeside = board.getPieceBottomLeftSpace(self.row,self.col)
        newSpaceJump=None
        if(newSpaceBeside!=None and newSpaceBeside!=0):
            newSpaceJump = board.getPieceBottomLeftSpace(newSpaceBeside.row,newSpaceBeside.col)
        if(newSpaceJump!=None and newSpaceJump==0 and newSpaceBeside!=0):
            leafNode = move.addChildNodeMove(newSpaceJump)
            newLeafJumps = []
            if(leafNode!=None):
                possibleJumpMoves.append(leafNode)
                newLeafJumps=newSpaceJump.checkNewJumpMoves(board,leafNode)
            return newLeafJumps + possibleJumpMoves
        else:
            return possibleJumpMoves
        return []

    def checkNewJumpMoves(self,board,move=None):        
        return (self.checkRightSpaceJump(board,move)+
                self.checkLeftSpaceJump(board,move)+
                self.checkTopSpaceJump(board,move)+
                self.checkBottomSpaceJump(board,move)+
                self.checkTopRightSpaceJump(board,move)+
                self.checkTopLeftSpaceJump(board,move)+
                self.checkBottomRightSpaceJump(board,move)+
                self.checkBottomLeftSpaceJump(board,move))
    
    def checkNewOneSpaceMoves(self,board,move=None):    
        # move = NodeMove(self)    
        return (self.checkRightSpace(board,move)+
                self.checkLeftSpace(board,move)+
                self.checkTopSpace(board,move)+
                self.checkBottomSpace(board,move)+
                self.checkTopRightSpace(board,move)+
                self.checkTopLeftSpace(board,move)+
                self.checkBottomRightSpace(board,move)+
                self.checkBottomLeftSpace(board,move))
    
    def checkPossibleMoves(self,board):
        
        return (self.checkNewJumpMoves(board,NodeMove(self))+self.checkNewOneSpaceMoves(board,NodeMove(self)))

    def possibleMoves(self,board):
        return (self.checkNewJumpMoves(board,NodeMove(self))+self.checkNewOneSpaceMoves(board,NodeMove(self)))
    
    def drawSelected(self,display=None):
        if(display!=None):
            pygame.draw.circle(display, BLACK, (int(self.col*SQUARE_SIZE+SQUARE_SIZE/2), int(self.row *SQUARE_SIZE+SQUARE_SIZE/2) ), int(SQUARE_SIZE/3))

    def __repr__(self):
        return   ('P1' +(f'({self.row} {self.col})') if self.color==PLAYER_1_COLOR else 'P2' +(f'({self.row} {self.col})')) if not self.blanckSpace else '0'

    def __eq__(self,other):
        if(self.blanckSpace):
            return other==0

class BlankSpace:
    def __init__(self,row,col):
        self.row = row
        self.col = col

    def __repr__(self):
        return  '0'

    def __eq__(self,other):
        return other==0