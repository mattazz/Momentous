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
            exitProgram()
        case _:
            invalidChoice()


def userInputMenu():
    menuItems = [
        "Add a Mountain",
        "Add Milestone",
        "Print Milestones",
        "Show your Mountain",
        "Edit Mountain Name" "Exit",
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
    ## Kev implement ##
    userTask.printMilestones()  # [milestone1,milestone2,milestone3]
     # Check whether the user wants to edit any milestones
    while True:  # Ensure user provides valid input for "Would you like to edit?"
        confirm = input("Would you like to edit any of your milestones? (Y/N)").lower()
        if confirm == "n":
            print("No changes made.")
            break
        elif confirm == "y":
            while True:  # Allow multiple edits of milestones
                try:
                    milestoneToEdit = int(input("Which milestone would you like to edit? (Enter the number): "))
                    if 1 <= milestoneToEdit <= len(self.milestones):
                        selectedMilestone = self.milestones[milestoneToEdit - 1]
                        selectedMilestone.title = input("What would you like to rename the Milestone to? ")
                        print(f"Here's the new Milestone name: {selectedMilestone.title}. \n")
                        
                        # Handle 'edit another' prompt with input validation
                        while True:
                            another_edit = input("Would you like to edit another Milestone? (Y/N)").lower()
                            if another_edit == "n":
                                print("Exiting Milestone editing.")
                                break  # Break from inner loop and stop editing
                            elif another_edit == "y":
                                break  # Break from inner loop and continue to edit another
                            else: 
                                print("Invalid response. Please enter 'Y' or 'N'.")
                    else:
                        print("Please enter the corresponding Milestone number.")
                except ValueError:
                    print("Please enter a valid number corresponding to the milestone you would like to change.")
        else:
            print('Invalid input. Please answer "Y" or "N"')
    # 1: milestone #1
    # 2: milestone #2

    # userInput = int(input("select a number to edit: ")) -> Try catch
    # Input what milestone to edit the name: 1

    # userTask.milestones[i - 1].title = input("What's the new name?")


def exitProgram():
    sys.exit()


while True:
    main()
