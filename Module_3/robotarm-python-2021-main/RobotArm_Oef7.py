from RobotArm import RobotArm
robotArm = RobotArm('exercise 7')
for x in range(1,6):
    for x in range(1,7):
        robotArm.moveRight()    
        robotArm.grab()
        robotArm.moveLeft()
        robotArm.drop()
    robotArm.moveRight()        
    robotArm.moveRight()
robotArm.wait()