# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 20:31:01 2020

@author: sid
"""

#guess_number=89
#turns=9
#while(turns):
    #if turns==1:
        #print("you have",turns,"turn")
    #else:
       # print("you have",turns,"turns")
   # num=input("Enter number between 1-100: ")
   # if int(num)==guess_number:
       # print("You won")
       # break
   # turns-=1
    #if turns==0:
       # print("you lost")

import random
guess=random.randint(1,10)
chance=6
name=input("Ener your name: ")
print("hello,",name)
print("Guess no. between 1-10")
while(chance):
    num=int(input("Enter no.: "))
    if num<guess:
        print("too low")
    elif guess<num:
        print("too high")
    elif num==guess:
        print("you won")
        break
    chance-=1
    if chance==0:
        print("The number is,",guess)
    