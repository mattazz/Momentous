from classes.Task import Mountain, Milestones, addMainTask
from utils.printStuff import *
import sys

# Global Vars
userTask = None


def main():
    userMenuAction: int = userInputMenu()

    match userMenuAction:
        case 1:  # if userMenuAction == 1
            addMountain()
        case 2:
            addMilestone()
        case 3:
            printMilestones()
        case 4:
            printMountain()
        case 5:
            editMountainName()
        case 6:
            editMilestones()
        case 7:
            exitProgram()
        case _:
            invalidChoice()


def userInputMenu():
    menuItems = [
        "Add a Mountain",
        "Add Milestone",
        "Print Milestones",
        "Show your Mountain",
        "Edit Mountain Name",
        "Edit Milestones",
        "Exit",
    ]
    printEmptyLine(1)
    printHash(30)
    for index, item in enumerate(menuItems, start=1):
        print(f"{index}: {item}")
    printHash(30)
    printEmptyLine(1)

    while True:
        try:
            userChoice = int(input("Select a menu number: "))
            break
        except ValueError:
            printEmptyLine()
            print("Please input a valid number")
    return userChoice


def invalidChoice():
    printEmptyLine(1)
    print("Invalid menu choice. Try again")


def addMountain():
    global userTask
    print("What's your main goal? ⛰")
    userTask = addMainTask()
    return


def addMilestone():
    print("Want to add a milestone?")
    printEmptyLine(1)

    userTitle = input("What title for this milestone?")
    userDesc = input("What description?")

    userTask.addMilestone(userTitle, userDesc)
    pressToContinue()

    return


def printMilestones():
    userTask.printMilestones()
    pressToContinue()
    return

def printMountain():
    print(userTask)
    return

def editMountainName():
    print(userTask)
    return

def editMilestones():
    ## Kev implement ##
    userTask.printMilestones()  # [milestone1,milestone2,milestone3]
    userTask.editMilestones()
    pressToContinue()
    return

def exitProgram():
    sys.exit()


while True:
    main()
