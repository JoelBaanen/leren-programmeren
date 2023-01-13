from RobotArm import RobotArm

robotArm = RobotArm('exercise 6')

# Jouw python instructies zet je vanaf hier:
robotArm.moveRight()
i = 3
for x in range(i):
    if i > 0:   
        robotArm.grab()
        robotArm.moveRight()
        robotArm.drop()
        robotArm.moveLeft()
        robotArm.grab()
        robotArm.moveLeft()
        robotArm.drop()
        robotArm.moveRight()
        i -= 1
# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()