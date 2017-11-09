from random import randint

def Greeting():
  print "***    Welcome to MATH    ***"
  print "It's like MASH, but I like 'trailer' instead of 'shack'..."
  print "Not that your future house is gonna be in this game...tee hee"
  print "I'm the programmer, I get to pick..."
  print "\nThere are 5 categories for your fate: Spouse, Car, Number of Children, Job, and Salary..."
  print "I will ask if you want me to choose the options for you, or you can provide them..."
  print "The game will ask for your spin number to determine which options to eliminate..."
  print "To make sure that you can't predict your future, the elimination is BASED on your number..."
  print "\n\nEnough chat, let's determine your fate!"
  
def AskForName():
  tryAgain = True
  while(tryAgain):
    name = raw_input("\n\n**What is your name: ")
    name = name.strip(' ')
    if(TestInputString(name)):
      tryAgain = False
    else:
      print "\nYeah, we are gonna try that again."
  return name
  
def TestInputString(string):
  goodInput = False
  if(len(string) > 0):
    goodInput = True
  return goodInput
  
def AskIfDefaultValues():
  tryAgain = True
  while(tryAgain):
    ans = raw_input("\n\n**Do you want to list each item? - y or n: ")
    ans = ans.strip(' ')[0]
    default = False
    if(TestInputString(ans)):
      if(ans.lower() == 'y'):
        default = True
        tryAgain = False
      elif(ans.lower() == 'n'):
        default = False
        tryAgain = False
      else:
        print "**Please answer with y or n,  friend."
  return default
  
def AskForSpinnerNumber():
  tryAgain = True
  while(tryAgain):
    spinNum = raw_input("\n\n**Please tell me your spin number: ")
    spinNum = spinNum.strip(' ')
    try:
      int(spinNum)
      tryAgain = False
    except:
      print "**Please enter just a number, i.e., a postive member of the integer number line..."
  return int((randint(1, 6)*int(spinNum))/randint(1,6))
  
def DisplayBoard(spouse, car, children, job, salary):
  print "\n\n**Okay, this is what the board looks like right now..."
  DisplayValues(spouse, "Spouse")
  DisplayValues(car, "Car")
  DisplayValues(children, "Kids")
  DisplayValues(job, "Job")
  DisplayValues(salary, "Salary")

def DisplayValues(array, cateogory):
  print "\n " + cateogory
  print "--------"
  for x in range(len(array)):
    print array[x]
 
def PlayGame(masterBoard):
  while((len(masterBoard[0]) == 1 and len(masterBoard[1]) == 1 and len(masterBoard[2])== 1 and len(masterBoard[3]) == 1 and len(masterBoard[4]) == 1) == False):
    spinNum = AskForSpinnerNumber()
    counter = 0
    while(counter < spinNum):
      for x in range(len(masterBoard)):
        for y in range(len(masterBoard[x])):
          if(len(masterBoard[x]) > 1):
            counter = counter + 1
            if (counter == spinNum):
              popped = masterBoard[x].pop(y)
              print popped
              print counter
    counter = 0
    DisplayBoard(masterBoard[0], masterBoard[1], masterBoard[2], masterBoard[3], masterBoard[4])
  return masterBoard
  
def CreateMasterBoard(spouse, car, children, job, salary):
  masterBoard = [spouse, car, children, job, salary]
  return masterBoard

def DisplayFinalResults(name, masterBoard):
  print "\n\n**Alright, " + name + "! So here's how the future is going to work out for you..."
  print "-------------------------------------------------------------------------------"
  print "-You gonna marry: " + masterBoard[0][0]
  print "-You gonna drive: " + masterBoard[1][0]
  print "-You gonna have this many childrens: " + str(masterBoard[2][0])
  print "-You gonna have this job: " + masterBoard[3][0]
  print "-You gonna make this much annually: " + masterBoard[4][0]
  print "-------------------------------------------------------------------------------"

def FillArrayFromUser(cateogory, array):
  tryAgain = True
  
  for x in range(5):
    tryAgain = True
    while(tryAgain):
      ans = raw_input("\n**Enter value " + str(x+1) + " for " + cateogory + ": ")
      ans = ans.strip(' ')
      if(TestInputString(ans)):
        array.append(ans)
        tryAgain = False
      else:
        print "\n-->Try entering that one again, please."
  return array
Greeting()
name = AskForName()
defaultValues = AskIfDefaultValues()

if(defaultValues == False):
  spouse = ['Barney the Dinosaur', 'Dora the Explorer', 'Johnny Depp', 'Natalie Portman', 'George Strait']
  car = ['Hummer', 'Wagon', 'Spaceship', 'Ferrari', 'School Bus']
  children = [0, 5, 12, 2, 1]
  job = ['Sanitation Engineer', 'Hair Stylist', 'Mechanic', 'Yoga Instructor', 'Archaeologist']
  salary = ['$12,000', '$112,000', '$5,550', '$45,000', '$72,100']
else:
  spouse = []
  spouse = FillArrayFromUser("Spouse", spouse)
  car = []
  car = FillArrayFromUser("Car", car)
  children = []
  children = FillArrayFromUser("Number of Children", children)
  job = []
  job = FillArrayFromUser("Job", job)
  salary = []
  salary = FillArrayFromUser("Salary", salary)

DisplayBoard(spouse, car, children, job, salary)
masterBoard = CreateMasterBoard(spouse, car, children, job, salary)
masterBoard = PlayGame(masterBoard)
DisplayFinalResults(name, masterBoard)
