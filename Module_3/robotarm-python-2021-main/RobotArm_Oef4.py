from RobotArm import RobotArm

robotArm = RobotArm('exercise 4')

# Jouw python instructies zet je vanaf hier:
i = 5
while i > 0:
    robotArm.grab()
    for x in range(1,3):
        robotArm.moveRight()
    robotArm.drop()
    if i == 1:
        break
    for x in range(3,1,-1):
        robotArm.moveLeft()
    i = i - 1    
e = 6
robotArm.grab()
while e > 1:        
    for x in range(3,2,-1):
        robotArm.moveLeft()
    robotArm.drop()    
    for x in range(2,3):
        robotArm.moveRight()
    e = e - 1
    if e <= 1:
        break
    robotArm.grab()
# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()