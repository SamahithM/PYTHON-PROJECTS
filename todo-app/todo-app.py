todos = []

while True:
    userInp = input("Enter add , show, edit, complete: ")
    if userInp.startswith('add'):
        userInp = userInp.strip("add")
        with open('/home/smg/Documents/PYTHON-PROJECTS/todo-app/todo-app.txt', 'r') as file:
            return file.readlines()
        todos = file.readlines()
