from RobotArm import RobotArm

robotArm = RobotArm('exercise 6')

# Jouw python instructies zet je vanaf hier:
robotArm.moveRight()
for x in range(6):
    robotArm.grab()
    if robotArm.scan()=="red":
        robotArm.moveRight()
        robotArm.drop()
        robotArm.moveLeft()
    elif robotArm.scan()=="white":
        robotArm.moveLeft()
        robotArm.drop()
        robotArm.moveRight()

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()