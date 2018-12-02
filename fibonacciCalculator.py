#######################################   this program is a basic fibonacci number sequence calculator      ###########################################

#just a basic functionality test, variable declaration, test print
if 1==1:
	test = ":)"
	print(test)


"""variable declaration starts here"""
#starting values forfirst fibonacci terms; vars: X, Y, Z
varX = 0 
varY = 1
varZ = varX + varY

#swap variables for moving from one iter to next in fibonacci;vars: A, B
varA = 0
varB = 0
"""variable declaration ends here"""


"""user interface starts here"""
#introduction to what the code does
print ("this program will out put various numbers in the fibonacci sequence based on the number of iters the user desires")


#make this a function that also checks if valid input. if invalid will give error message and repeat. if good will set variable
def func_UserIn_ShowIter():
	userIn_ShowIter = input("If you would like to see all iterations calculated type, 'y' or 'yes'. If not, type 'n' or 'N' ")
	userIn_ShowIter = userIn_ShowIter.lower()

	if userIn_ShowIter in ["y", "yes"]:
		print("Showing all iterations calculated")
		return 1

	elif userIn_ShowIter in ["n", "no"]:
		print("Only showing the final iteration calculated")
		return 0

	else:
		print("Invalid input. Please try again")
		func_UserIn_ShowIter()

b_ShowIter = func_UserIn_ShowIter()

#prompt to get user input for iters(converted to integer)
userIn_Iters = int(input("how many iters do you want?"))
print("calculating for", userIn_Iters, "iters")

"""user interface ends here"""


"""the code for whether or not the iterations will be shown based on user input"""


"""The """


"""main body of the code begins here"""
#the count for how many iters the function has run
#should I start this at 1 for the while loop, or shoul I keep 0 and add one at start of while loop?
iterCount_Math = 0
#used only for the while loop that is used once
iterCount_First = 0

#need this for first iter
while iterCount_First == 0:
	#may take this out depending on starting value. need to do something so first iter isn't 0
	iterCount_Math += 1

	#prints the starting values declared at start of module. the first 3 fibonacci iter numbers; raises function iter count
	print(varX, "Iter#", iterCount_Math)

	iterCount_Math += 1
	print(varY, "Iter#", iterCount_Math)

	#could have the counter increase after the variable value changing or leave before it
	iterCount_Math += 1
	varZ = varX + varY
	print(varZ, "Iter#", iterCount_Math)

	#move the relevant variables into swap variables
	varA = varY
	varB = varZ

	#add to the counter, ending this one time use while loop 
	iterCount_First += 1


#function to be run number of times based on input from user gained start of program
#first way i structured the loop running the function(  for g in range (1, userIn_Iters):  ))
#alternate way to do this loop(  while iterCount_Math < userIn_Iters:  )
while iterCount_Math <= userIn_Iters:
#taking last two iter ends and pluging back into equation
	varX = varA
	varY = varB

	#get the answer for this iter
	varZ = varX + varY

	#prints iter value, kinda the point of the code XD
	print(varZ, "Iter#", iterCount_Math)

	#move the relevant variables into swap variables
	varA = varY
	varB = varZ

	#adds to iter counter
	iterCount_Math += 1


"""start of: code to print a gramaticly nice final value phrase"""
#print("the value of the", iterCount_Math, )

"""end of: code that makes the program print a gramaticly nice final value phrase"""


"""main body of code ends here"""


"""end output and program end begins here"""
#without the -1, the below print command is outputting a number one higher than the actual number of iters
print("the number of iters calculated were:", iterCount_Math-1)
print("done")
"""program has run and is complete"""