# Author:Silvio Orozco 18282
# Universidad del Valle
# Ingenieria en Ciencias de la Computación
# Hoppers game with AI
# Hoppers minimaxAgent.py
from game_options import PLAYER_1_COLOR,PLAYER_2_COLOR
import numpy as np

#Minimax agent
class MinimaxAgent():
    #Receives a game as starter and the maximizer color
    def __init__(self,game,playerMaxColor=PLAYER_1_COLOR):
        self.game = game
        self.color= playerMaxColor
        self.playerMaxColor = playerMaxColor
        self.playerMinColor = PLAYER_2_COLOR if self.playerMaxColor==PLAYER_1_COLOR else PLAYER_1_COLOR
        self.depth =3
        self.turnCount = 0
        self.indexTargetPiecePlayer1 = 0
        self.indexTargetPiecePlayer2 = 0
        self.piecesTargetOrderPlayer1 = [(9,9),(9,8),(8,8),(8,9),(9,7),(8,7),(7,7),(7,8),(7,9),(9,6),(8,6),(9,5),(6,9),(5,9),(6,8)]
        self.piecesTargetOrderPlayer2 = [(0, 0), (0, 1), (1, 1), (1, 0), (0, 2), (1, 2), (2, 2), (2, 1), (2, 0), (0, 3), (1, 3), (0, 4), (3, 0), (4, 0), (3, 1)]

    #Update game to minimax when there is a move
    def updateGame(self,game):
        self.game = game

    #Check target pieces for minimax algorithm
    def checkTargetPieces(self,game):
        #Target Piece Player 1
        self.targetPiecePlayer1=self.piecesTargetOrderPlayer1[self.indexTargetPiecePlayer1]
      
        for x in range(self.indexTargetPiecePlayer1,len(self.piecesTargetOrderPlayer1)-1):
            target = self.piecesTargetOrderPlayer1[x]
            if(game.board.getPiece(target[0],target[1]).color==PLAYER_1_COLOR):
                self.indexTargetPiecePlayer1 = self.indexTargetPiecePlayer1 + 1
                self.targetPiecePlayer1=self.piecesTargetOrderPlayer1[self.indexTargetPiecePlayer1]
            else:
                break
        #Target Piece Player 2
        self.targetPiecePlayer2=self.piecesTargetOrderPlayer2[self.indexTargetPiecePlayer2]
        for x in range(self.indexTargetPiecePlayer2,len(self.piecesTargetOrderPlayer2)-1):
            target = self.piecesTargetOrderPlayer2[x]
            if(game.board.getPiece(target[0],target[1]).color==PLAYER_2_COLOR):
                self.indexTargetPiecePlayer2 = self.indexTargetPiecePlayer2 + 1
                self.targetPiecePlayer2=self.piecesTargetOrderPlayer2[self.indexTargetPiecePlayer2]
            else:
                break

    #Alphabeta search 
    def alphaBetaSearch(self,game,alpha,beta,depth):
        self.checkTargetPieces(game)
        value,move = self.maxValue(game,alpha,beta,depth)
        return move #("Eval Function")

    #Max value with prunning
    def maxValue(self,game,alpha,beta,depth):
        isTerminal=game.checkWin()
        if(depth==0 or isTerminal!=False):
            return self.evalFunction(game,isTerminal),None #Eval Function
        value = float("-inf")
        for action in game.checkPossibleMoves(self.piecesTargetOrderPlayer1[0:self.indexTargetPiecePlayer1]):
            value2,action2=self.minValue(game.moveActionCopy(action),alpha,beta,depth-1)
            if(value2>value):
                value,move = value2,action
                alpha = max(alpha,value)
            if(value>=beta):
                return value,move
        return value,move

    #Min value with prunning
    def minValue(self,game,alpha,beta,depth):
        isTerminal=game.checkWin()
        if(depth==0 or isTerminal!=False):
            return self.evalFunction(game,isTerminal),None #Eval Function
        value = float("inf")
        for action in game.checkPossibleMoves(self.piecesTargetOrderPlayer1[0:self.indexTargetPiecePlayer2]):
            value2,action2=self.maxValue(game.moveActionCopy(action),alpha,beta,depth-1)
            if(value2<value):
                value,move = value2,action
                beta = min(beta,value)
            if(value<=alpha):
                return value,move
        return value,move

    #Eval function
    def evalFunction(self,game,checkWin):
        if(self.playerMaxColor==PLAYER_1_COLOR):
            return self.evalFunctionDistance(game,checkWin)
        else:
            return self.evalFunctionDistance(game,checkWin)

    #Space of different evaluation functions

    def evalFunctionDistance(self,game,checkWin):
        #Utility function
        if(checkWin==self.playerMaxColor):
            return float('inf')
        elif(checkWin==self.playerMinColor):
            return float('-inf')
        else:
            #Base player points on distance to a target space on board
            pointsPlayer1=0
            pointsPlayer2=0
            targetPiecePlayer1 = self.targetPiecePlayer1
            targetPiecePlayer2 = self.targetPiecePlayer2
            for i in range(len(game.board.piecesPlayer1)):
                piecePlayer1=game.board.piecesPlayer1[i]
                piecePlayer2=game.board.piecesPlayer2[i]
                normRowPlayer1=piecePlayer1.row
                normColPlayer1=piecePlayer1.col

                normRowPlayer2=piecePlayer2.row
                normColPlayer2=piecePlayer2.col
                if(normRowPlayer1+normColPlayer1>=14):
                    pointsPlayer1 = pointsPlayer1 - 25
                if(normRowPlayer1==targetPiecePlayer1[0] and normColPlayer1==targetPiecePlayer1[1]):
                     pointsPlayer1 = pointsPlayer1 - 100
                if(normRowPlayer2+normColPlayer2<=4):
                    pointsPlayer2 = pointsPlayer2 - 25
                if(normRowPlayer2==targetPiecePlayer2[0] and normColPlayer2==targetPiecePlayer2[1]):
                     pointsPlayer2 = pointsPlayer2 - 15
                pointsPiecePlayer1= ((targetPiecePlayer1[0]-normRowPlayer1)**2 + (targetPiecePlayer1[1]-normColPlayer1)**2)*1/2
                pointsPiecePlayer2= ((targetPiecePlayer2[0]-normRowPlayer2)**2 + (targetPiecePlayer2[1]-normColPlayer2)**2)*1/2
                
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
            targetPiecePlayer1=self.piecesTargetOrderPlayer1[0]
            for x in range(len(self.piecesTargetOrderPlayer1)-1):
                target = self.piecesTargetOrderPlayer1[x]
                if(game.board.getPiece(target[0],target[1]).color==PLAYER_1_COLOR):
                    target = self.piecesTargetOrderPlayer1[x+1]
                    targetPiecePlayer1 = target
            #Target Piece Player 2
            targetPiecePlayer2=self.piecesTargetOrderPlayer2[0]
            for x in range(len(self.piecesTargetOrderPlayer2)-1):
                target = self.piecesTargetOrderPlayer2[x]
                if(game.board.getPiece(target[0],target[1]).color==PLAYER_2_COLOR):
                    target = self.piecesTargetOrderPlayer2[x+1]
                    targetPiecePlayer2 = target

            for i in range(len(game.board.piecesPlayer1)):
                piecePlayer1=game.board.piecesPlayer1[i]
                piecePlayer2=game.board.piecesPlayer2[i]
                normRowPlayer1=piecePlayer1.row
                normColPlayer1=piecePlayer1.col
                # normRowPlayer2=(piecePlayer2.row-9)*-1
                # normColPlayer2=(piecePlayer2.col-9)*-1
                normRowPlayer2=piecePlayer2.row
                normColPlayer2=piecePlayer2.col
                if(normRowPlayer1+normColPlayer1>=14):
                    pointsPlayer1 = pointsPlayer1 -25
                if(normRowPlayer1==targetPiecePlayer1[0] and normColPlayer1==targetPiecePlayer1[1]):
                     pointsPlayer1 = pointsPlayer1 -30
                if(normRowPlayer2+normColPlayer2<=4):
                    pointsPlayer2 = pointsPlayer2 -25
                if(normRowPlayer2==targetPiecePlayer2[0] and normColPlayer2==targetPiecePlayer2[1]):
                     pointsPlayer2 = pointsPlayer2 -30
                try:
                    pointsPiecePlayer1= ((((targetPiecePlayer1[0]-normRowPlayer1)**2 + (targetPiecePlayer1[1]-normColPlayer1)**2)**(12/2)))
                except:
                    pointsPiecePlayer1=2
                try:
                    pointsPiecePlayer2= ((((targetPiecePlayer2[0]-normRowPlayer2)**2 + (targetPiecePlayer2[1]-normColPlayer2)**2)**(12/2)))
                except:
                    pointsPiecePlayer2=2


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


