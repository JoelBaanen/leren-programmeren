from RobotArm import RobotArm

robotArm = RobotArm('exercise 12')

# Jouw python instructies zet je vanaf hier:
i = 9
for x in range(9):
    robotArm.grab()
    if robotArm.scan() == "red":
        for a in range(i):
            robotArm.moveRight()
        robotArm.drop()
        i -= 1
        for a in range(i):
            robotArm.moveLeft()
    else:
        robotArm.drop()
        robotArm.moveRight()
        i -= 1
    
    


# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()