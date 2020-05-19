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

my_sq_list = [x*x for x in range(0,11,1)]
print(my_sq_list)
