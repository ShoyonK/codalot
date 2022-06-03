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
    print("Passed")

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
    print("Passed")


if __name__ == '__main__':
    TestGame()
    TestTrainingYardStaminaZero()