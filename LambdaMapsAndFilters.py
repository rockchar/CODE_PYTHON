# now we will learn about maps and filters quickly

# 1. Map Function
# the map function allows you to "map" a function to an
# iterable object
# This allows us to call the same function quickly for 
# every iterable object
# for example 

def Square(num):
    return num**2

my_list = [1,2,3,4,5,6,7,8,9,10]

map(Square,my_list)

print(list(map(Square,my_list)))

# The functions can be more complex than that

def Splicer(mystring):
    if len(mystring) % 2 == 0:
        return 'even'
    else:
        return mystring[0]

my_names=["John","Cindy","Sarah","Kelly","Mike"]
print(list(map(Splicer,my_names)))

# 2. Filter Function
# The filter function returns an iterator yielding those items 
# of iterable for which function(item) is true. This means a function
# that returns a true or a false then passing that into the 
# filter alsong with the iterable and you will get back the 
# results that return only true when passed to that function
# for exampe

def check_even(num):
    if num %2 == 0:
        return True
    else:
        return False


my_filter_List=[1,2,3,4,5,6,7,8,9,10]
print(list(filter(check_even,my_filter_List)))

# 3. LAmbda Expressions : Lambda expressions or anonymous functions are 
# used extensively in python. They allow us to declare a one time function
# without a name. This means we can create an adhoc function without needing
# to define a function using def.
# Function objects returned by lambda expressions match exactly as returned 
# by functions defined using def.
# Some differences between functions defined by def and lambda expression is 
# that lambda expressions body are a single statements as compared to a block 
# of statements defined in a function.
# the generally do what we expect the return from a defined function does.

# Let us see an example by breaking down a function

def Square_ver1(num):
    result = num**2
    return result


print(Square_ver1(10)) #prints the square 

# now we will simplify the above function

def Square_sim(num):
    return num**2

print(Square_sim(10)) #prints the square 

# we can actually write the function in a simple line

def Square_line(num): return num**2
print(Square_line(10)) # prints the square

# this def Square_line(num): return num**2 is the form that the 
# lambda expression intends to replicate. Hence a lambda expression
# can be written as

lambda num : num**2

# although the lambda functions are anonymous, we are just assigning 
# a name so that we can demonstrate the function

square_lambda = lambda num : num ** 2
print(square_lambda(10))

# so where do we use lambda and why use it at all ?
# As seen in the examples of map and filter we very often need to pass 
# a method to iterables. Now most of these methods are one time use.
# this helps us in passing an adhoc anonymous function rather than 
# declaring a full multi statement def 

print(list(map(lambda num : num **2 ,my_list)))

# let us define some random lambda expressions

# lambda expression to grab the first letter of the string

lambda letter : letter[0]
print(list(map(lambda letter : letter[0],my_names)))

# lambda expression to reverse the string
lambda my_str : my_str[::-1]
print(list(map(lambda my_str : my_str[::-1],my_names)))

# lambda expression to get the first three characters of the string
lambda my_str : my_str[0:3]
print(list(map(lambda my_str : my_str[0:3],my_names)))

# lambda expression to get the first three characters of the string
lambda my_str : my_str[-3::]
print(list(map(lambda my_str : my_str[-3::],my_names)))