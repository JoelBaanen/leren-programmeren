from RobotArm import RobotArm
robotArm = RobotArm('exercise 10')
i = 9
for x in range(5):
    robotArm.grab()
    for x in range(i):
        robotArm.moveRight()
    i -= 1
    robotArm.drop()
    for a in range(i):
        robotArm.moveLeft()
    i -= 1
robotArm.wait()