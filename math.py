#addition 
def add(x,y):
	pass

#Subtraction
def sub(x,y):
	return x-y

#Multiplication
def mul(x,y):
	return x*y 
#Division
def div(x,y):			#On Master Branch
	if y==0:
		return DIVIDE_BY_0_ERROR
	else :
		return x/y
#Squre function
def square(x):
	return x*x