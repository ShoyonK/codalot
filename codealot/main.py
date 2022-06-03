from random import Random
from Knight import Knight
from Codalot import Codalot

if __name__ == "__main__":
    
    numberOfDays = int(input('How many days to simulate? '))
    numberOfHours = numberOfDays*24
    codalot = Codalot(12) #generate Codalot with 12 knights inside
    knights = codalot.getKnights()
    random = Random(1)

    hour = 0
    while(hour < numberOfHours): #iterate through the number of hours inputted with 1 hour increments
        for knight in knights:
            randomVal = random.randint(0, 2)
            if randomVal == 0:
                knight.moveToTrainingYard()
            elif randomVal == 1:
                knight.moveToTavern()
            elif randomVal == 2:
                knight.moveToRoundTable(codalot.getRoundTable())
            if hour % 24 == 0: #every 24 hours belowZeroStaminaFlag
                knight.setBelowZeroStaminaFlag(False)
        if hour % 24 == 0: #every 24 hours clear the bonusKnights in the list and the signin sheet (dict) at the round table
            codalot.clearBonusKnights()
            codalot.getRoundTable().clearDict() 
        codalot.process() #make necessary changes to stamina and xp
        hour = hour + 1

            

    codalot.grantBonusXp()
    totalXp = codalot.calculateEarnedXp()

    print("Total XP earned by " + str(len(knights)-1) + " knights: " + str(totalXp)) #subtract 1 from length for king arthur
    kingArthur = codalot.getKingArthur()
    print("Xp earned by King Arthur: '{xp}'".format(xp=kingArthur.getXp()))


