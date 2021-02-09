# Author:Silvio Orozco 18282
# Universidad del Valle
# Ingenieria en Ciencias de la Computación
# Hoppers game with AI
# Move.py
from game_options import SQUARE_SIZE,NUMBER_OF_ROWS_AND_COLS,PLAYER_1_COLOR
import pygame 

class Space:
    def __init__(self,row,col):
        self.row = row
        self.col = col

#Class Move   
class NodeMove:
    def __init__(self,space,parent=None):
        self.parent=parent
        self.fullPath=[]
        self.currentRow = space.row
        self.currentCol = space.col
        
    #Calculate a path on the go
    def path(self,path=None):
        path= path if path!=None else []
        if(self.parent==None):
            path.append((self.currentRow,self.currentCol))
            path.reverse()
            return path
        else:
            path.append((self.currentRow,self.currentCol))
            return self.parent.path(path)

    #Check in Tree of moves 2
    def checkInTree2(self,space):
        if(self.parent==None):
            return False
        elif(self.parent.currentRow==space.row and self.parent.currentCol==space.col):
            return True
        else:
            return self.parent.checkInTree2(space)

    #Check in tree of moves 
    def checkInTree(self,space,path=None):
        path = self.parent.path()
        for move in path:
            rowMove,colMove = move
            if(rowMove==space.row and colMove==space.col):
                return True
        return path

    #Check root space of move
    def checkRootSpace(self):
        if(self.parent==None):
            return self
        else:
            return self.parent.checkRootSpace()

    #Add child node to a possible move
    def addChildNodeMove(self,space):
        nodeMove = NodeMove(space,self)
        path = nodeMove.checkInTree(space)
        if(path==True):
            return None
        #Add fullPath to new node
        path.append((nodeMove.currentRow,nodeMove.currentCol))
        nodeMove.fullPath = path
        return nodeMove
        
    
    