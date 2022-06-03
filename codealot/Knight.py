

class Knight(object):
    __isInTavern = False
    __isInTrainingYard = False
    __isAtRoundTable = False #not scalable, refactor later
    __belowZeroStamina = False

    def __init__(self):
        self.__xp = 0
        self.__stamina = 0

    def getXp(self):
        return self.__xp

    def setXp(self, xp):
        self.__xp = xp

    #add inputted xp to the current xp
    def incrementXp(self, xp): 
        self.__xp += xp

    def getStamina(self):
        return self.__stamina

    def setStamina(self, stamina):
        self.__stamina = stamina

    def incrementStamina(self, stamina): #use when incrementing by the hour
        self.__stamina += stamina

    def isInTavern(self):
        return self.__isInTavern

    def setInTavern(self, isInTavern):
        self.__isInTavern = isInTavern

    def isInTrainingYard(self):
        return self.__isInTrainingYard

    def setInTrainingYard(self, isInTrainingYard):
        self.__isInTrainingYard = isInTrainingYard
    
    def setInRoundTable(self, isInRoundTable):
        self.__isAtRoundTable = isInRoundTable

    def moveToTrainingYard(self): #toggles appropriate fields to set knight in training yard
        self.setInTrainingYard(True)
        self.setInTavern(False)
        self.setInRoundTable(False)

    def moveToTavern(self): #toggles appropriate fields to set knight in tavern
        self.setInTrainingYard(False)
        self.setInTavern(True)
        self.setInRoundTable(False)

    def moveToRoundTable(self, roundTable):
        self.setInTrainingYard(False)
        self.setInTavern(False)
        self.setInRoundTable(True)
        roundTable.visitRoundTable(self)

    def getBelowZeroStaminaFlag(self):
        return self.__belowZeroStamina
    
    def setBelowZeroStaminaFlag(self, belowZero):
        self.__belowZeroStamina = belowZero


    def toString(self):
        print("xp is '{xp}' and stamina is '{sta}'".format(xp=self.__xp, sta=self.__stamina))