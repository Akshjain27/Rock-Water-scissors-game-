#  install the random Module:  pip install random2    
import random        # This module create the random value

randomnumber =random.randint(1,3)     #in randint fuction create 1 to 3 random value

def game():
    if randomnumber==1:        #if randomnumber create 1 to print the "r"
        print("r")
    elif randomnumber==2:       #if randomnumber create 2 to print the "p"
     print("p")
    else:
     print("s")                 #else randomnumber create 3 and print the "s"


a = input("Your Turn Rock(r), Paper(p), Scissor(s) choose one? " )     # input by the user Rock(r), Paper(p), Scissor(s) choose one?
print("Computer Turn Rock(r), Paper(p), Scissor(s) choose one?",end=" "),game()     # game() fuction print Rock(r), Paper(p), Scissor(s) from computer


if a in "r":                        # if user choose "r"      
     if  randomnumber == 2:         # if randomnumber is 2 ("p")     
          print ("you lose")        # paper("p") killed the rock("r") and user is lose and computer is win

if  a in "r":                       # if user choose "r"
     if randomnumber == 3:          # if randomnumber is 3 ("s") 
          print ("you win")         # rock("r") killed the scissor("s") and user is lose and computer is win

if a in "r":                        # if user choose "r"
     if  randomnumber == 1:         # if randomnumber is 1 ("r") 
          print ("Match is tied")   # rock("r") == rock("r") Match is tied              



if a in "p":
     if  randomnumber == 3:
          print ("you lose")

if a in "p":
     if  randomnumber == 1:
          print ("you win")  

if a in "p":
     if  randomnumber == 2:
          print ("Match is tied") 



if a in "s":
     if  randomnumber == 1:
          print ("you lose")

if a in "s":
     if  randomnumber == 2:
          print ("you win")  
          
if a in "s":
     if  randomnumber == 3:
          print ("Match is tied")                 



