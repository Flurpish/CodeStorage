# How Does Code Work?

## Good ol' 0s and 1s

I'm pretty sure it's "ol'", although I could be wrong.
Anyway, machines only actually know 2 types of data: **on and off**. 

Typically, this is translated to 1 and 0. 1 would be on, while 0 would be off. Computers are basically just a giant collection of 
0s and 1s, which is why you see those super cringe hacking scenes in movies use a bunch of **binary** when it's absolutely pointless.

These on and off settings are called **switches**, or **transistors**. So, computers are made of a lot of switches. You get to learn this a lot when 
dealing with microprocessors, which is a required class at TAMUK, but I'll also touch into it eventually. For now, just know that at the
base level, it's just good ol' 0s and 1s.

This language is referred to as machine language, or **binary**. It's the lowest-level programming language, basically meaning that there's infinite possibilities
but is super hard to code in. This is like the type of torture you'd apply to war criminals. "Code my program in binary." 

Binary is grouped into groups of 8 digits, known as **bytes**. A **byte** is considered the standard way computers store data. It consists of 8 **bits**, which 
is basically one of those digits. Below is an example of a **byte**, with 8 **bits**:

> 11000110

## Programming Languages

So because it's a war crime to make someone type things out in binary and you'll likely die before anything gets finished, people managed to come up
with programming languages. This was mentioned previously, but programming languages are basically the bridge between human readable language and a machine's 
love for on-off values. These programming languages get translated into binary values for your computer to run, allowing for us to make our programs.

But of course, it's not _THAT_ simple behind the scenes. 

Us humans use tools such as **interpreters** and **compilers** to turn human-readable code into machine code. These both do similar jobs, but in their own way.

Both of these tools help translate human-readable code into machine code that the computer can understand and execute.
Some languages do this directly, while others use intermediate steps such as bytecode or virtual machines.

**Interpreters** translate and execute code as the program runs. This makes it easier to debug, or find issues, and allows the management of memory automatically. It's slower than compilers and is 
used mostly for programming and developement. 

**Compilers** translate the entire program into machine code before the program runs. Rather than go line-by-line, it does everything at once and creates an output, which is an exe file. 
This output ends up being faster in comparison to interpreted code, and can help improve application security. It can only catches specific errors. 
Compilers are used mainly in production.

Different programming languages run off of these. C, C++, and C# are all compiler-based languages, while Python and MATLAB are interpreter-based.

## Integrated Development Environment (IDE)

Writing code in a notepad is technically possible. It's a little tedious, but it can definitely get you there. A more optimized route would be to use **IDEs**, which are 
software applications that make it much easier to read and write code. Most IDEs have integrated support for at least one language, with several offering support for a wide variety.

IDE software typically have an "intelligent" feature that allows you to code faster and easier. This simply means that the IDE knows the programming language you're writing in and it knows 
it's rules. Because of this, it'll let you know when something is off and even prompt things you'll probably want while writing. In VSCode, this feature is called Intellisense. It's extremely 
helpful when writing code, as it speeds up the process of writing while also showing your mistakes in realtime. 

IDEs also help compile and interpret your code. This is awesome, because you really don't want to go out of your way to do this all yourself. It helps with debugging and testing as well! 

Next, we'll go over the IDE that I use throughout all of these tutorials. I'll also provide the links to install Python and set it up with the IDE.


