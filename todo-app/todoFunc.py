
def getTodos(filepath):
    with open(filepath, 'r') as file:
        todos = file.readlines()
        return todos
def writelines(filepath,todos):
    with open(filepath, 'w') as file:
        for todo in todos:
            file.write(f"{todo}")
def addTodos(filepath,todos,userInp):
    getTodos(filepath)
    todos.append(f'{userInp}\n')
    writelines(filepath,todos)
def showTodos(filepath):
    todos = getTodos(filepath)
    for items,todo in enumerate(todos):
        print(items+1, todo)
    return todos

def editTods(filepath):
    todos = getTodos(filepath)
    showTodos(filepath)
    index = int(input('Enter the number of the task to edit : '))
    todos[index-1] = input("new Task : ")
    writelines(filepath,todos)

def completeTask(filepath, todos):
    showTodos(filepath)
    index = int(input("please enter the index of the completed task"))
    todos.pop(index)
