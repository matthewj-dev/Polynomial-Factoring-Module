class Holding:

    def __init__(self, varList, degree, leading, trailing):

        self.constants = varList
        self.degrees = degree
        self.quotients = set()
        self.first = leading
        self.last = trailing

    def getLeadingFactors(self):
        return self.leadingfactors

    def getTrailingFactor(self):
        return self.trailingfactors

    def setLeadingFactors(self, factorlist):

        self.leadingfactors = factorlist

    def setTrailingFactors(self, factorlist):

        self.trailingfactors = factorlist
