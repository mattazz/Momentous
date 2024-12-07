from utils.printStuff import *


class Mountain:
    def __init__(
        self,
        taskTitle: str,
        taskDescription: str,
        loggedHours: int,
        goalHours: int,
        milestones: list,  ## [Milestone(),Milestone(),Milestone()]
    ):
        self.taskTitle = taskTitle
        self.taskDescription = taskDescription
        self.loggedHours = (
            loggedHours  ## will eventually be the sum of all Milestone.loggedHours
        )
        self.goalHours = goalHours
        self.milestones = milestones

    def __str__(self):
        milestones_str = "\n".join(str(milestone) for milestone in self.milestones)
        return (
            f"⛰ {self.taskTitle} ⛰\n"
            f"💡 {self.taskDescription} 💡\n"
            f"Goal Hours: {self.goalHours}\n"
            f"Number of Hours Spent: {self.loggedHours}\n"
            f"Milestones: \n{milestones_str}"
        )

    def addMilestone(self, title, description):
        userMilestone = Milestones(title, description, 0)

        self.milestones.append(userMilestone)

    def printMilestones(self):
        print("Here are your milestones")

        for index, item in enumerate(self.milestones, start=1):
            print(f"{index}: {item}")

    
    def editMountainName(self):
        print("hello") # check only

    def editMilestones(self):
        while True:  # Allow multiple edits of milestones
            try:
                milestoneToEdit = int(input("Which milestone would you like to edit? (Enter the number): "))
                if 1 <= milestoneToEdit <= len(self.milestones):
                    selectedMilestone = self.milestones[milestoneToEdit - 1]
                    selectedMilestone.title = input("What would you like to rename the Milestone to? ")
                    selectedMilestone.description = input("What description? ")
                    print(f"Here's the new Milestone name: {selectedMilestone.title}. \n")
                    print(f"Here's the new Milestone description: {selectedMilestone.description}. \n")
                    # Handle 'edit another' prompt with input validation
                    while True:
                        another_edit = input("Would you like to edit another Milestone? (Y/N)").lower()
                        if another_edit == "n":
                            break  # Break from inner loop and stop editing
                        elif another_edit == "y":
                            break  # Break from inner loop and continue to edit another
                        else: 
                            print("Invalid response. Please enter 'Y' or 'N'.")
                    break
                else:
                    print("Please enter the corresponding Milestone number.")
            except ValueError:
                print("Please enter a valid number corresponding to the milestone you would like to change.")

    def updateLoggedHours(self):
        sum = 0
        for i in self.milestones:
            sum += i
        self.loggedHours = sum
        return self.loggedHours


class Milestones:
    def __init__(
        self,
        title: str,
        description: str,
        loggedHours: int,
    ):
        self.title = title
        self.description = description
        self.loggedHours = loggedHours

    def __str__(self):
        return (
            f" ⛳ {self.title} ⛳\n"
            f" {self.description}\n"
            f"Hours spent = {self.loggedHours}\n"
        )


# Main Create function for Task
def addMainTask():
    printEmptyLine(1)
    printHash(30)
    userTaskTitle = input("What's the title?")
    userTaskDesc = input("What's the description?")
    userGoalHours = input("How many hours do you want to commit?")

    newTask = Mountain(
        taskTitle=userTaskTitle,
        taskDescription=userTaskDesc,
        loggedHours=0,
        goalHours=userGoalHours,
        milestones=[],
    )
    printEmptyLine(1)
    printHash(30)
    print(f"⛰ This is your new task, good luck in learning {newTask.taskTitle} ⛰")
    printHash(30)
    print(newTask)
    printHash(30)

    pressToContinue()

    return newTask  # -> Class Task
