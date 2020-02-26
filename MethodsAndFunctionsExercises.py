# Section 1 : LEVEL 0 -------------------------------------------------------------------------------------------------------

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


# Section 2: LEVEL 1 -------------------------------------------------------------------------------- 

# Exercise 1: OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name
# Hint: grab the letters from index 0 to 2 and then from 3 to end and capitalize it!

def OLD_MCDONALD(name):
    if len(name) > 3:
        return name[:3].capitalize()+name[3:].capitalize()
    else:
        return "Name too short. Try again"

# Exercise 2: MASTER YODA: Given a sentence, return a sentence with the words reversed

def master_yoda(sentence):
    '''
    wordlist = sentence.split()
    print(wordlist)
    wordlist = wordlist[::-1]
    return " ".join(wordlist)
    '''
    return ' '.join(sentence.split()[::-1])

# Exercise 3: ALMOST THERE: Given an integer n, return True if n is within 10 of either 100 or 200
# HINT: Use Absolute Value

def almost_there(num):
    return abs(100 - num) <= 10 or abs(200 - num) <= 10 



# SECTION 3 : LEVEL 2 ----------------------------------------------------------------------------------

# Exercise 1: FIND 33:Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.

def Find_33(ints):
    for n in range(0,len(ints)-1):
        # print("n is {} num 1 is {} and num 2 is {}".format(n,ints[n],ints[n+1]))
        # if ints[n] == 3 and ints[n+1] == 3:
            #return True
        # using slicing
        if ints[n:n+2] == [3,3]:
            return True
    return False


# Exercise 2: PAPER DOLL: Given a string, return a string where for every character in the original 
# there are three characters
# TODO: Try the same using map

def paper_doll(word):
    word3 = ''
    for n in word:
        word3 +=n*3
    return word3

# Exercise 3: BLACKJACK: Given three integers between 1 and 11, if their sum is less than or equal to 21, 
# return their sum. If their sum exceeds 21 and there's an eleven, reduce the total sum by 10. 
# Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'

def blackjack(num1,num2,num3):
    # check the range of numbers
    points = sum((num1,num2,num3))
    if points <= 21:
        return points
    if points > 21 and 11 in (num1,num2,num3): #use tuples as we do not want to change the numbers
        points -=10
        # print("Points after reduction {}".format(points))
    if points > 21:
        return "BUST"
    else:
        return points


# Exercie 4: SUMMER OF '69: Return the sum of the numbers in the array, except ignore sections of numbers 
# starting with a 6 and extending to the next 9 (every 6 will be followed by at least one 9). Return 0 for 
# no numbers.

def summerof69(inputarray):
    add = True
    sum = 0
    for n in inputarray:
        if n == 6:
            add = False
        if add:
            sum+=n
        if n == 9 and not add:
            add = True
    return sum

# another way using while loops 

def summer_69(arr):
    total = 0
    add = True
    for num in arr:
        while add:
            if num != 6:
                total += num
                break
            else:
                add = False
        while not add:
            if num != 9:
                break
            else:
                add = True
                break
    return total

# Exercise 5 : SPY GAME: Write a function that takes in a list of integers and returns True 
# if it contains 007 in order 
# spy_game([1,2,4,0,0,7,5]) --> True
# spy_game([1,0,2,4,0,5,7]) --> True
# spy_game([1,7,2,0,4,5,0]) --> False
def spy_game(integerlist):
    spy_list = [0,0,7,'x']
    for n in integerlist:
        if spy_list[0] == n:
            print("popped {}".format(spy_list.pop(0)))
            if spy_list[0]=='x':
                return True
    return False


# ------------------------------------- Driver Code Below -----------------------------------------------
print("Spy Game:")
print(spy_game([1,2,4,0,0,7,5]))
print(spy_game([1,0,2,4,0,5,7]))
print(spy_game([1,7,2,0,4,5,0]))


print("Summerof69:")
print(summerof69([4, 5, 6, 7, 8, 9]))
print(summerof69([1, 3, 5]))
print(summerof69([2, 1, 6, 9, 11]))

print("Blackjack:")
print(blackjack(5,6,7))
print(blackjack(9,9,9))
print(blackjack(9,9,11))

print("Find 33:")
print(Find_33([1,2,3,3,5]))

print("Almost there:")
print(almost_there(80))

print("Paper Doll:")
print(paper_doll("hello"))

print("Master Yoda:")
print(master_yoda("Hello World"))


print("Old Mcdonalds:")
print(OLD_MCDONALD("oldmcdonalds"))
print(OLD_MCDONALD("old"))

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