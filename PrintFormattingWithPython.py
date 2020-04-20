'''
What is print formatting ?
Print formatting lets you inject items into a string rather than chain items together
using commas or string concatenation. The following example shows that:
Formatting is more elegant,easier and efficient.
'''
player = "Rohit"
runs   =  50

mystr = "Last match player "+player+" scored "+str(runs)+ " runs."          #concatenation
print(mystr)

myformattedStr = 'Last match player {} scores {} runs '.format(player,runs) #formatting
print(myformattedStr)

'''
String formatting has evolved with time 
    1. Initially the formatting was done using the placeholder method or using %(modulo) operator.
       This is the oldest technique.
    2. Then a better method of using parentheisis came {} and .format() method. This was an improved
       Technique.
    3. The latest way to format is the f strings available from python 3.6(introduced in python 3.6).
       This latest way of formatting uses formatted string literals called f-strings.
'''
# Formatting using the placeholders

placeholderstr = "This is an example where we use %s for formatting"%('placeholder') 
print(placeholderstr)

#multiple string placeholders
multiplaceholderstr = "This is where we %s the use of %s string %s"%("demonstrate","multiple","placeholders")
print(multiplaceholderstr)

# %s in the above example denotes string we can use %d for integers and %f for float values
stringfloatanddecimal = "This is an example of float %f and integer %d"%(3.1416,3)
print(stringfloatanddecimal)

stringfloatanddecimal = "This is an example of float %f and float rounded off %d"%(3.1416,3.1416)
print(stringfloatanddecimal)

#the following shows the float precision %x.y. If x is more than the number of digits before the decimal point
#then they are padded with space. If y is more than the number of digits after the decimal points then they are
#appended with zeroes
stringfloatprecision = "This is an example of float precision %5.5f"%(3.1416)
print(stringfloatprecision)

stringfloatprecision = "This is an example of float precision with appended space and zeros %150.50f"%(3.1416)
print(stringfloatprecision)

# Formatting strings using the format method
formatMethodString = "The {} {} {} jumps over the lazy dogs!".format("quick","brown","fox")
print(formatMethodString)

#indexing : inserted objects can be called by index positions
formatMethodStringIndex = "The {2} {1} {0} jumps over the lazy dogs!".format("quick","brown","fox")
print(formatMethodStringIndex)

#assigning variables to the index . The inserted objects can be assigned keywords.
formatmethodvarindex = "The quick brown fox {a} {b} {c} jumps over the lazy dogs!".format(a="Quick",b="brown",c="fox")
print(formatmethodvarindex)

#the assigned keywords can be reused and interchanged thus promoting reuse 
formatmethodvarindex = "The quick brown fox {b} {c} {a} jumps over the lazy dogs ... swift  {b} {c}!".format(a="Quick",b="brown",c="fox")
print(formatmethodvarindex)

#Alignement padding and precision with .format() format method
stringprecision = "This is an example of a float precision using format method float = {0:2.15f}".format(333.1416)
print(stringprecision)

#Alignment, padding and precision with .format()
# using the curly braces we can specify the width, alignment and precision or rounding parameters
