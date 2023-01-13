from RobotArm import RobotArm

robotArm = RobotArm('exercise 5')

# Jouw python instructies zet je vanaf hier:
for x in range(1,8):
    robotArm.moveRight()
i = 8
for a in range(i):
    robotArm.grab()
    for a in range(1,2):
        robotArm.moveRight()
    robotArm.drop()  
    if i >= 2:
        for b in range(3,1,-1):
            robotArm.moveLeft()
    i -= 1
    
    
# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()