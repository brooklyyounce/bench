from random import randint
from sys import exit

def DisplayGreeting():
  print "**    Welcome to Tic-Tac-Toe!    **"
  print "Although I'm sure you know how to play..."
  
  PressEnter()
  
  print "\n\nThe board with coordinates will look something like this..."

  print "     |     |    "
  print " 0,0 | 0,1 | 0,2"
  print "_____|_____|____"
  print "     |     |    "
  print " 1,0 | 1,1 | 1,2"
  print "_____|_____|____"
  print "     |     |    "
  print " 2,0 | 2,1 | 2,2"
  print "     |     |    "
  print "\n\nThe game will ask for the X coordinate..."
  print "...and then the Y coordinate..."
  print "\n\nFor example, to make this move..."
  exampleBoard = MakeEmptyBoard()
  exampleBoard[0][1] = "X"
  DisplayBoard(exampleBoard)
  print "Input '0' for the X coordinate, hit <enter>..."
  print "Input '1' for the Y coordinate, hit <enter>..."
  print "\n**Note: Cols and rows start from the number 0, because we are programmers!**"
  print "Then the computer will take its turn..."
  print "\n\nSo let's get started!!"
  PressEnter()
  
def DisplayBoard(board):
  for x in range(len(board)):
    print "      |      |     "
    print "   " + board[x][0] + "  |   " + board[x][1] +"  |   " + board[x][2]
    if x < 2:
      print  "______|______|_____"
  print "      |      |       " 
   
def PressEnter():
  raw_input("\nPress Enter to continue...")  
  
def MakeEmptyBoard():
  board = []
  for x in range(3):
    board.append([])
    for y in range(3):
      board[x].append(" ")
  return board
  
def AvailableSpace(board, x, y):
  if(board[x][y] == " "):
    return True
  return False

def GoodCoordinate(num):
  if(num >= 0 and num <= 2):
    return True
  return False
  
def NotString(num):
  try:
    int(num)
    return True
  except:
    return False
  
def GetXMove():
  return raw_input("Enter X coordinate for move: ")

def GetYMove():
  return raw_input("Enter Y coordinate for move: ")
  
def CheckForWin(board, char):
  rowWin = False
  colWin = False
  diag1Win = False
  diag2Win = False
  for row in range(3):
    if(board[row][0] == board[row][1] == board[row][2] == char):
      rowWin = True
      break
  for col in range(3):
    if(rowWin == False and board[0][col] == board[1][col] == board[2][col] == char):
      colWin = True
      break
  if(rowWin == False and colWin == False):
    if(board[2][0] == board[1][1] == board[0][2] == char):
      diag1Win = True
    elif(board[0][0] == board[1][1] == board[2][2] == char):
      diag2Win = True
  return rowWin or colWin or diag1Win or diag2Win

def ComputerTurn(board, char):
  foundMove = False
  while(foundMove == False):
    x = randint(0,2)
    y = randint(0,2)
    available = AvailableSpace(board, x, y)
    if(available):
      board[x][y] = char
      foundMove = True
def GoodByeMessage():
  print "\n\n--> Bye! Thanks so much for playing..."
  print "\n\n"
  print "             Credits"
  print "Designer..........Brookly Younce"
  print "Costume Concepts..Brookly Younce"
  print "Director..........Brookly Younce"
  print "Programmer........Brookly Younce"
  print "Special Effects...Brookly Younce"
  print "Sound Effects.....Brookly Younce"
  print "Makeup............Brookly Younce"
  print "Hair..............Brookly Younce"
  print "Animal Caretaker..Brookly Younce"
  print "Travel Director...Brookly Younce"
  print "Refreshments......Brookly Younce"
  print "Coffee Brewer.....Brookly Younce"
  print "No animals harmed making this silly game..."
  exit(0)
  
DisplayGreeting()

totalMoves = 9
movesSoFar = 0

board = MakeEmptyBoard()

playerChar = "X"
computerChar = "O"

while(movesSoFar < totalMoves):
  tryAgain = True
  
  number = False
  goodValue = False
  available = False
  
  while(tryAgain):
    x = GetXMove()
    y = GetYMove()
    number = (NotString(x) and NotString(y))
    
    if(number):
      goodValue = GoodCoordinate(int(x)) and GoodCoordinate(int(y))
      available = AvailableSpace(board, int(x), int(y))
    
    if(number and goodValue and available):
      board[int(x)][int(y)] = playerChar
      movesSoFar = movesSoFar + 1
      playerWin = CheckForWin(board, playerChar)
      if(playerWin):
        DisplayBoard(board)
        print "\n\n***You win!"
        print "Start the game again to play some more!"
        GoodByeMessage()
      tryAgain = False
    else:
      print "\n\n**We didn't understand the values you entered, please try again.\n"
      
  print "This is the board after your turn..."
  DisplayBoard(board)
  PressEnter()
  
    
  if(movesSoFar < totalMoves):
    ComputerTurn(board, computerChar)
    computerWin = CheckForWin(board, computerChar)
    if(computerWin):
      DisplayBoard(board)
      print "\n\n**Oh no! The computer just won!!"
      print "Start the game again to play some more!"
      GoodByeMessage()
    movesSoFar = movesSoFar + 1
    print "This is the board after the Computer's turn..."
    DisplayBoard(board)
  else:
    print "\n\n***Whoops! Looks like a CAT!!"
    print "Start the game again to play some more!"
    GoodByeMessage()
   




