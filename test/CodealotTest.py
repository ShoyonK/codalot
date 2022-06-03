import sys,os
sys.path.insert(0,'../')
sys.path.insert(0,'../codealot')

from codealot.Codalot import Codalot

'''
this test case generates 2 knights in the tavern and 4 knights in the training yard and generates the result for 1 hour. The result should be zero 
because knights in the training yard have zero stamina
'''
def TestGame():
    codalot = Codalot(6)
    knights = codalot.getKnights()
    knights[0].moveToTavern()
    knights[1].moveToTavern()
    knights[2].moveToTrainingYard()
    knights[3].moveToTrainingYard()
    knights[4].moveToTrainingYard()
    knights[5].moveToTrainingYard()

    codalot.process() #make necessary changes to stamina/xp

    assert(codalot.calculateEarnedXp() == 0)
    print("Passed - 1 - TestGame")

'''
this test case generates 2 knights in the tavern and 4 knights in the training yard and generates the result for 1 hour. Only one knight has 1 stamina
The result should be 1 because only one knight has the stamina to train and gain xp
'''
def TestTrainingYardStaminaZero():
    codalot = Codalot(6)
    knights = codalot.getKnights()
    knights[0].moveToTavern()
    knights[1].moveToTavern()
    knights[2].moveToTrainingYard()
    knights[3].moveToTrainingYard()
    knights[4].moveToTrainingYard()
    knights[5].moveToTrainingYard()

    knights[5].incrementStamina(1)
    codalot.process() #make necessary changes to stamina/xp

    assert(codalot.calculateEarnedXp() == 1)
    print("Passed - 2 - TestTrainingYardStaminaZero")


'''
This test case generates 6 knights with three knights having 3 XP. This test checks if the bonusXP method in codalot correctly determines the bonus
to give and gives it to the correct knights
'''
def TestBonusXPMethod():
    codalot = Codalot(6)
    knights = codalot.getKnights()
    knights[0].setXp(3)
    knights[1].setXp(3)
    knights[2].setXp(3)  
    codalot.addToBonusKnightList(knights[0])  
    codalot.addToBonusKnightList(knights[1])  
    codalot.addToBonusKnightList(knights[2])  

    codalot.grantBonusXp()

    assert(codalot.calculateEarnedXp() == 24)
    assert(knights[0].getXp() == 8)
    assert(knights[1].getXp() == 8)
    assert(knights[2].getXp() == 8)


    print("Passed - 3 - TestBonusXPMethod")


'''
This test case generates 1 knight that has gone below 0 stamina throughout a day and makes sure the process method is not adding xp as per the requirement. 
The answer should be zero becaus
the knight has its flag = True
'''
def TestBelowZeroStaminaFlag():
    codalot = Codalot(1)
    knights = codalot.getKnights()
    knights[0].moveToTrainingYard()
    knights[0].setBelowZeroStaminaFlag(True)
    knights[0].setStamina(5)
    codalot.process()
    assert(knights[0].getXp() == 0)
    print("Passed - 4 - TestBelowZeroStaminaFlag")


if __name__ == '__main__':
    TestGame()
    TestTrainingYardStaminaZero()
    TestBonusXPMethod()
    TestBelowZeroStaminaFlag()