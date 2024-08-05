#First get the random library cus we need it 
import random

#Get all the inputs from the user because we need it to function
#Get name from the user because we need it to function
print("input you name\n")
name = str(input())
#Get age from the user because we need it to function
print("input your age\n")
age = int(input())
#Get password inputs from the user because we need it to function
print("choose your password (type anything) \n")
password = str(input())
#Get guess number inputs from the user because we need it to function
print("input a number to see if you are gay \n")
numberGuess = int(input())

#Function for picked number. We are also directing the function to the number variable
def PickedNumber(numberGuess):
 #if and else statement to make sure the function has a function when it gets the number
 if numberGuess > 5 :
  print (" Looks like you picked a number hugher than 5 ")
  print ((name) , "You must thinking really high . At " , (age) , "you are going for high numbers" )

 else :
  print ("Looks like you like playing it cool with low numbers")
#First function finished for the guessed number
  
#Computer should now random pick a number but in a function for neat code and return a number so the computer dont keep it in its mind
def RandomGuess():
 return random.randrange(1, 10)

#Show us results of first function 
PickedNumber(numberGuess)

#Telling the computer to save its chosen number in a new variable and giving it conditions
ComputerGuess = RandomGuess()
if ComputerGuess > 5 :
  print (" According to the computers guess ..Looks like we going for the big one")
  print ((name) , "You must really like high numbers . At " , (age) , "you are going higher" )

else :
  print (" According to the computers guess  .Looks like you like playing it safe")
#Done , now throw the output but calling function
RandomGuess()




