from number import Number
import random
import time
import sys

j = ''
while j != 'q':
    j = input("type q to quit or enter to continue:")
    if j is 'q':
        break

    i = 1
    while i == 1:

        choice = input("Would you like to see an example?(Y/n):")

        if choice == 'y' or choice == 'Y':
            print("") # example:
            i = 0
        elif choice == 'n' or choice == 'N':
            i = 0
        else:
            print("Invalid Choice") # error

    i = 1
    while i == 1:

        choice = input("Would you like to input your own polynomial?(Y/n):")

        if choice == 'y' or choice == 'Y':
            varList = []
            polynomialLen = int(input("What power of polynomial do you wish to factor? "))
            mynum = 0
            othernum = 0
            for w in range(0, (polynomialLen+1)):
                print("Please enter a value for variable #", (w + 1))
                if w == 0:
                    mynum = (int(input("Variable:")))
                    varList.append(mynum)
                #varList.append(int(input("Variable")))
                elif w < polynomialLen:
                    varList.append(int(input("Variable:")))
                elif w == (polynomialLen):
                    othernum = (int(input("Variable:")))
                    varList.append(othernum)

            '''initialises a quotient set to be used later'''
            quotientList = []
            quotientSet = set()
            seconds = time.time()

            #mynum =#9445128
            num1 = Number(abs(mynum))
            #num1.displayFactors()

            #othernum =10#35000#9445128 #1831923
            num2 = Number(abs(othernum))
            #num2.displayFactors()

            '''The lines of code below goes through the factor list of both numbers and
            divides the second number(probably will change to be accurate) divided over
            the first number(also likely to change) but does allow for duplicates

            selfnote: if I remember synthetic division well enough it can be used for
            factors on the polynomial and may not need to be reset and factors done again
            on the new polynomial'''
            for p in range (len(num1.factorlist)):#this 2 factors of 5
                tempnum = num1.factorlist.pop()
                for q in range (len(num2.factorlist)):#this is 4 factors of 10
                    termnum = num2.factorlist.pop()

                    quotientSet.add(termnum / tempnum)
                    quotientList.append(termnum / tempnum)
                    quotientSet.add(-1 *(termnum / tempnum))
                    quotientList.append(-1 *(termnum / tempnum))

                    num2.factorlist.insert(0, termnum)


            count = 0
            tempval = 0
            result = []
            for j in range(count, len(quotientList)):
                for i in range(0, len(varList)):
                    tempval = tempval + varList[i]
                    tempval = tempval * quotientList[count]


                if tempval == 0:
                     result.append(quotientList[count])
                tempval = 0
                count += 1

            #print(quotientList)
            print(quotientSet)
            for w in range(0, len(result)):
                if result[w] == abs(result[w]):
                    print('x - ', result[w])
                else:
                    print('x + ', abs(result[w]))

                #print(result)


            #print((time.time() - seconds))

            '''from here set up for synthetic division on passed in polynomial so reading
            in polynomial is next step and making those the numbers set to the numbers
            are getting factors found'''
        elif choice == 'n' or choice == 'N':
            i = 0
        else:
            print("") # error