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

            # 1: milestone #1
            # 2: milestone #2

            # Input what milestone to edit the name: 1
            # milestoneToEdit = self.milestones[i - 1]
            # milestoneToEdit.title. = input("What's the new name?")

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
