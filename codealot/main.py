from random import Random
from Knight import Knight
from Codalot import Codalot

if __name__ == "__main__":
    
    codalot = Codalot()

    knights = list()
    for i in range(12): #create 12 knights
        knights.append(Knight())

    random = Random(1)
    for i in range(24):
        codalot.clearKnights()
        for knight in knights:
            randomVal = random.randint(0, 1)
            if randomVal == 0:
                codalot.addKnightToTrainingYard(knight)
            elif randomVal == 1:
                codalot.addKnightToTavern(knight)
        codalot.process()
    codalot.grantBonusXp()

    totalXp = 0
    for knight in knights:
        totalXp = totalXp + knight.getXp()

    print("Total XP earned by all " + str(len(knights)) + " knights: " + str(totalXp))


