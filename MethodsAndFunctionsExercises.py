# Section 1 : EASY -------------------------------------------------------------------------------------------------------

# Exercise 1 : LESSER OF TWO EVENS: Write a function that returns the lesser of two given numbers if both numbers are even, 
# but returns the greater if one or both numbers are odd

def LesserOfTheTwo(num1,num2):
    if num1%2 == 0 and num2%2 == 0:
        if num1<num2:
            return num1
        else:
            return num2
    elif num1%2 !=0 and num2%2 !=0:
        if num1<num2:
            return num2
        else:
            return num1
     
# the above can be optimized to use min and max functions

def LesserOfTheTwoUsingMin(num1,num2):
    if num1%2==0 and num2%2==0:
        return min(num1,num2)
    else:
        return max(num1,num2)


# Exercise 2: ANIMAL CRACKERS: Write a function takes a two-word string and 
# returns True if both words begin with same letter
# TODO: Revisit the split and other utility functions

def AnimalCrackers(name):
    wordlist = name.split()
    if wordlist[0][0] == wordlist[1][0]:
        return True
    else:
        return False

# Exercise 3: MAKES TWENTY: Given two integers, 
# return True if the sum of the integers is 20 or if one of the integers is 20. If not, 
# return False

def MakesTwenty(num1,num2):
    if num1 == 20 or num2==20 or num1+num2 == 20:
        return True
    else:
        return False


# Section 2: LEVEL 1 --------------------------------------------------------------------------- 













print(LesserOfTheTwo(3,5))
print(LesserOfTheTwo(4,6))

print(LesserOfTheTwoUsingMin(3,5))
print(LesserOfTheTwoUsingMin(4,6))

print(MakesTwenty(20,20))
print(MakesTwenty(10,10))
print(MakesTwenty(5,10))

print(AnimalCrackers("Laughing LLama"))
print(AnimalCrackers("Happy Dog"))

print(__name__)