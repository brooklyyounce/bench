def getListPrice():
  return getNumbers("\n\n-------------------------------------\n\nPlease enter the list price: ")
  
def getNumberOfPromos():
  return getNumbers("\n\nPlease enter the number of promotions: ")
  
def getNumbers(message):
  tryAgain = True
  while(tryAgain):
    number = input(message)
    number = number.replace("$", "")
    number = number.replace("%", "")
    number = number.replace(" ", "")
    number = number.replace(",", "")
    try:
      float(number)
      tryAgain = False
      number = abs(float(number))
    except ValueError:
      print ("Must enter a number. Try again.")
  return round(number, 2)
  
listPrice = getListPrice()
print (listPrice)

numPromos = getNumberOfPromos()
promoArray = []

for x in range(int(numPromos)):
  promoArray.append(getNumbers("\n\nPlease enter discount " + str(x + 1) + ": ")/100)
  
nextPrice = listPrice

for x in range(int(numPromos)):
  print ("\n\nDiscount " + str(x+1) + ")  (1 - " + str(round(promoArray[x], 2)) + ") * " + str(round(nextPrice, 2)) + " = ")
  nextPrice = (1 - promoArray[x]) * nextPrice
  print ("                                         "+str(round(nextPrice, 2)))
  
  
print ("\n\n**The discounted price is: $" + str(round(nextPrice, 2)) + "\n\n-------------------------------------------\n\n")