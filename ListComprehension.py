# List comprehensions are an important and integral part
# of python programming. Im addition to sequence operations
# like slicing and indexing , Python includes a more advanced 
# operation called list comprehension.

# List comprehenions allow us to build out lists using a 
# different notation. One can think of it essentially as 
# a one line "for" loop built inside brackets. Let us see a
# simple example

# Grab every letter in a string
my_list = [letter for letter in "Hello World"]
print(my_list)

# the above is the basic idea of list comprehension

# the following is a representation of the mathematical
# notation X^2 : X in {0,1,2,3,4,5,6,7,8,9,10}
#

my_sq_list = [x*x for x in range(11)]
print(my_sq_list)

# We can also add if statements within the list

my_evennum_list = [ x for x in range(11) if x%2 == 0 ]
print(my_evennum_list)

# we can do more complicated mathematics too
# for example celcius to farenheit 

my_celsius_list = [ 0, 32, 64, 127 ]
my_farenheit_list = [((9/5)*temp+32) for temp in my_celsius_list ]
print(my_farenheit_list) 

# we can also perform nested list comprehension
my_nested_list = [ x*x for x in [x*x for x in range(11)]]
print(my_nested_list)
