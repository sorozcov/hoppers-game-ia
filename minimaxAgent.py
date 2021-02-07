# Author:Silvio Orozco 18282
# Universidad del Valle
# Ingenieria en Ciencias de la Computación
# Hoppers game with AI
# Hoppers minimaxAgent.py
from game_options import PLAYER_1_COLOR,PLAYER_2_COLOR
import numpy as np
class MinimaxAgent():
    #Receives a game as starter
    def __init__(self,game,playerMaxColor=PLAYER_1_COLOR):
        self.game = game
        self.color= playerMaxColor
        self.playerMaxColor = playerMaxColor
        self.playerMinColor = PLAYER_2_COLOR if self.playerMaxColor==PLAYER_1_COLOR else PLAYER_1_COLOR
        self.depth =3
        self.turnCount = 0
        self.piecesTargetOrderPlayer1 = [(9,9),(9,8),(8,8),(8,9),(9,7),(8,7),(7,7),(7,8),(7,9),(9,6),(8,6),(9,5),(6,9),(5,9),(6,8)]
        self.piecesTargetOrderPlayer2 = [(0, 0), (0, 1), (1, 1), (1, 0), (0, 2), (1, 2), (2, 2), (2, 1), (2, 0), (0, 3), (1, 3), (0, 4), (3, 0), (4, 0), (3, 1)]
    
    #Update game to minimax when there is a move
    def updateGame(self,game):
        self.game = game

    def alphaBetaSearch(self,game,alpha,beta,depth):
        value,move = self.maxValue(game,alpha,beta,depth)
        self.turnCount+=1
        print(value)
        return move #("Eval Function")
        
    def maxValue(self,game,alpha,beta,depth): 
        isTerminal=game.checkWin()
        if(depth==0 or isTerminal!=False):
            return self.evalFunction(game,isTerminal),None #Eval Function
        value = float("-inf")
        for action in game.checkPossibleMoves():
            value2,action2=self.minValue(game.moveActionCopy(action),alpha,beta,depth-1)
            if(value2>value):
                value,move = value2,action
                alpha = max(alpha,value)
            if(value>=beta):
                return value,move
        return value,move

    def minValue(self,game,alpha,beta,depth): 
        isTerminal=game.checkWin()
        if(depth==0 or isTerminal!=False):
            return self.evalFunction(game,isTerminal),None #Eval Function
        value = float("inf")
        for action in game.checkPossibleMoves():
            value2,action2=self.maxValue(game.moveActionCopy(action),alpha,beta,depth-1)
            if(value2<value):
                value,move = value2,action
                beta = min(beta,value)
            if(value<=alpha):
                return value,move
        return value,move

    def evalFunction(self,game,checkWin):
        if(self.playerMaxColor==PLAYER_1_COLOR):
            return self.evalFunction3(game,checkWin)
            #evalFunction3
        else:
            #return self.evalFunction4(game,checkWin)
            return self.evalFunction6(game,checkWin)

    def evalFunction3(self,game,checkWin):
        #Utility function
        if(checkWin==self.playerMaxColor):
            return float('inf')
        elif(checkWin==self.playerMinColor):
            return float('-inf')
        else:
            pointsPlayer1=0
            pointsPlayer2=0
            #Target Piece Player 1
            indexTargetPiecePlayer1=0
            targetPiecePlayer1 = self.piecesTargetOrderPlayer1[indexTargetPiecePlayer1]
            pieceInTargetPlayer1= game.board.board[targetPiecePlayer1[0]][targetPiecePlayer1[1]]
            if(self.turnCount>20):
                while(pieceInTargetPlayer1.color==PLAYER_1_COLOR):
                    indexTargetPiecePlayer1=indexTargetPiecePlayer1+1
                    targetPiecePlayer1 = self.piecesTargetOrderPlayer1[indexTargetPiecePlayer1]
                    pieceInTargetPlayer1= game.board.board[targetPiecePlayer1[0]][targetPiecePlayer1[1]]
                    pointsPlayer1 = pointsPlayer1 + 2
            # Target Piece Player 2 
            indexTargetPiecePlayer2=0
            targetPiecePlayer2 = self.piecesTargetOrderPlayer2[indexTargetPiecePlayer2]
            pieceInTargetPlayer2= game.board.board[targetPiecePlayer2[0]][targetPiecePlayer2[1]]
            if(self.turnCount>20):
                while(pieceInTargetPlayer2.color==PLAYER_2_COLOR):
                    indexTargetPiecePlayer2=indexTargetPiecePlayer2+1
                    targetPiecePlayer2 = self.piecesTargetOrderPlayer2[indexTargetPiecePlayer2]
                    pieceInTargetPlayer2= game.board.board[targetPiecePlayer2[0]][targetPiecePlayer2[1]]
                    pointsPlayer1 = pointsPlayer1 + 2
            for i in range(len(game.board.piecesPlayer1)):
                piecePlayer1=game.board.piecesPlayer1[i]
                piecePlayer2=game.board.piecesPlayer2[i]
                normRowPlayer1=piecePlayer1.row
                normColPlayer1=piecePlayer1.col
                # normRowPlayer2=(piecePlayer2.row-9)*-1
                # normColPlayer2=(piecePlayer2.col-9)*-1
                normRowPlayer2=piecePlayer2.row
                normColPlayer2=piecePlayer2.col
                pointsPiecePlayer1= ((targetPiecePlayer1[0]-normRowPlayer1)**2 + (targetPiecePlayer1[1]-normColPlayer1)**2)*3/5
                pointsPiecePlayer2= ((targetPiecePlayer2[0]-normRowPlayer2)**2 + (targetPiecePlayer2[1]-normColPlayer2)**2)*3/5
                # if(normRowPlayer1+normColPlayer1<=4):
                # pointsPiecePlayer1 = normRowPlayer1+normColPlayer1
                # pointsPiecePlayer2 = normRowPlayer2+normColPlayer2
                # elif():
                pointsPlayer1=pointsPlayer1+pointsPiecePlayer1
                pointsPlayer2=pointsPlayer2 +pointsPiecePlayer2
            if(self.playerMaxColor==PLAYER_1_COLOR):
                return -(pointsPlayer1-pointsPlayer2)
            else:
                return -(pointsPlayer2-pointsPlayer1)

    def evalFunction6(self,game,checkWin):
        #Utility function
        if(checkWin==self.playerMaxColor):
            return float('inf')
        elif(checkWin==self.playerMinColor):
            return float('-inf')
        else:
            pointsPlayer1=0
            pointsPlayer2=0
            #Target Piece Player 1
            indexTargetPiecePlayer1=0
            targetPiecePlayer1 = self.piecesTargetOrderPlayer1[indexTargetPiecePlayer1]
            pieceInTargetPlayer1= game.board.board[targetPiecePlayer1[0]][targetPiecePlayer1[1]]
            while(pieceInTargetPlayer1.color==PLAYER_1_COLOR):
                indexTargetPiecePlayer1=indexTargetPiecePlayer1+1
                targetPiecePlayer1 = self.piecesTargetOrderPlayer1[indexTargetPiecePlayer1]
                pieceInTargetPlayer1= game.board.board[targetPiecePlayer1[0]][targetPiecePlayer1[1]]
            # Target Piece Player 2 
            indexTargetPiecePlayer2=0
            targetPiecePlayer2 = self.piecesTargetOrderPlayer2[indexTargetPiecePlayer2]
            pieceInTargetPlayer2= game.board.board[targetPiecePlayer2[0]][targetPiecePlayer2[1]]
            while(pieceInTargetPlayer2.color==PLAYER_2_COLOR):
                indexTargetPiecePlayer2=indexTargetPiecePlayer2+1
                targetPiecePlayer2 = self.piecesTargetOrderPlayer2[indexTargetPiecePlayer2]
                pieceInTargetPlayer2= game.board.board[targetPiecePlayer2[0]][targetPiecePlayer2[1]]
            for i in range(len(game.board.piecesPlayer1)):
                piecePlayer1=game.board.piecesPlayer1[i]
                piecePlayer2=game.board.piecesPlayer2[i]
                normRowPlayer1=piecePlayer1.row
                normColPlayer1=piecePlayer1.col
                # normRowPlayer2=(piecePlayer2.row-9)*-1
                # normColPlayer2=(piecePlayer2.col-9)*-1
                normRowPlayer2=piecePlayer2.row
                normColPlayer2=piecePlayer2.col
                try:
                    pointsPiecePlayer1= ((((targetPiecePlayer1[0]-normRowPlayer1)**2 + (targetPiecePlayer1[1]-normColPlayer1)**2)**(1/2))/13)**(-1)
                except:
                    pointsPiecePlayer1=10
                try:
                    pointsPiecePlayer2= ((((targetPiecePlayer2[0]-normRowPlayer2)**2 + (targetPiecePlayer2[1]-normColPlayer2)**2)**(1/2))/13)**(-1)
                except:
                    pointsPiecePlayer2=10
                
                
                # if(normRowPlayer1+normColPlayer1<=4):
                # pointsPiecePlayer1 = normRowPlayer1+normColPlayer1
                # pointsPiecePlayer2 = normRowPlayer2+normColPlayer2
                # elif():
                pointsPlayer1=pointsPlayer1+pointsPiecePlayer1
                pointsPlayer2=pointsPlayer2 +pointsPiecePlayer2
            if(self.playerMaxColor==PLAYER_1_COLOR):
                return (pointsPlayer1-pointsPlayer2)
            else:
                return (pointsPlayer2-pointsPlayer1)

    def evalFunction5(self,game,checkWin):
        #Utility function
        if(checkWin==self.playerMaxColor):
            return float('inf')
        elif(checkWin==self.playerMinColor):
            return float('-inf')
        else:
            pointsPlayer1=0
            pointsPlayer2=0
            for i in range(len(game.board.piecesPlayer1)):
                piecePlayer1=game.board.piecesPlayer1[i]
                piecePlayer2=game.board.piecesPlayer2[i]
                normRowPlayer1=piecePlayer1.row
                normColPlayer1=piecePlayer1.col
                normRowPlayer2=(piecePlayer2.row-9)*-1
                normColPlayer2=(piecePlayer2.col-9)*-1
                pointsPiecePlayer1= ((9-normRowPlayer1)**2 + (9-normColPlayer1)**2)**2
                pointsPiecePlayer2= ((9-normRowPlayer2)**2 + (9-normColPlayer2)**2)**2
                # if(normRowPlayer1+normColPlayer1<=4):
                # pointsPiecePlayer1 = normRowPlayer1+normColPlayer1
                # pointsPiecePlayer2 = normRowPlayer2+normColPlayer2
                # elif():
                

                pointsPlayer1=pointsPlayer1+pointsPiecePlayer1
                pointsPlayer2=pointsPlayer2 +pointsPiecePlayer2
            if(self.playerMaxColor==PLAYER_1_COLOR):
                return -(pointsPlayer1-pointsPlayer2)
            else:
                return -(pointsPlayer2-pointsPlayer1)
                
    def evalFunction4(self,game,checkWin):
        #Utility function
        if(checkWin==self.playerMaxColor):
            return float('inf')
        elif(checkWin==self.playerMinColor):
            return float('-inf')
        else:
            pointsPlayer1=0
            pointsPlayer2=0
            for i in range(len(game.board.piecesPlayer1)):
                piecePlayer1=game.board.piecesPlayer1[i]
                piecePlayer2=game.board.piecesPlayer2[i]
                normRowPlayer1=piecePlayer1.row
                normColPlayer1=piecePlayer1.col
                normRowPlayer2=(piecePlayer2.row-9)*-1
                normColPlayer2=(piecePlayer2.col-9)*-1
                pointsPiecePlayer1= ((9-normRowPlayer1)**2 + (9-normColPlayer1)**2)**(1/2)
                pointsPiecePlayer2= ((9-normRowPlayer2)**2 + (9-normColPlayer2)**2)**(1/2)
                # if(normRowPlayer1+normColPlayer1<=4):
                # pointsPiecePlayer1 = normRowPlayer1+normColPlayer1
                # pointsPiecePlayer2 = normRowPlayer2+normColPlayer2
                # elif():
                

                pointsPlayer1=pointsPlayer1+pointsPiecePlayer1
                pointsPlayer2=pointsPlayer2 +pointsPiecePlayer2
            if(self.playerMaxColor==PLAYER_1_COLOR):
                return -(pointsPlayer1-pointsPlayer2)
            else:
                return -(pointsPlayer2-pointsPlayer1)

    def evalFunction2(self,game,checkWin=None):
        #Utility function
        if(checkWin==self.playerMaxColor):
            return float('inf')
        elif(checkWin==self.playerMinColor):
            return float('-inf')
        else:
            pointsPlayer1=0
            pointsPlayer2=0
            for i in range(len(game.board.piecesPlayer1)):
                piecePlayer1=game.board.piecesPlayer1[i]
                piecePlayer2=game.board.piecesPlayer2[i]
                normRowPlayer1=piecePlayer1.row
                normColPlayer1=piecePlayer1.col
                normRowPlayer2=(piecePlayer2.row-9)*-1
                normColPlayer2=(piecePlayer2.col-9)*-1
                try:
                    pointsPiecePlayer1= ((9-normRowPlayer1)**2 + (9-normColPlayer1)**2)**(-1/2)
                except:
                    pointsPiecePlayer1=1.1
                try:
                    pointsPiecePlayer2= ((9-normRowPlayer2)**2 + (9-normColPlayer2)**2)**(-1/2)
                except:
                    pointsPiecePlayer2=1.1
                
                # if(normRowPlayer1+normColPlayer1<=4):
                # pointsPiecePlayer1 = normRowPlayer1+normColPlayer1
                # pointsPiecePlayer2 = normRowPlayer2+normColPlayer2
                # elif():
                

                pointsPlayer1=pointsPlayer1+pointsPiecePlayer1
                pointsPlayer2=pointsPlayer2 +pointsPiecePlayer2
            if(self.playerMaxColor==PLAYER_1_COLOR):
                return (pointsPlayer1-pointsPlayer2)
            else:
                return (pointsPlayer2-pointsPlayer1)
 

    