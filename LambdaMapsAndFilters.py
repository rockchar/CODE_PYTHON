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

# 3. LAmbda Expressions
