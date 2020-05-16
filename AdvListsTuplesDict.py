'''
In this section we will see some advanced features of Lists e.g. List comprehension.
We will also see tuples which are just unmutable lists i.e. immutable ordered sequence 
of python objects.Once declared they cannot be changed.
We will also see Dictionaries that is an unordered collection of key value pair.
Lastly we will quickly see sets and booleans

'''

# lets first discuss dictionaries
# dictionaries are unordered collection of key value pairs. Dictionaries are similar to 
# hash tables. They dont need order as the objects are stored as key value pairs

# Lets declare a dictionary 

my_dict = { "key1":"value1" , "key2":"value2" , "key3":"value3" }
print(type(my_dict)) 
# now lets print the value associated with key1
print(my_dict["key1"])

# now lets check some inbuilt functions in dictionary
print(my_dict.keys())
print(type(my_dict.keys())) #type dict keys 

# Dictionaries are versatile. There are many types of objects they can hold as values
my_dict_list = { "key_fruits" : ["Apple","Orange","Mango"] , "key_animals" : ["Cat","Dog","Cow"] }
# now we can access the fruits and animals list with key and index position
print(type(my_dict_list["key_fruits"]))

# So we can see that the print statement prints type list.Hence we can do all the list operations
print(my_dict_list["key_fruits"][0])
print(my_dict_list["key_fruits"][1])
print(my_dict_list["key_fruits"][2])
my_dict_list["key_fruits"].append("Guava")
print(my_dict_list["key_fruits"][3])

# inbuilt methods to print all the values 
print(my_dict_list.values())

# lets create a new key via assignment 
my_dict_list["key_snacks"] = ["Chips","Chocolates","Cakes"]
print(my_dict_list.values())

# adding a new key using assignment 
print(my_dict.values())
my_dict["key4"]="value4"
print(my_dict.values())

# the values themselves can be manipulated

my_dict["key5"] = 125
print(my_dict["key5"])

my_dict["key5"]-= 121
print(my_dict["key5"])

# dictionaries can be nested 
my_nested_dictionary = {"key1":{"key2":{"key3":["Nested_value1","Nested_Value2","Nested_Value3"]}}}
print(my_nested_dictionary["key1"])
print(my_nested_dictionary["key1"]["key2"])
print(my_nested_dictionary["key1"]["key2"]["key3"])
print(my_nested_dictionary["key1"]["key2"]["key3"][2])

# let us print the keys and values 
print(my_nested_dictionary.keys())
print(my_nested_dictionary.values())