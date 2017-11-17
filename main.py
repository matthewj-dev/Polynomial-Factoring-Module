from calculations import Calculations
from holding import Holding
import random
import time
import sys

varList = []

polynomialLen = int(input("What degree is your polynomial? "))
mynum = 0
othernum = 0

# print("Please say which options you would like to take:")
# input("(a, b, c) = (Example, )")


for w in range(0, (polynomialLen+1)):
    print("Please enter a value for constant #", (w + 1))
    if w == 0:
        mynum = (int(input("Constant:")))
        varList.append(mynum)
    #varList.append(int(input("Variable")))
    elif w < polynomialLen:
        varList.append(int(input("Constant:")))
    elif w == (polynomialLen):

        othernum = (int(input("Constant:")))

        if othernum == 0:
            print("Trailing integer needs to be non-zero")
            othernum = (int(input("Constant:")))
        varList.append(othernum)
    # print("Please enter a value for the power value of variable #", (w+1))

    #powerList.append(int(input("Power:")))

firstPoly = Holding(varList, polynomialLen, mynum, othernum)

print("Here are the constants ", firstPoly.constants)

seconds = time.time()

calc = Calculations(abs(firstPoly.first))
# print(calc.factorlist)
firstPoly.setLeadingFactors(calc.factorlist)
print("leading factors ",firstPoly.leadingfactors)

#othernum =10#35000#9445128 #1831923
calc = Calculations(abs(firstPoly.last))
firstPoly.setTrailingFactors(calc.factorlist)
print("trailing factors ", firstPoly.trailingfactors)

# list1len = len(firstPoly.leadingfactors)
# list2len = len(firstPoly.trailingfactors)
'''The lines of code below goes through the factor list of both numbers and
divides the second number(probably will change to be accurate) divided over
the first number(also likely to change) but does allow for duplicates
selfnote: if I remember synthetic division well enough it can be used for
factors on the polynomial and may not need to be reset and factors done again
on the new polynomial'''
for p in range (len(firstPoly.getLeadingFactors())):#this 2 factors of 5
    tempnum = firstPoly.leadingfactors.pop()
    for q in range (len(firstPoly.getTrailingFactor())):#this is 4 factors of 10
        termnum = firstPoly.trailingfactors.pop()

        firstPoly.quotients.add(termnum / tempnum)
        firstPoly.quotients.add(-1 *(termnum / tempnum))

        firstPoly.trailingfactors.insert(0, termnum)


print("quotients ",firstPoly.quotients)
# print((time.time() - seconds))

'''from here set up for synthetic division on passed in polynomial so reading
in polynomial is next step and making those the numbers set to the numbers
are getting factors found'''

polys = [firstPoly]

for j in range(0, polynomialLen):
    if (polynomialLen) > 2:
        poly = polys.pop()
        constants = list(poly.constants)
        factors = list(poly.quotients)
        result = calc.synthetic_div(poly, constants, factors)
        polys.append(Holding(result, (poly.degrees - 1), result[0], result[(len(result)-1)]))

smallPoly = polys.pop()
calc.quadraticFormula(smallPoly, smallPoly.constants, smallPoly.quotients)
print(smallPoly.roots)
