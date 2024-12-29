todos = []
def todo():
    while True:
        userInp = input("Enter add , show, edit, complete: ")
        if userInp.startswith('add'):
            userInp = userInp.strip("add")
            with open('todo.txt', 'r') as file:
                todos = file.readlines()
            todos.append(userInp)
            with open('todo.txt', 'w') as file:
                for todo in todos:
                    file.write(todo)
        else:
             exit()

todo()
