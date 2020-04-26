'''
Lists are ordered sequence of objects. Lists are mutable which means that the individual elements can be
changed inside a list.

This file demonstrates the following list operations:
1.) Creating lists
2.) Indexing and Slicing Lists
3.) Basic List Methods
4.) Nesting Lists
5.) Introduction to List Comprehensions
'''

# CREATING A LIST :
#-------------------------------------------------------------------------------------------------------------------
print("\n\nCREATING A LIST:\n")
# 1. Creating a list is simple. Just declare a list as following 
my_list = ["1","2", "3","4"]
print(my_list)
print(type(my_list))

# 2. Creating a list with initialization
my_init_list1 = [ None , None , None ] # creates  a list of three elements
print(my_init_list1)

my_init_list2 = [None] * 10 # creates a list of 10
print(my_init_list2)

my_init_list3 = [0 for i in range(100) ] # initialises a list of size 100 initialised to 0 using list comprehension
print(my_init_list3)

# Lists are mutable.Which means that any object at an index can be changed 
# lets change the 3rd object of my_list ( see top ) to an integer
my_list[2] = 3
print(my_list)

# now lets change the first element of the list to a string 
my_list[0] = "Orange"
print(my_list)

#2. INDEXING AND SLICING LISTS
#--------------------------------------------------------------------------------------------------------------------
print("\n\nINDEXING AND SLICING LISTS\n")
# List elments can be accessed using indices. Furthermore they can be sliced/grabbed etc
# let us declare a list of 10 elements. The choice of objects is yours. We will take intefers here

my_slicable_list = [1,2,3,4,5,6,7,8,9,10]
print(my_slicable_list)

# Now we will grab the 3rd element in the list. Note that the list index starts from 0 so the 3rd element is index 2
print(my_slicable_list[2])

# Now we will grab all the elements starting from 4th element till the end of the list
print(my_slicable_list[4:])

# Now we will grab all the elements starting from first element to the 5th  element
print(my_slicable_list[:5])

# now we will grab all the elements in the list skipping one element in between
print(my_slicable_list[0:11:2])

# now we will grab all the elements is the list from the second element till the end skipping one element in between
print(my_slicable_list[1:11:2])

# so we have seen that the list slicing can be done using list[<start index>:<end index>:step]
# <start index> : the index in the list which we want to grab first
# <end index >  : the index in the list till where  which we want grab
# <step>        : the step size 

# interesting fact is that the lists have a negative step too. For example if we want to traverse the list 
# backwards then we can use the negative step. Below is an example

# Traverse the list backwards element by element 
print(my_slicable_list[::-1])

# Traverse the list backwards element by element skipping one element in between
print(my_slicable_list[::-2])

#Traverse the list backwards starting from the second last element
print(my_slicable_list[:0:-1])

#Traverse the list backwards starting from the third last element till 4th last element 
print(my_slicable_list[3:0:-1])


# Lists also have a negative indexing. The last element is represented by -1
print(my_slicable_list[-1])

#Note that the list change is not permanenent and when we print the list, the list is printed in order 
print(my_slicable_list)












# #---------------------------------------------------------------------------------------------------------
# #declare list 
# my_list = [1,2,3,4,5]
# print(my_list)
# print(type(my_list))
# #different object types can be assigned to a list 
# a= 'banana'
# my_list = ['Apple',1, 3.14, a,'x']
# print(my_list)

# #------------------------------list slicing and indexing----------------------------------

# #grab the object at index 1
# print(my_list[1])
# #grab everything starting at the index 2 element till end
# print(my_list[2:])
# #entire list skipping one element
# print(my_list[::2])
# #reverse the list(not permanent)
# print(my_list[::-1])
# #using + to concatenate list (not permanent)
# print(my_list+["new item 1","new item 2"])
# #using + for reassignment (permanent)
# my_list = my_list+["Orange"]
# print(my_list)
# #using * to duplicate the list 
# print(my_list*2)


# #-----------------------------List Functions-------------------------------------------------

# my_list.append("mango") #appends an object to the list
# print(my_list)

# print(my_list.pop())    #pops the last element
# print(my_list)

# my_list.reverse()       #permanent
# print(my_list)