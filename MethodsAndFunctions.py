# methods work on objects to provide some functionality like manipulation etc
# methods are necessarily functions built into objects.
# we have already seen the methods in list objects. Lets skip to write
# some functions

# lets see how we build out a function syntax in python
# it starts with def 

def name_of_the_function(parameters):
    ''' 
    Here is where the function's document string goes (docstring) 

    '''
    # do your stuff here 
    # return the desired result

# lets see an example. Lets write a function that reurns whether
# a number is prime or not.

def IsPrimeNumber(num):
    '''
    This function evaluates if a number is prime or not. Returns 
    boolean True or False based on the result.
    '''
    if num == 1:
        print("1 is neither prime nor composite")
        return False
    else:
        a = int(num/2)
        for n in range(2,a,1):
            if num%n == 0:
                print("Number is not prime")
                return False
        print("Number is Prime")
        return True


def AddTwoNumbers(a,b):
    '''
    This function adds two numbers and returns the result
    '''
    return a+b

# A note about __name__ == "__main__": a special variable in python

if __name__ == "__main__": 
    print("Executed when invoked directly")
    print(AddTwoNumbers(3,4))
    print(IsPrimeNumber(2))
    print(IsPrimeNumber(10))
else: 
    print("Executed when imported")