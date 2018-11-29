#######################################     this program is a basic fibonacci number sequence calculator           ###########################################

#just a basic functionality test, variable declaration, test print
if 1==1:
	test = ":)"
	print(test)


"""variable declaration starts here"""
#starting values forfirst fibonacci terms; vars: X, Y, Z
varX = 0 
varY = 1
varZ = varX + varY

#swap variables for moving from one iteration to next in fibonacci;vars: A, B
varA = 0
varB = 0
"""variable declaration ends here"""


"""user interface starts here"""
#introduction to what the code does
print ("this program will out put various numbers in the fibonacci sequence based on the number of iterations the user desires")

#prompt to get user input for iterations(converted to integer)
userInput = int(input('how many iterations do you want?'))
print("calculating for", userInput, "iterations")
"""user interface ends here"""


"""main body of the code begins here"""
#the count for how many iterations the function has run
#should I start this at 1 for the while loop, or shoul I keep 0 and add one at start of while loop?
mathIterationCount = 0
#used only for the while loop that is used once
firstIterationCount = 0

#need this for first iteration
while firstIterationCount == 0:
	#may take this out depending on starting value. need to do something so first iteration isn't 0
	mathIterationCount += 1

	#prints the starting values declared at start of module. the first 3 fibonacci iteration numbers; raises function iteration count
	print(varX, "Iter#", mathIterationCount)

	mathIterationCount += 1
	print(varY, "Iter#", mathIterationCount)

	#could have the counter increase after the variable value changing or leave before it
	mathIterationCount += 1
	varZ = varX + varY
	print(varZ, "Iter#", mathIterationCount)

	#move the relevant variables into swap variables
	varA = varY
	varB = varZ

	#add to the counter, ending this one time use while loop 
	firstIterationCount += 1


#function to be run number of times based on input from user gained start of program
#first way i structured the loop running the function(  for g in range (1, userInput):  ))
#alternate way to do this loop(  while mathIterationCount < userInput:  )
while mathIterationCount <= userInput:
#taking last two iteration ends and pluging back into equation
	varX = varA
	varY = varB

	#get the answer for this iteration
	varZ = varX + varY

	#prints iteration value, kinda the point of the code XD
	print(varZ, "Iter#", mathIterationCount)

	#move the relevant variables into swap variables
	varA = varY
	varB = varZ

	#adds to iteration counter
	mathIterationCount += 1


"""start of: code to print a gramaticly nice final value phrase"""
#print("the value of the", mathIterationCount, )

"""end of: code that makes the program print a gramaticly nice final value phrase"""


"""main body of code ends here"""


"""end output and program end begins here"""
#without the -1, the below print command is outputting a number one higher than the actual number of iterations
print("the number of iterations calculated were:", mathIterationCount-1)
print("done")
"""program has run and is complete"""
