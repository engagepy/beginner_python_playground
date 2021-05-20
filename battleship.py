#import function random(low,high)

from random import randint
from time import sleep

#an empty board to populate

board = []

#append "o"

for x in range(5):
  board.append(["O"] * 5)

#new join function learnt

def print_board(board):
  for row in board:
    print (" ".join(row))

print_board(board)

#to check board len()

'''print (len(board))'''

#computer battleship position selection function

def random_row(board):
  return randint(0, len(board) - 1)

def random_col(board):
  return randint(0, len(board[0]) - 1)

#for debugging could print random_row,random_col

ship_row = random_row(board)
ship_col = random_col(board)

def suspense():
        print(" ")
        print ("Launching Attack")
        print (" ")
        sleep(1) 
        print (".")
        sleep(1) 
        print ("..") 
        sleep(1) 
        print("... \n")
        print ("Missile Fired")
        sleep(1)
        print (" ") 





# Everything from here on in for loop

for turn in range(4):
  print (" ")
  print ("Turn", turn + 1)
  print (" ")
  print ("Rows & Cols range between 0 - 4")
  print (" ")
  
  guess_row = int(input("Guess Row: "))
  guess_col = int(input("Guess Col: "))

  suspense() 

  if guess_row == ship_row and guess_col == ship_col:
    print ("Congratulations! You sunk my battleship!")
    board[guess_row][guess_col] = "$"
    print_board(board)
    break
  else:
    if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
      print ("Oops, that's not even in the ocean.")
      print (" ")
    elif(board[guess_row][guess_col] == "X"):
      print ("You guessed that one already.")
      print (" ") 
    else:
      print ("You missed my battleship!")
      print (" ")
      board[guess_row][guess_col] = "X"
    if turn == 3:
      print ("Game Over")
      print (" ")
      print (" ")
      print ("Actual location of battle ship ",ship_row,ship_col)
      print (" ")
      print (" ")
      board[ship_row][ship_col]="$"
  print_board(board)
  
