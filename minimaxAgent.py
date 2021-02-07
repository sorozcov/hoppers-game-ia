# Author:Silvio Orozco 18282
# Universidad del Valle
# Ingenieria en Ciencias de la Computación
# Hoppers game with AI
# Hoppers minimaxAgent.py
from game_options import PLAYER_1_COLOR,PLAYER_2_COLOR

class MinimaxAgent():
    #Receives a game as starter
    def __init__(self,game,playerMaxColor=PLAYER_1_COLOR):
        self.game = game
        self.color= playerMaxColor
        self.playerMaxColor = playerMaxColor
        self.playerMinColor = PLAYER_2_COLOR if self.playerMaxColor==PLAYER_1_COLOR else PLAYER_1_COLOR
        self.depth =3

    #Update game to minimax when there is a move
    def updateGame(self,game):
        self.game = game

    def alphaBetaSearch(self,game,alpha,beta,depth):
        value,move = self.maxValue(game,alpha,beta,depth)
        print(value)
        return move #("Eval Function")
        
    def maxValue(self,game,alpha,beta,depth): 
        if(depth==0 or game.checkWin()!=False):
            return self.evalFunction(game),None #Eval Function
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
        if(depth==0 or game.checkWin()!=False):
            return self.evalFunction(game),None #Eval Function
        value = float("inf")
        for action in game.checkPossibleMoves():
            value2,action2=self.maxValue(game.moveActionCopy(action),alpha,beta,depth-1)
            if(value2<value):
                value,move = value2,action
                beta = min(beta,value)
            if(value<=alpha):
                return value,move
        return value,move

    def evalFunction(self,game):
        #Utility function
        if(game.checkWin()==self.playerMaxColor):
            return float('inf')
        elif(game.checkWin()==self.playerMinColor):
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
                pointsPiecePlayer1= ((9-normRowPlayer1)**2 + (9-normColPlayer1)**2)**1/2
                pointsPiecePlayer2= ((9-normRowPlayer2)**2 + (9-normColPlayer2)**2)**1/2
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
 

    