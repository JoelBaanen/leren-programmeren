from RobotArm import RobotArm

robotArm = RobotArm('exercise 11')

# Jouw python instructies zet je vanaf hier:
for a in range(8):
    robotArm.moveRight()
for x in range(9):
    robotArm.grab()
    if robotArm.scan() == "white":
        robotArm.moveRight()
        robotArm.drop()
        robotArm.moveLeft()  
    else:
        robotArm.drop()
    if x < 8:
        robotArm.moveLeft()
    
# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()