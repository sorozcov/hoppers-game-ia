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
        self.display = display
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

    def checkRightSpaceJump(self,board,parent=None):
        possibleJumpMoves = []
        move = NodeMove(self,parent)
        newSpaceBeside = board.getPieceRightSpace(self.row,self.col)
        newSpaceJump=None
        if(newSpaceBeside!=None and newSpaceBeside!=0):
            newSpaceJump = board.getPieceRightSpace(newSpaceBeside.row,newSpaceBeside.col)
        if(newSpaceJump!=None and newSpaceJump==0 and newSpaceBeside!=0 and newSpaceBeside!=0):
            leafNode = move.addChildNodeMove(newSpaceJump)
            newLeafJumps = []
            if(leafNode!=None):
                possibleJumpMoves.append(leafNode)
                newLeafJumps=newSpaceJump.checkNewJumpMoves(board,leafNode)
            return newLeafJumps + possibleJumpMoves
        else:
            return possibleJumpMoves
        return []

    def checkLeftSpaceJump(self,board,parent=None):
        possibleJumpMoves = []
        move = NodeMove(self,parent)
        newSpaceBeside = board.getPieceLeftSpace(self.row,self.col)
        newSpaceJump=None
        if(newSpaceBeside!=None and newSpaceBeside!=0):
            newSpaceJump = board.getPieceLeftSpace(newSpaceBeside.row,newSpaceBeside.col)
        if(newSpaceJump!=None and newSpaceJump==0 and newSpaceBeside!=0 and newSpaceBeside!=0):
            leafNode = move.addChildNodeMove(newSpaceJump)
            newLeafJumps = []
            if(leafNode!=None):
                possibleJumpMoves.append(leafNode)
                newLeafJumps=newSpaceJump.checkNewJumpMoves(board,leafNode)
            return newLeafJumps + possibleJumpMoves
        else:
            return possibleJumpMoves
        return []

    def checkTopSpaceJump(self,board,parent=None):
        possibleJumpMoves = []
        move = NodeMove(self,parent)
        newSpaceBeside = board.getPieceTopSpace(self.row,self.col)
        newSpaceJump=None
        if(newSpaceBeside!=None and newSpaceBeside!=0):
            newSpaceJump = board.getPieceTopSpace(newSpaceBeside.row,newSpaceBeside.col)
        if(newSpaceJump!=None and newSpaceJump==0 and newSpaceBeside!=0 and newSpaceBeside!=0):
            leafNode = move.addChildNodeMove(newSpaceJump)
            newLeafJumps = []
            if(leafNode!=None):
                possibleJumpMoves.append(leafNode)
                newLeafJumps=newSpaceJump.checkNewJumpMoves(board,leafNode)
            return newLeafJumps + possibleJumpMoves
        else:
            return possibleJumpMoves
        return []

    def checkBottomSpaceJump(self,board,parent=None):
        possibleJumpMoves = []
        move = NodeMove(self,parent)
        newSpaceBeside = board.getPieceBottomSpace(self.row,self.col)
        newSpaceJump=None
        if(newSpaceBeside!=None and newSpaceBeside!=0):
            newSpaceJump = board.getPieceBottomSpace(newSpaceBeside.row,newSpaceBeside.col)
        if(newSpaceJump!=None and newSpaceJump==0 and newSpaceBeside!=0 and newSpaceBeside!=0):
            leafNode = move.addChildNodeMove(newSpaceJump)
            newLeafJumps = []
            if(leafNode!=None):
                possibleJumpMoves.append(leafNode)
                newLeafJumps=newSpaceJump.checkNewJumpMoves(board,leafNode)
            return newLeafJumps + possibleJumpMoves
        else:
            return possibleJumpMoves
        return []

    def checkTopRightSpaceJump(self,board,parent=None):
        possibleJumpMoves = []
        move = NodeMove(self,parent)
        newSpaceBeside = board.getPieceTopRightSpace(self.row,self.col)
        newSpaceJump=None
        if(newSpaceBeside!=None and newSpaceBeside!=0):
            newSpaceJump = board.getPieceTopRightSpace(newSpaceBeside.row,newSpaceBeside.col)
        if(newSpaceJump!=None and newSpaceJump==0 and newSpaceBeside!=0 and newSpaceBeside!=0):
            leafNode = move.addChildNodeMove(newSpaceJump)
            newLeafJumps = []
            if(leafNode!=None):
                possibleJumpMoves.append(leafNode)
                newLeafJumps=newSpaceJump.checkNewJumpMoves(board,leafNode)
            return newLeafJumps + possibleJumpMoves
        else:
            return possibleJumpMoves
        return []

    def checkTopLeftSpaceJump(self,board,parent=None):
        possibleJumpMoves = []
        move = NodeMove(self,parent)
        newSpaceBeside = board.getPieceTopLeftSpace(self.row,self.col)
        newSpaceJump=None
        if(newSpaceBeside!=None and newSpaceBeside!=0):
            newSpaceJump = board.getPieceTopLeftSpace(newSpaceBeside.row,newSpaceBeside.col)
        if(newSpaceJump!=None and newSpaceJump==0 and newSpaceBeside!=0 and newSpaceBeside!=0):
            leafNode = move.addChildNodeMove(newSpaceJump)
            newLeafJumps = []
            if(leafNode!=None):
                possibleJumpMoves.append(leafNode)
                newLeafJumps=newSpaceJump.checkNewJumpMoves(board,leafNode)
            return newLeafJumps + possibleJumpMoves
        else:
            return possibleJumpMoves
        return []
    
    def checkBottomRightSpaceJump(self,board,parent=None):
        possibleJumpMoves = []
        move = NodeMove(self,parent)
        newSpaceBeside = board.getPieceBottomRightSpace(self.row,self.col)
        newSpaceJump=None
        if(newSpaceBeside!=None and newSpaceBeside!=0):
            newSpaceJump = board.getPieceBottomRightSpace(newSpaceBeside.row,newSpaceBeside.col)
        if(newSpaceJump!=None and newSpaceJump==0 and newSpaceBeside!=0 and newSpaceBeside!=0):
            leafNode = move.addChildNodeMove(newSpaceJump)
            newLeafJumps = []
            if(leafNode!=None):
                possibleJumpMoves.append(leafNode)
                newLeafJumps=newSpaceJump.checkNewJumpMoves(board,leafNode)
            return newLeafJumps + possibleJumpMoves
        else:
            return possibleJumpMoves
        return []

    def checkBottomLeftSpaceJump(self,board,parent=None):
        possibleJumpMoves = []
        move = NodeMove(self,parent)
        newSpaceBeside = board.getPieceBottomLeftSpace(self.row,self.col)
        newSpaceJump=None
        if(newSpaceBeside!=None and newSpaceBeside!=0):
            newSpaceJump = board.getPieceBottomLeftSpace(newSpaceBeside.row,newSpaceBeside.col)
        if(newSpaceJump!=None and newSpaceJump==0 and newSpaceBeside!=0 and newSpaceBeside!=0):
            leafNode = move.addChildNodeMove(newSpaceJump)
            newLeafJumps = []
            if(leafNode!=None):
                possibleJumpMoves.append(leafNode)
                newLeafJumps=newSpaceJump.checkNewJumpMoves(board,leafNode)
            return newLeafJumps + possibleJumpMoves
        else:
            return possibleJumpMoves
        return []

    def checkNewJumpMoves(self,board,parent=None):        
        return (self.checkRightSpaceJump(board,parent)+
                self.checkLeftSpaceJump(board,parent)+
                self.checkTopSpaceJump(board,parent)+
                self.checkBottomSpaceJump(board,parent)+
                self.checkTopRightSpaceJump(board,parent)+
                self.checkTopLeftSpaceJump(board,parent)+
                self.checkBottomRightSpaceJump(board,parent)+
                self.checkBottomLeftSpaceJump(board,parent))
    
    def checkNewOneSpaceMoves(self,board):    
        move = NodeMove(self)    
        return (self.checkRightSpace(board,move)+
                self.checkLeftSpace(board,move)+
                self.checkTopSpace(board,move)+
                self.checkBottomSpace(board,move)+
                self.checkTopRightSpace(board,move)+
                self.checkTopLeftSpace(board,move)+
                self.checkBottomRightSpace(board,move)+
                self.checkBottomLeftSpace(board,move))
    
    def checkPossibleMoves(self,board):
        self.drawSelected()
        return (self.checkNewJumpMoves(board)+self.checkNewOneSpaceMoves(board))

    def drawSelected(self):
        pygame.draw.circle(self.display, BLACK, (int(self.col*SQUARE_SIZE+SQUARE_SIZE/2), int(self.row *SQUARE_SIZE+SQUARE_SIZE/2) ), int(SQUARE_SIZE/3))

    def __repr__(self):
        return   ('P1' if self.color==PLAYER_1_COLOR else 'P2') if not self.blanckSpace else '0'

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