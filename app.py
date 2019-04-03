import TaskList as tl
import Robot
import threading
import sys

curRobots = []
botTasks = tl.tasks
botTypeList = tl.typeList
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

    #If user selects 1 add a robot
    if mainMenuSel == '1':
        botName = input('Enter the robot name: ')
        botType = input('Enter the type: ')

        #Check if the type is a valid type and if it is, assign the bot 5 random tasks and start the bot
        if botType.upper() in botTypeList:
            isCreated = False
            for index, curBot in enumerate(curRobots):
                #If the name of the bot already exists, add the new tasks to the old instance
                if curBot.name.upper() == botName.upper():
                    setattr(curRobots[index], 'type', botType)
                    curRobots[index].curTasks.clear()
                    curRobots[index].assignTasks()
                    curRobots[index].isRunning = True
                    threading.Thread(target=curRobots[index].startTasks).start()
                    isCreated = True
                    break

            if not isCreated:
                curRobots.append(Robot.Robot(botName, botType))
                curRobots[len(curRobots) - 1].assignTasks()
                curRobots[len(curRobots) - 1].isRunning = True
                threading.Thread(target=curRobots[len(curRobots) - 1].startTasks).start()
        else:
            print()
            print('That is not a correct type. Please try again.')

        runMainMenu()

    #If user selects 2 print out the bots name, type, and completed tasks
    elif mainMenuSel == '2':
        for bots in curRobots:
            print(bots.name + ': ' + bots.type)
            print(bots.completedTasks)
        runMainMenu()

    #If user selects 3 print out a leaderboard of completed tasks with the highest bot at the top
    elif mainMenuSel == '3':
        tempBots = curRobots
        tempBots = sorted(tempBots, key=lambda bot: len(bot.completedTasks), reverse=True)

        for i in tempBots:
            print(i.name + " has completed " + str(len(i.completedTasks)) + " tasks.")

        runMainMenu()

    #If user selects 4 print out the total time in milliseconds the bot has been running tasks
    elif mainMenuSel == '4':
        tempBots = curRobots
        tempBots = sorted(tempBots, key=lambda bot: sum(bot.completedTime), reverse=True)

        for i in tempBots:
            print(i.name + " has taken " + str(sum(i.completedTime)) + " milliseconds to complete its tasks.")
        runMainMenu()

    #Exit the program
    elif mainMenuSel == '5':
        sys.exit()


runMainMenu()
