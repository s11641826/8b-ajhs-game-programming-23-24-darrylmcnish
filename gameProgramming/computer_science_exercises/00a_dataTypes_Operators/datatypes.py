#Data type and Operators, Darryl Mcnish, v2

#Variable Rules
#CANNOT START WITH A NUMBER
#CANNOT USE BULT- IN KEYBOARDS AS VARIABLES
#VARIABLE NAME SHOULD DESCRIBE THE DATA BEING STORED. 
#snake_case variables use _ to separate words, all lower case.
#camelcase variables do not use spaces, 1st word lower, rest up

# String Literal Examples
playerName = "jack love"
emptySring = ""
spaceString = " "
monstername = "purple people eater"

#INTERGER DATA TYPES
health = 100
extralives = 5
temperature = -17

# Floating Point Data Types
pi = 3.1415678
laptime = 3.5
velocty = -2.0

#Boolean Data Types
isfiretype = False
weaponequipped = True
pvpEnabled = False

# Architmetic Operators
# PEMDAS APPLIES JUST LIKE IN MATH CLASS!
print(3 + -1) # Addition
print(0 - 25) # Subtraction
print(1 * -1) # Multiplication
print(3 / -1)#divison
print(3 * 4)# Exponents
print(18 % 4) # Modulus

# Comparison Operators
# Evaluate the expression, then return True or False
print(5 > 3) # Greater Than
print(7 >= -1) # Greater Than or Equal to
print(-1 < -2) # Less Than
print(0 <= 0) # Less Than or Equal To
print(5 == 3) # Equal to
print(-99 != 99) # Not Equal to

# Assignment Operators
myVariable = 'myValue' # Assign variable on the left the value on the right, throw out any curren values
myotherVariable = (10 + 5)

myVariableAgain = 1
myVariableAgain = 5
print(myVariableAgain)

# Addition Assignment -- Add the value on the right, keeping any current value
myWallet = 0
myWallet += 1
myWallet += 5
print(myWallet)

# Same Effect
x = 0
x+= 1
x = x + 1

 #Logical Operators
print(3 > 5 and 4 < 3) # AND requires ALL aexpressions to be true
print(3 > 2 and 4 < 3)
print(3 > 2 and 4 != 3)
print(3 > 2 and 4 != 3 and favColor == "blue" and temp == -5)
# When writing and expressions, put the value most likely to be False first!
