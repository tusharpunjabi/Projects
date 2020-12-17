# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 15:51:05 2020

@author: sid
"""
#import random
#a=["x","o"]
#letter=input("enter letter").upper()
#print(letter)
#select=random.randint(0,1)
#print(a[select])
def gboard(board):
    print(board[7]+"|"+board[8]+"|"+board[9])
    print("-+-+-")
    print(board[4]+"|"+board[5]+"|"+board[6])
    print("-+-+-")
    print(board[1]+"|"+board[2]+"|"+board[3])
    return ""
board=[" "," "," "," "," "," "," "," "," "," "," "]
def counting(turn, board):
        if board[8]==board[7]==board[9]!=" ":
            print(gboard(board))
            print("Hooray!! You won,",turn)
            return True
        elif board[5]==board[4]==board[6]!=" ":
            print(gboard(board))
            print("Hooray!! You won,",turn)
            return True
        elif board[2]==board[1]==board[3]!=" ":
            print(gboard(board))
            print("Hooray!! You won,",turn)
            return True
        elif board[7]==board[5]==board[3]!=" ":
            print(gboard(board))
            print("Hooray!! You won,",turn)
            return True
        elif board[9]==board[5]==board[1]!=" ":
            print(gboard(board))
            print("Hooray!! You won,",turn)
            return True
        elif board[5]==board[8]==board[2]!=" ":
            print(gboard(board))
            print("Hooray!! You won,",turn)
            return True
        elif board[7]==board[4]==board[1]!=" ":
            print(gboard(board))
            print("Hooray!! You won,",turn)
            return True
        elif board[6]==board[9]==board[3]!=" ":
            print(gboard(board))
            print("Hooray!! You won,",turn)
            return True
def game():
    board=[" "," "," "," "," "," "," "," "," "," "]
    turn=input("Select either X or O ").upper()

    count=0
    while(1):
        gboard(board)
        print("It's your turn",turn,",where would you like you move? ")
        move=int(input())
        
        if board[move]==" ":
            board[move]=turn
            count+=1
        else:
            print("This place is already occupied.")
        if count>=5:
            result=counting(turn, board)
            if result==True:
                break
        if count==9:
            print(gboard(board))
            print("It's a TIE")
            break
        if turn=="X":
            turn="O"
        else:
            turn="X"
            
        
game()
        
        
        
        
        
        
        