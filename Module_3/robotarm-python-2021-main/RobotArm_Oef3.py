from RobotArm import RobotArm

robotArm = RobotArm('exercise 3')

# Jouw python instructies zet je vanaf hier:
x = 1
while x <= 4:
    robotArm.grab()
    robotArm.moveRight()
    robotArm.drop()
    robotArm.moveLeft()
    x = x + 1
    

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()