class Knight(object):
    __isInTavern = False
    __isInTrainingYard = False

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

    def incrementStamina(self, stamina):
        self.__stamina += stamina

    def isInTavern(self):
        return self.__isInTavern

    def setInTavern(self, isInTavern):
        self.__isInTavern = isInTavern

    def isInTrainingYard(self):
        return self.__isInTrainingYard

    def setInTrainingYard(self, isInTrainingYard):
        self.__isInTrainingYard = isInTrainingYard

    def moveToTrainingYard(self): #toggles appropriate fields to set knight in training yard
        self.setInTrainingYard(True)
        self.setInTavern(False)

    def moveToTavern(self): #toggles appropriate fields to set knight in tavern
        self.setInTrainingYard(False)
        self.setInTavern(True)

    def toString(self):
        print("xp is '{xp}' and stamina is '{sta}'".format(xp=self.__xp, sta=self.__stamina))