# Variables - Containers to store data
# Space in your computers memory
# Jab bhi aap koi var banate ho tab aapke memory main ek us variable ki size ka dabba/box ban jata hain aur jab hum use koi value assign karte hain tab oh value us dabbe main jake store ho jayegi

# e.g - a = 35 - "a" naam ka memory mein ek dabba ban gaya aur usme 35 value store ho gayi

a = 35 # Type - Integer.

b = "Nandkishor" # Type - String - Koi naam, koi text.

c = 40.45 # Type - floating point number - float.

d = 6

'''
print(a + c) 
print(a - d) 
print(a * d) 
print(a / d)
'''

# Variables banane ke rools 

'''
1. Should start with letter OR _underscore.
2. Cannot start with a number. 
3. It can only contain alphanumeric characters - e.g A to Z, 0 to 9, "_". 
4. Variable names are case-sensitive - Nandu & nandu are 2 different
'''

# How to find Type of variable 

typeA = type(a) # Integer - int

print(typeA)

typeB = type(b) # String - str

print(typeB)

typeC =  type(c) # floating point - float

print(typeC)

# Container Data types can be changed for e.g

a = "Sanatan"

print(a)

typeD = type(a)

print(typeD)

e = 31

print(e+5)

f = "31"

# print(f+10) - Can only concatenate 'str' + 'str' not 'int' to 'str'

print(type(e))
print(type(f))

