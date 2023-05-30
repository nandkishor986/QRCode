name = "SitaRam"

print(name)

name_2 = 'Govina'

print(name_2)

name_3 = '''
Have a nice 
day
'''

print(name_3)

# String Functions

# slice

s_name = "Gurgaon"

print(s_name[0])
print(s_name[1])
print(s_name[2])
print(s_name[3])
print(s_name[4])
print(s_name[5])

print(s_name[2:4]) # 2 se lekar 4 se 1 ghatakar yani 2 se 3 tak

print(s_name[2:5]) # 2 se lekar 5 se 1 ghatakar yani 2 se 4 tak

name_4 = "          Gaurdians     "

print(name_4)

print(name_4.strip()) # Trim OR Cut extra spaces


# To know length of the string - len(name_3)

print(len(name_2))

var = name.lower() # Make Lowercase

var_2 = name.upper() # Make Uppercase

print(var)
print(var_2)

name_5 = "Harry"

var_3 = name_5.replace("r","p") # Replace "r" by "p"
var_4 = name_5.replace("ar","s") # Replace "ar" by "s"

print(var_3)
print(var_4)

var_6 = "Jack, Ma, Ki, Biwi, Ka, Wah, Taj"

var_7 = var_6.replace(",", '')
var_8 = var_6.replace(",", '\n') # New Line Character - Nai Line
var_9 = var_6.replace(", ", '\n') # New Line Character - Nai Line

print(var_7)
print(var_8)
print(var_9)

# Concatenate 2 Strings

stri = "This is a "
nam_10 = "Pyari"
stri2 = "This is not a"

print(stri+stri2) # 2 Strings are Concatenated - Jud Jayegi 

print(stri + nam_10)

# To make a template like This is a harry & he is a good harry

naam_1 = "Marie"
naam_2 = "Rohan"

temp = "This is a {} and he is a good boy named {}".format(naam_1, naam_2)

# {} - placeholders {} - Focus & Practise above syntax multiple times {} - Occupies naam_1 & naam_2

print(temp) # {} - placeholders lagage baad main .format krke kar skte ho.

temp_2 = "This is a {1} & he is a good boy named {0}".format(naam_1,naam_2)

print(temp_2)

# f" "- f String - 3.6 onwards 

temp_3 = f"This is a {naam_1} & he is a {naam_2}"

print(temp_3)

# Try this Operators - ** - 




















