#--------------------
# BASIC OPERATORS
#--------------------

'''
  Welcome to arthimetic! Now we'll learn the basics of adding, subtracting, multiplying, dividing, and modulo (remainders).
  I'll be assigning the outputs to variables as well to showcase how variables hold information.
'''

# ---- Addition and Subtraction ----

# Addition uses the + symbol to add two things together.
print(1+2) # IT'S 3!!

# Subtraction uses the - symbol to subtract things from one another.
print(1-2) # IT'S -1!!

#You can do things like this with variables and operations:

x = 12
y = 10

answer = x + y # 12 + 10
answer2 = x - y # 12 - 10

print(answer, answer2)

#I did a few things here. First, I made 2 variables, x and y, and assigned the ints 12 and 10 to them. 
#Then, I made two more variables, answer and answer2, and assigned the value of the operation to them.
#Finally, I printed both values. You can use a comma to seperate print values. I'll go over more that you can do with print in the next section.

# With addition and subtraction, the data type that the result is depends on what the initial values of the operation was. For example, addition between two ints, such as the ones above, 
# will result in an int as the answer.

print(type(answer), type(answer2))

# Same for subtraction.

# A float with an int will be a float, because the decimal remains!

x = 1.2

print(x+y, type(x+y)) # Remember y is still 10

#We can also add strings together in Python. This is called "Concatenate". Most other languages don't usually allow this type of string addition.

greeting = "Hello!"
name = " My name is Dominic."

sentence = greeting + name

print(sentence)

#I added a space at the beginning of the name variable's string because if I didn't, then it would be something like "Hello!My name is Dominic."

# ---- Multiplication and Division ----

#Multiplication uses the * symbol to multiply two tings. 

print(x*y, type(x*y))

#This is a float still because it's calculating the .0 in the answer.

# Division usually ends up being a float as well, as most things simply become decimals.
