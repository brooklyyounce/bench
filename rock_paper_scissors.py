import random
while True:
  print "\n\n\n    **Welcome to Rock, Paper, Scissors!**"
  play = raw_input("Shoot: ").lower()[0]
  possiblePlays = ['Rock', 'Paper', 'Scissors']
  computerPlay = random.choice(possiblePlays).lower()[0]
  print "\n\nThe computer played: " + computerPlay
  playerWin = tie = False
  if((play == 'r' and computerPlay == 's') or (play == 'p' and computerPlay == 'r') or (play == 's' and computerPlay == 'p')):
    print "\n\n** You win!!"
  elif (computerPlay == play):
    print "\n\n**It was a tie!!"
  else:
    print "\n\n**The computer won this time! Bummer. Try again!"
