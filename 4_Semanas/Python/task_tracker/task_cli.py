import sys
import os
import datetime
import json


def readArgs():
    if len(sys.argv) < 2:
        print("Use: python task_cli.py <command>")
        sys.exit(1)
    else:
        return sys.argv[1:]


def translateArgs():
    args = readArgs()
    if args[0] == "add":
        addTask(args[1])
    elif args[0] == "update":
        updateTask(args[1], args[2])
    elif args[0] == "delete":
        deleteTask(args[1])
    elif args[0] == "mark-in-progress":
        markInProgress(args[1])
    elif args[0] == "mark-done":
        markDone(args[1])
    elif args[0] == "list":
        listTasks()


def addTask(t):
    global id
    task = {"id": id,
            "description": t,
            "status": "todo",
            "created-at": f"{datetime.datetime.now().strftime('%d-%m-%Y')}/{datetime.datetime.now().strftime('%H-%M-%S')}",
            "updated-at": f"{datetime.datetime.now().strftime('%d-%m-%Y')}/{datetime.datetime.now().strftime('%H-%M-%S')}"
            }

    print(f"Task added! ID: {id}")
    id += 1

    editTasksFile("write", t=task)


def updateTask(task_id, new_description):
    editTasksFile("update", id=int(task_id), t=new_description)


def deleteTask(id):
    editTasksFile("delete", id=id)


def markInProgress(id):
    editTasksFile("mark-in-progress", id=id)


def markDone(id):
    editTasksFile("mark-done", id=id)


def listTasks():
    for task in getTasksInFile():
        print(f"Todo: {task['description']}\tStatus: {task['status']}")


def createTaskFile():
    with open("E:\\Programacao\\Projetos\\Projects\\4_Semanas\\Python\\task_tracker\\tasks.json", "w") as f:
        f.write("[]")


def editTasksFile(func, id=None, t=None):
    if not os.path.exists("E:\\Programacao\\Projetos\\Projects\\4_Semanas\\Python\\task_tracker\\tasks.json"):
        createTaskFile()

    try:
        with open("E:\\Programacao\\Projetos\\Projects\\4_Semanas\\Python\\task_tracker\\tasks.json", "r") as f:
            file = json.loads(f.read())
    except json.JSONDecodeError:
        file = []

    if func == "delete":
        file = [task for task in file if task["id"] != id]
        

    elif func == "write":
        file.append(t)

    elif func == "update":
        for task in file:
            if task["id"] == id:
                task["description"] = t
                task["updated-at"] = f"{datetime.datetime.now().strftime('%d-%m-%Y')}/{datetime.datetime.now().strftime('%H-%M-%S')}"
                break

    elif func == "mark-in-progress":
        for task in file:
            if task["id"] == id:
                task["status"] = "in-progress"
                break

    elif func == "mark-done":
        for task in file:
            if task["id"] == id:
                task["status"] = "done"
                break

    with open("E:\\Programacao\\Projetos\\Projects\\4_Semanas\\Python\\task_tracker\\tasks.json", "w") as f:
        f.write(json.dumps(file))


def getTasksInFile():
    try:
        with open("E:\\Programacao\\Projetos\\Projects\\4_Semanas\\Python\\task_tracker\\tasks.json", "r") as f:
            return json.loads(f.read())
    except json.JSONDecodeError:
        return []


tasks = getTasksInFile()
if tasks:
    id = tasks[-1]["id"] + 1
else:
    id = 0


def main():
    translateArgs()


if __name__ == "__main__":
    main()
