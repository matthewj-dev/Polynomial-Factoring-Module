class Holding:

    def __init__(self, varList, degree, leading, trailing, root):

        self.constants = varList
        self.degrees = degree
        self.quotients = set()
        self.first = leading
        self.last = trailing
        self.roots = []
        self.roots.extend(root)

    def getLeadingFactors(self):
        return self.leadingfactors

    def getTrailingFactor(self):
        return self.trailingfactors

    def setLeadingFactors(self, factorlist):

        self.leadingfactors = factorlist

    def setTrailingFactors(self, factorlist):

        self.trailingfactors = factorlist
