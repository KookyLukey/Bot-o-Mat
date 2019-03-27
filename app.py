import TaskList
import Robot
import threading

curRobots = []
botTasks = TaskList.tasks
mainMenuSel = 0

def runMainMenu():
    print('Welcome to Bot-o-Mat. Please select one of the following:')
    print('1: Add a robot')
    print('2: Check current robot status')
    print('3: Exit')
    mainMenuSel = input('Enter selection: ')

    if mainMenuSel == '1':
        botName = input('Enter the robot name:')
        botType = input('Enter the type:')

        curRobots.append(Robot.Robot(botName, botType))
        curRobots[len(curRobots) - 1].assignTasks()
        curRobots[len(curRobots) - 1].isRunning = True
        threading.Thread(target=curRobots[len(curRobots) - 1].startTasks).start()

        runMainMenu()
    
    elif mainMenuSel == '2':
        for bots in curRobots:
            print(bots.name)
            print(bots.completedTasks)
        runMainMenu()

runMainMenu()