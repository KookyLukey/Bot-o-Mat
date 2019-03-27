import TaskList
import Robot
import threading

curRobots = []
botTasks = TaskList.tasks
mainMenuSel = 0

def runMainMenu():
    print()
    print('Welcome to Bot-o-Mat. Please select one of the following:')
    print('1: Add a robot')
    print('2: Check current robot status')
    print('3: Leaderboard')
    print('4: Time taken to complete tasks')
    print('5: Exit')
    mainMenuSel = input('Enter selection: ')
    print()

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
            print(bots.name + ': ' + bots.type)
            print(bots.completedTasks)
        runMainMenu()
    
    elif mainMenuSel == '3':
        tempBots = curRobots
        tempBots = sorted(tempBots, key=lambda bot: len(bot.completedTasks), reverse=True)
        
        for i in tempBots:
            print(i.name + " has completed " + str(len(i.completedTasks)) + " tasks.")

        runMainMenu()

    elif mainMenuSel == '4':
        tempBots = curRobots
        tempBots = sorted(tempBots, key=lambda bot: sum(bot.completedTime), reverse=True)
        
        for i in tempBots:
            print(i.name + " has taken " + str(sum(i.completedTime)) + " milliseconds to complete its tasks.")
        runMainMenu()


runMainMenu()