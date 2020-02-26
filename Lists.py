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

#declare list 
my_list = [1,2,3,4,5]
print(my_list)
print(type(my_list))
#different object types can be assigned to a list 
a= 'banana'
my_list = ['Apple',1, 3.14, a,'x']
print(my_list)

#------------------------------list slicing and indexing----------------------------------

#grab the object at index 1
print(my_list[1])
#grab everything starting at the index 2 element till end
print(my_list[2:])
#entire list skipping one element
print(my_list[::2])
#reverse the list(not permanent)
print(my_list[::-1])
#using + to concatenate list (not permanent)
print(my_list+["new item 1","new item 2"])
#using + for reassignment (permanent)
my_list = my_list+["Orange"]
print(my_list)
#using * to duplicate the list 
print(my_list*2)


#-----------------------------List Functions-------------------------------------------------

my_list.append("mango") #appends an object to the list
print(my_list)

print(my_list.pop())    #pops the last element
print(my_list)

my_list.reverse()       #permanent
print(my_list)