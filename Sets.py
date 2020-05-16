# sets are unordered collections of unique objects. They contain only one 
# unique object

# Lets create a set 
my_set = set()
my_set.add(1)
my_set.add(2)
my_set.add(3)

print(my_set)

# lets try to add a duplicate element to the set
my_set.add(3)

print(my_set)

#lets declare a list with duplicate objects 

my_list = [1,2,2,3,3,4,4,4,4,4,5]
print(my_list)

#now lets convert it to a set

my_set_frm_list = set(my_list)
print(my_set_frm_list)

#in the above example we can see that the duplicate objects were eliminated

# the following will fail as sets are unordered 
print(my_set_frm_list[4])