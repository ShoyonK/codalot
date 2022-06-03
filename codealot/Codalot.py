from Knight import Knight

class Codalot(object):
    knights = []

    def __init__(self, numKnights):
        self.knights = list()
        for i in range(numKnights):
            self.knights.append(Knight())
        
    def clearKnights(self):
        del self.knights[:]

    def getKnights(self):
        return self.knights

    def addKnightToTrainingYard(self, knight):
        self.knights.append(knight)
        knight.setInTrainingYard(True)
        knight.setInTavern(False)

    def addKnightToTavern(self, knight):
        self.knights.append(knight)
        knight.setInTavern(True)
        knight.setInTrainingYard(False)

    def process(self):
        for knight in self.knights:
            knight.incrementXp(1 if (knight.isInTrainingYard() and knight.getStamina() > 0) else 0) #must come before incrementStamina for edge case when stamina = 1 and knight is in training yard
            knight.incrementStamina(1 if knight.isInTavern() else -1)

    def grantBonusXp(self):
        bonusKnights = 0
        for knight in self.knights:
            if knight.getXp() >= 3:
                bonusKnights = bonusKnights + 1

        if bonusKnights == 3:
            for knight in self.knights:
                if knight.getXp() >= 3:
                    knight.setXp(knight.getXp() + 5)

        if bonusKnights == 5:
            for knight in self.knights:
                if knight.getXp() >= 3:
                    knight.setXp(knight.getXp() + 10)

        if bonusKnights == 6:
            for knight in self.knights:
                if knight.getXp() >= 3:
                    knight.setXp(knight.getXp() + 20)

    def calculateEarnedXp(self):
        total = 0
        for knight in self.knights:
            total += knight.getXp()
        return total
