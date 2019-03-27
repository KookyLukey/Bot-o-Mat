import TaskList as tl
import random
from time import sleep

class Robot(object):
    """A robot that will do tasks after the user creates the bot:

    Attributes:
        name: A string representing the robot's name.
        type: A string representing the robots type.
        curTasks: A dictionary to store the robots current tasks
    """

    def __init__(self, name, type):
        self.name = name
        self.type = type
        self.curTasks = {}
        self.completedTasks = []
        self.isRunning = False

    def assignTasks(self):
        for i in range(5):
            #Create temporary task dict so that we do not mess with the original and pick a random task to add
            tempTaskList = tl.tasks 
            tempKey, tempVal = random.choice(list(tempTaskList.items()))

            #Add it to the instances dict and remove it from the temp so we don't get duplicates
            self.curTasks[tempKey] = tempVal 
            tempTaskList.pop(tempKey, None)

    def startTasks(self):
        for key, value in self.curTasks.items():
            sleep(value/1000)
            self.completedTasks.append(key)


