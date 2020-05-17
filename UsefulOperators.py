#######################################################################
# this file has some useful operators that python provides
# the operators we will discuss are 
# 1. range
# 2. enumerate
# 3. zip
# 4. in operator
# 5. min and max
# 6. random
# 7. input
#######################################################################

# 1. Range
# The range function is very helpful in generating a list of integers 
# It takes three parameters start,stop and step size. Lets see some 
# examples

print(list(range(0,11,1)))

# print with a step size of 2, i.e. skip one elements in between

print(list(range(0,11,2)))


# 2. Enumerate
# Enumerate is a handy function which can be used with for loops
# For example imagine a situation as follows

index_count = 0 

for letters in "India is my country":
    print(f"At index {index_count} the letter is {letters}")
    index_count+=1

# in the world of python it is so common to keep a track of the loops
# you have gone through that the operator enumerate was created so that
# the programmer does not have to maintain a variable like index_count
# Hence the above code becomes
print("\n Using enumerate \n")

for i,letters in enumerate("India is my country"):
    print(f"At Index {i} the letter is {letters}" )


# 3. Zip
# As we dive deeper into python, we will realise that tuple packing is 
# a very common data structure specially when using outside libraries

print( list(enumerate("India is my country")))

# we can see that the output is a list of tuples. Hence in the for loop
# we can use tuple unpacking. Zip is a utility that does the same for us
# it packs two lists as tuples 

list1 = [1,2,3,4]
list2 = ['a','b','c','d']
ziplist= list(zip(list1,list2))
print(ziplist)
print(list(zip(list1,list2)))

# now to use the generator, we can just use a for loop
for item1,item2 in list(zip(list1,list2)):
    print(f"item {item1} in list2 is {item2}")

# this will come in handy in many cases 