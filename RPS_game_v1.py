""" builing the game
user input """

from random import randint
from time import sleep
rps = ["ROCK","PAPER","SCISSOR"]
msg = {"tie":"YAWN its a tie!","won":"YAYee you won!","lost":"AWW you lost!"}

def decide_winner(user_choice,computer_choice):
  print (" ")
  print ("You have selected: %s" % user_choice)
  sleep(1)
  print (" ")
  print ("Computer selected: %s" % computer_choice)
  sleep(1)
  if user_choice == computer_choice:
    print (" ")
    print (msg["tie"])
    print (" ")
    sleep(1)
  elif user_choice == rps[0] and computer_choice == rps[2]:
    print (" ")
    print (msg["won"])
    print (" ")
    sleep(1)
  elif user_choice == rps[1] and computer_choice == rps[0]:
    print (" ")
    print (msg["won"])
    print (" ")
    sleep(1)
  elif user_choice == rps[2] and computer_choice == rps[1]:
    print (" ")
    print (msg["won"])
    print (" ")
    sleep(1)
  else:
    print (" ")
    print (msg["lost"])
    print (" ")
    sleep(1)
            

def user_input():
  print ( " ")
  print ("    WELCOME TO ROCK,PAPER & SCISSOR BY Z v1.0")
  print (" ")
  x = input("Enter ROCK-R, PAPER-P, or SCISSOR-S: ")
  x = x.lower()
  if len(x) == 1 and x == "r":
    x = "ROCK"
    user_choice = x
  elif len(x) ==1 and x == "s":
    x = "SCISSOR"
    user_choice = x
  elif len(x) == 1 and x == "p":
    x = "PAPER"
    user_choice = x
  else:
    user_choice = x
    
  play_rps(user_choice)


def play_rps(user_choice): 
  user_choice = user_choice.upper()
  computer_choice = rps[randint(0,2)]
  decide_winner(user_choice, computer_choice)
  
while True:
  user_input()
  



#trying a separate input function to take inputs both as "ROCK" or "R"



   

