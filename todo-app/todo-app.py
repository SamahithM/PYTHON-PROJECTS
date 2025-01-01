import todoFunc as tf


todos = []
def todo():
    filepath = input("filepath: ")
    while True:
        userInp = input("Enter add , show, edit, complete: ")
        if userInp.startswith('add'):
            userInp = userInp.strip("add")
            tf.addTodos(filepath,todos,userInp)
        elif userInp.startswith('show'):
            tf.showTodos(filepath)
        elif userInp.startswith("edit"):
            tf.editTods(filepath)
        elif userInp.startswith("complete"):
            tf.completeTask(filepath, todos)
        elif userInp.startswith("exit"):
            exit()
todo()
print("samahith")
