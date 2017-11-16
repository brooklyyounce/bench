import random

def constructBoard(noose, hangMan, numWrongGuesses):
  num = numWrongGuesses + 1
  man = ["", "", "", "", ""]
  board = []
  for x in range(num):
    man[x] = hangMan[x]
  for x in range(len(noose)):
    board.append(noose[x] + man[x])
  return board

def displayBoard(board, secretWord, guessedLetters, wrongGuesses):
  print "\nAll guesses: " + guessedLetters
  print "\nWrong guesses: " + wrongGuesses
  
  for x in range(len(board)):
    print board[x]

  print "             Secret word : " + secretWord
  
def getLetterGuess(guessedLetters):
  tryAgain = True
  letter = ''
  while(tryAgain):
    letter = raw_input("Please guess a letter: ")
    if(letter[0].isdigit() == False and len(letter) > 0 and len(letter.strip(' ')) > 0):
      if(letter not in guessedLetters):
        tryAgain = False
      else:
        print "**You've already guessed that letter. Try again, please."
    else:
      print "**Please only enter one letter, try again."
  return letter[0].lower()

def insertLetter(guessWord, secretWord, letter):
  temp = list(secretWord)
  for x in range(len(guessWord)):
    if(guessWord[x] == letter):
      temp[x] = letter
  return ''.join(temp)
 
def numCharsInWord(letter, guessWord):
  count = 0
  temp = list(guessWord)
  for x in range(len(temp)):
    if(temp[x] == letter):
      count = count + 1
  return count
  
hangMan = ["", "O","\|/", " |", "/ \\"]

noose = ["  /---  ", "  |   \\", "  |   ", "  |   ", "__|__ "]

  
board = []
guessedLetters = ""
wrongGuesses = ""
manSoFar = ["", "", "", ""]

possibleWords = ["Balderdash", "Bullocks", "England", "America", "Crystals", "Library", "Tadploes", "Alligators", "Dolphins", "Cantaloupe", "Wind", "Blue", "Cornocopia", "Chicken", "Mumbai", "Kuwait", "Xray", "Trombone", "Cymbals", "Gopher", "Georgia", "Vicariously", "Vendetta", "Watermelon", "Mother", "Quietly", "Wastebasket", "Rhino", "Toasty", "Yarn", "Umbilical", "Igloo", "Pansy", "Albatross", "Sexy", "Dandelions", "Franklin", "Giraffe", "Husking", "Jojoba", "Kangaroo", "Lioness", "Zoo", "Xylophone", "Cranberries", "Vicious", "Bologna", "Nuanced", "Maui"]

totalNumWrongGuessesAllowed = 4
numWrongGuessesSoFar = 0
numGuessesSoFar = 0
numCorrectGuesses = 0

guessWord = random.choice(possibleWords).lower()
lengthOfWord = len(guessWord)
secretWord = ""

for x in range(lengthOfWord):
  secretWord = secretWord + "*"

while (numCorrectGuesses < lengthOfWord and numWrongGuessesSoFar < totalNumWrongGuessesAllowed):
  board = constructBoard(noose, hangMan, numWrongGuessesSoFar)
  displayBoard(board, secretWord, guessedLetters, wrongGuesses)
  
  guessedLetter = getLetterGuess(guessedLetters)
  result = -1
  try:
    result = guessWord.lower().index(guessedLetter)
  except:
    result = -1
  
  numGuessesSoFar = numGuessesSoFar + 1
  guessedLetters = guessedLetters + " " + guessedLetter
  
  if(result == -1):
    numWrongGuessesSoFar = numWrongGuessesSoFar + 1
    wrongGuesses = wrongGuesses + " " + guessedLetter
    print "\n\n**Nope. That letter isn't in there!"
    
  else:
    numCorrectGuesses = numCorrectGuesses + numCharsInWord(guessedLetter, guessWord)
    secretWord = insertLetter(guessWord, secretWord, guessedLetter)

    
if(numCorrectGuesses == lengthOfWord):
  print "\n\n****** You win! You guessed the word before the poor man died! ******"
else:
  print "\n\n You lost. The poor man hung from the neck until he expired...."
  print "Dun dun dun..."
  print "X("
  print "The word was: " + guessWord
print "\n                       FINAL RESULTS"
board = constructBoard(noose, hangMan, numWrongGuessesSoFar)
displayBoard(board, secretWord, guessedLetters, wrongGuesses)
