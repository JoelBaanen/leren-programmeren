from RobotArm import RobotArm
# Let op: hier start het anders voor een random level:
robotArm = RobotArm()
robotArm.randomLevel(1,7)
# Jouw python instructies zet je vanaf hier:
i = 0
work = True
while work:
    i += 1
    if robotArm.grab() == False:
        work = False
    if work == True:
        for x in range(i):
            robotArm.moveRight()
        robotArm.drop()
        for x in range(i):
            robotArm.moveLeft()
     
# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()