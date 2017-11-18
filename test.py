from number import Number
from example import Example
import random
import time
import sys

# Matthew Jackson
# Grayson Ingram
# Passiah White
# Matthew Warren
# Terry Lewis
#
# Project Source Code PFM
# CS 420 TR 12:30 - 1:45

# The program will continue running until user specifies otherwise. First the user will be asked if they want an example or the ability to input their own polynomial.
# If the user specifies the example choice, the program will print it to the screen on a step by step basis.
# If the user specifies the custom input example the program will request their input and will give a detailed response.

j = input("type q to quit or enter to continue:")   # if user wants to leave program by typing q then break away from the loop

while j != 'q':

    i = 1
    while i == 1:

        choice = input("Would you like to see an example?(Y/n):")   # ask the user if they need to see an example

        if choice == 'y' or choice == 'Y':  # if yes then print example
            Example() # example: http://www.sparknotes.com/math/algebra2/polynomials/section4.rhtml
            i = 0
        elif choice == 'n' or choice == 'N':    # if no then break from loop
            i = 0
        else:
            print("Invalid Choice") # error

    i = 1
    while i == 1:

        choice = input("Would you like to input your own polynomial?(Y/n):")    # ask user if they would like to input a custom polynomial

        if choice == 'y' or choice == 'Y':

            # Input requests will first ask for the degree of the polynomial. Then the console will ask for each succeeding coefficient

            polynomialLen = int(input("What power of polynomial do you wish to factor? "))  # ask for the degree
            varList = []
            mynum = 0
            othernum = 0

            # ask for each coefficient
            for w in range(0, (polynomialLen+1)):
                print("Please enter a value for variable #", (w + 1))
                if w == 0:
                    mynum = (int(input("Variable:")))   # ask for leading coefficient
                    varList.append(mynum)
                # varList.append(int(input("Variable")))
                elif w < polynomialLen:
                    varList.append(int(input("Variable:"))) # middle coefficients
                elif w == (polynomialLen):
                    othernum = (int(input("Variable:")))    # ask for trailing coefficients
                    varList.append(othernum)

            # initialises a quotient set to be used later
            quotientList = []
            quotientSet = set()
            seconds = time.time()   # start timer for early testing

            num1 = Number(abs(mynum)) # get the factor list q for the leading coefficient
            print("The factor list q for the leading coefficient is:", num1)

            num2 = Number(abs(othernum)) # get the factor list p for the trailing coefficient
            print("The factor list p for the trailing coefficient is:", num2)

            # The lines of code below goes through the factor list of both numbers and
            # divides the second number over the first number: +-p/q

            for p in range (len(num1.factorlist)):
                tempnum = num1.factorlist.pop()
                for q in range (len(num2.factorlist)):
                    termnum = num2.factorlist.pop()

                    quotientSet.add(termnum / tempnum)
                    quotientList.append(termnum / tempnum)
                    quotientSet.add(-1 *(termnum / tempnum))
                    quotientList.append(-1 *(termnum / tempnum))

                    num2.factorlist.insert(0, termnum)

            print("The list of possible zeroes is (p/q): ", quotientSet)


            # This is the synthetic division function. This takes all of the quotient set and divides each element into the polynomial using synthetic division
            count = 0
            tempval = 0
            result = []
            for j in range(count, len(quotientList)):
                for i in range(0, len(varList)):
                    tempval = tempval + varList[i]  # bring down the top term or after the first iteration add the top and bottom terms
                    tempval = tempval * quotientList[count] # multiply the resulting polynomial with the element from a specific iteration through the quotientSet

                if tempval == 0:
                     result.append(quotientList[count]) # add a root when the remainder is 0
                tempval = 0
                count += 1

            print("Below are the roots for the polynomial:")
            for w in range(0, len(result)):
                if result[w] == abs(result[w]):
                    print('x - ', result[w])
                else:
                    print('x + ', abs(result[w]))

        elif choice == 'n' or choice == 'N':
            i = 0
        else:
            print("Invalid Input") # error

    j = input("type q to quit or enter to continue:")   # if user wants to leave program by typing q then break away from the loop
