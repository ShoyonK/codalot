from random import Random
from Knight import Knight
from Codalot import Codalot

if __name__ == "__main__":
    
    codalot = Codalot(12) #generate Codalot with 12 knights inside
    knights = codalot.getKnights()

    random = Random(1)

    hour = 0
    while(hour < 24): #iterate through 24 hours with 1 hour increment
        for knight in knights:
            randomVal = random.randint(0, 1)
            if randomVal == 0:
                knight.moveToTrainingYard()
            elif randomVal == 1:
                knight.moveToTavern()
        codalot.process() #make necessary changes to stamina and xp
        hour = hour + 1
        
    codalot.grantBonusXp()
    totalXp = codalot.calculateEarnedXp()

    print("Total XP earned by all " + str(len(knights)) + " knights: " + str(totalXp))


