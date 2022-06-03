

class RoundTable(object):

    def __init__(self):
        self.__dict = {}

    def visitRoundTable(self,knight):
        self.addKnightToList(knight)
        self.incrementCounterOfKnight(knight)

    def addKnightToList(self,knight):
        if knight not in self.__dict:
            self.__dict[knight] = 0

    def incrementCounterOfKnight(self,knight):
        self.__dict[knight] = self.__dict[knight] + 1

    def visitedMinThreeTimes(self,knight):
        if knight in self.__dict:
            return self.__dict[knight] >= 3

    def clearDict(self):
        self.__dict = {}

    def getDict(self):
        return self.__dict
    