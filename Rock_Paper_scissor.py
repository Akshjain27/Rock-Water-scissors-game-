# from ast import get_docstring
import random

rand =random.randint(1,3)

def game():
    if rand==1:
        print("r")
    elif rand==2:
     print("p")
    else:
     print("s")  


a = input("Your Turn Rock(r), Paper(p), Scissor(s) choose one? " )
print("Computer Turn Rock(r), Paper(p), Scissor(s) choose one?",end=" "),game()


if a in "r":
     if  rand == 2:
          print ("you lose")
if a in "r":
     if  rand == 3:
          print ("you win")  
if a in "r":
     if  rand == 1:
          print ("Match is tied")                 

if a in "p":
     if  rand == 3:
          print ("you lose")
if a in "p":
     if  rand == 1:
          print ("you win")  
if a in "p":
     if  rand == 2:
          print ("Match is tied") 

if a in "s":
     if  rand == 1:
          print ("you lose")

if a in "s":
     if  rand == 2:
          print ("you win")  
if a in "s":
     if  rand == 3:
          print ("Match is tied")                 



