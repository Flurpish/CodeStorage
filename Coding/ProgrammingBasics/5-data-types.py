# --------------------
# DATA TYPES
# --------------------

#So we know how to make variables, how to print, and how to run python code with VSCode. Now, lets explain the different basic data types that variables can be.

#I'll also introduce a new function, only because I think it'll be important to view these data types. We'll do that soon.

#We'll go over these basic types:

'''
  strings (or str, which are sentences or characters)
  integers (or int)
  float (decimal numbers)
  boolean (or bool, which is true or false)
'''


# ---- TYPE FUNCTION ----

# The type function is going to help us see the data types of the following variables. The type function works like this:

type(5)

# This doesn't visibly do anything yet, but behind the scenes it's returning what type 5 is. We can visualize it by printing it.

print(type(5))

#This is going to be used below to allow us to see what each type is.


# ---- STRINGS ----

print("This is a string!") 
print(type("This is a string!"))

#Anything inside of '' or "" is a string. In the print function above, we print out the string "This is a string!". You can directly print things, like in this one, or use variables.

x = "this is a string" # x is now a string that says "this is a string"
print(x)
print(type(x))

print('this is also a string')
#and so is:
print('a')
print(type('a'))
#Some languages call single letter strings "characters", or char, but Python doesn't really do this.

#Strings are pretty important to coding. Most languages have String functions, which means that you can do specific things to a string. We'll go over that soon though.


# ---- INTEGERS ----

print(5)
print(type(5))
#Integers are whole numbers without decimal points.

x = 10
print(x)
print(type(x))
#x is an int. Notice how x was a string before, but now it's an int. Python allows variables to change types easily. Most other languages don't though, requiring something like:

x = int(10)
# or
'''
int x = 10
'''

#This is because in most other languages, you need to define the amount of space that the variable will use, since certain data types take up a certain amount of bits.

#oh yeah, integers can also be negative
y = -1210
print(y)
print(type(y))


# ---- FLOATS ----

print(1.2)
print(type(1.2))

#Floats are decimal point numbers. Basically, that's their whole thing.

x = -13.454
print(x)
print(type(x))

#Why is it called a float? Well, that's because the term for them is "floating point value", so they just turned it into floats for short. 

# ---- BOOLEAN ----

print(True)
print(type(True))

#Bools are either True or False. 

print(False)
print(type(False))

x = True
print(x)
print(type(x))

# -----------------
# PRACTICE
# -----------------

#As practice, make a variable called name. Assign your name to it as a string.
#Next, print out your name using the print function and check what data type your name was!

name = "Dominic"
print(name)
print(type(name))

#create another variable and name it whatever you'd like, I'll just do "temp" for temporary.
temp = 0 #set it to anything, whether it's a float, int, bool, or string.

#do this below:
temp = name

#What will be the value of temp?
