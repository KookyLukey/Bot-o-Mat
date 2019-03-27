import TaskList as tl
import random
from time import sleep

class Robot(object):
    """A robot that will do tasks after the user creates the bot:

    Attributes:
        name: A string representing the robot's name.
        type: A string representing the robots type.
        curTasks: A dictionary to store the robots current tasks
        completedTasks: A list to store which tasks the robot has completed
        isRunning: A boolean to check if theinstance is running or not
    """

    def __init__(self, name, type):
        self.name = name
        self.type = type
        self.curTasks = {}
        self.completedTasks = []
        self.isRunning = False
        self.completedTime = []

    def assignTasks(self):
        #Create temporary task dict so that we do not mess with the original and pick a random task to add
        tempTaskList = tl.tasks

        i = 0
        while i < 5:
            tempKey, tempVal = random.choice(list(tempTaskList.items()))

            #Add it to the instances dict and remove it from the temp so we don't get duplicates
            if tempKey in self.curTasks:
                pass
            else:
                self.curTasks[tempKey] = tempVal 
                i+=1
            print(self.curTasks)
        print(self.curTasks)

    def startTasks(self):
        for key, value in self.curTasks.items():
            sleep(value/1000)
            self.completedTasks.append(key)
            self.completedTime.append(value)

    def getCompletedCount(self):
        return len(self.completedTasks)
