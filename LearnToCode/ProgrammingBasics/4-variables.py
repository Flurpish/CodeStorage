#Welcome to your first python file! You'll notice that this file ends in .py. That is the extension of the file, which means it's a python file. 
#So anytime you see a file with .py at the end, you'll know it's a python file! 

#In VSCode, you can create new files on the left. The first tab should show you a file explorer window. In this, you can press a + icon or right click and add a new file.
#Next, type the file name, something like LearningPython then type .py at the end. It should look like:

'''LearningPython.py'''

#Of course, without the '''. 
#You might be wondering why I'm using # and '''. Well, in python, # is used to comment lines of code. This means that the IDE will ignore the code after the #. 
#Other languages have different ways of comments, such as using // or ;. 

#The ''' that I used is to make a thing called a "multiline string literal" (don't worry about it), 
#but since we don't actually do anything with it, it ends up being useless! We'll talk about strings in the next section.

# -------------------
# VARIABLES AND PRINT
# -------------------

#The thing I did above is just for style! It's still a comment because of the #. 

#Anyway, it's time to write your first actual piece of code. 

#Variables in python are made to be extremely easy. By simply typing a word or letter, you can make a variable! For example:

myCoolVariable = 0

#The name of this variable is myCoolVariable. The = means that we're assigning whatever is on the right to myCoolVariable, which would be 0 in this case.

#To explain this simply, the left side, the variable, is going to be assigned as whatever the right side is. myCoolVariable equals the number 0.

#Variables are EXTREMELY important. You will always be using variables while you code so that you can save things to memory!

#Now, lets talk about the print() function. Print is very important to cover early so we can have a visual representation of what each variable is assigned as.
#Print is going to be used A LOT, typically in debugging, but all the time as a beginner. The print() function will essentially put anything inside of its parentheses into the output of the IDE.
#of the IDE.

print(myCoolVariable) 
#This will print whatever myCoolVariable is assigned as. Try this in your own IDE and press the play button on the top right. If asked, choose the first python interpreter.
#Once it runs, you'll see the value of myCoolVariable in the output section at the bottom of the IDE!

#Lets move on.

#You can change existing variables whenever you want as long as it's on the left side of a =. Lets say we want to change myCoolVariable to 6. 

myCoolVariable = 6
print(myCoolVariable)

#Congrats! This variable is now 6. 
#Notice how if you run the file now, you'll see 0 and 6 in the output. That's because it reads from top to bottom. myCoolVariable was changed to 6 after the first print, which means
#that the first print still reads myCoolVariable as 0.

#Lets make a new variable for any number you choose. 

number = 291273907
print(number)

#I named my variable "number", but you could really name it whatever you want. Just be careful, if you misspell a variable name...

''' It's still a variable! '''

#That means that:

number = 291273907
#and
nunber = 291273907

#are two completely different variables. They just happen to have the same value. Changing one variable will not affect the value of the other.

# --------------
# ASSIGNING VARIABLES TO VARIABLES
# --------------

#You can assign a variable to another variables value like this:

number = 2 # Number now equals the number 2
myValue = number 
print(myValue)

# myValue, which is a new variable, is now equal to number, which is 2. So, myValue is 2!

#Variables names are important, so try to follow a clean format, which are these options usually:

myVariable
my_Variable

#Note that you cannot do: (ignore the ''')
'''my variable'''
'''1variable'''
'''very@cool'''

#Variables can only start with a letter or _, and can contain letters, numbers, and _. They also can't be a reserved python word, such as if, while, and def. Of course, there
#are more reserved words, but you'll come to know them more later.

#As good practice, use one of the options I mentioned above. Don't start a variable with _ just yet, as we do that for specific types of things.
