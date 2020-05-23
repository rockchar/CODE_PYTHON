# NESTED STATEMENTS
# now we have a fair idea of writing own functions etc. Now we will 
# discuss about nested statements and scope of variables

x = 25

def PrintSomething():
    x = 50
    return x

print(x)
print(PrintSomething())

# as we can see that the above outputs print 25 and 50
# its interesting because how does Python know which value
# of X to use. This is where the concept of scope comes in.
# the basic sequence of referencing variable value is 
# L E G B
# L = Local
# E = Enclosing Functions
# G = Global
# B = Built in
# Let us see these in the following examples

name = "this is a global name"

def Greet():
    name = "Rohit"
    #the following is a enclosing function
    def SayHello():
        print("Hello " + name)
    SayHello()

print(name)
Greet()

# wecan see that the name used in local scope was used in greet()
# Let us see another example
x = 50 #global scope

def PrintNumber(x):
    print("Value of x is ",x)
    x = 2
    print("Changing the value of x to ",x)


PrintNumber(x)
print(f"x is still {x}")

# Now let us see how we can use the num declared in a global
# scope
# If you want to assign a value to a name defined at the top 
# level of the program (i.e. not inside any kind of scope such 
# as functions or classes), then you have to tell Python that the 
# name is not local, but it is global. 
# We do this using the global statement. 
# It is impossible to assign a value to a variable defined 
# outside a function without the global statement.

num = 50

def GlobalExample():
    global num
    print("now we are usung the global value of num = ",num)
    print("changing the global valur to 2")
    num = 2

print(num)
GlobalExample()
print(num)