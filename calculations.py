from functools import reduce
class Calculations:

#what makes a number factors
    # other = 0
    #factorlist =[1]

    def __init__(self, number):
        self.number = number
        self.factorlist = [1]
        self.half = number // 2
        self.factorlist = sorted(reduce(list.__add__, ([i, number//i] for i in range(1, int(number**0.5) + 1) if number % i == 0)))

    def displayFactors(self):
        print(self.factorlist)
        print(len(self.factorlist))

    def appendList(self, otter):
        self.factorlist.append(otter)

    def synthetic_div(self, step, polynomial, factor_list):

        count = 0
        tempval = 0
        result = []

        for j in range(count, len(factor_list)):

            for i in range(0, len(polynomial)):
                tempval = tempval + polynomial[i]
                tempval = tempval * factor_list[count]

            if tempval == 0:
                step.roots.append(factor_list[j])
                result.append(factor_list[count])

            tempval = 0
            count += 1
        return result

    def quadraticFormula(self, smallPoly, polynomial, factor_list):
        print(polynomial[0], polynomial[1], polynomial[2])

        smallPoly.roots.append(int(-(polynomial[1]) + ((polynomial[1]**2) - 4*polynomial[0]*polynomial[2])**0.5)/(2*polynomial[0]))
        smallPoly.roots.append(int(-(polynomial[1]) - ((polynomial[1]**2) - 4*polynomial[0]*polynomial[2])**0.5)/(2*polynomial[0]))
