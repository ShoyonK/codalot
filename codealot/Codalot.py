from Knight import Knight
from KingArthur import KingArthur

class Codalot(object):
    knights = []
    bonusKnights = []
    kingArthur = None

    def __init__(self, numKnights):
        self.knights = list()
        self.kingArthur = KingArthur()
        self.knights.append(self.kingArthur)

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
            incrementXpChecker = (knight.isInTrainingYard() and knight.getStamina() > 0 and knight.getBelowZeroStaminaFlag() == False)
            knight.incrementXp(1 if (incrementXpChecker) else 0) #must come before incrementStamina for edge case when stamina = 1 and knight is in training yard
            knight.incrementStamina(1 if knight.isInTavern() else -1)

            if knight.getXp() >= 3: #if the knight has a positive net of 3 or more xp in 24 hours and is currently not in the bonusKnight list, then add it
                if knight not in self.bonusKnights:
                    self.bonusKnights.append(knight)

    #This method will determine the number of knights that qualify for bonus exp and 
    def grantBonusXp(self):
        numBonusKnights = len(self.bonusKnights)
        bonusXp = 0
        if numBonusKnights == 3:
            bonusXp = 5
        elif numBonusKnights == 5:
            bonusXp = 10
        elif numBonusKnights == 6:
            bonusXp = 20

        for knight in self.bonusKnights:
            knight.incrementXp(bonusXp)

    def calculateEarnedXp(self):
        total = 0
        for knight in self.knights:
            if isinstance(knight,type(Knight())): #only include instances of knights in the calculation to exclude King Arthur
                total += knight.getXp()
        return total

    def addToBonusKnightList(self, knight):
        self.bonusKnights.append(knight)

    def clearBonusKnights(self):
        del self.bonusKnights[:]

    def getKingArthur(self):
        return self.kingArthur;
