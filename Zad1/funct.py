FILEPATH = "todos.txt"

def load_todo(filepath=FILEPATH):
    with open(filepath, 'r') as file:
        list = file.readlines()
    return list

def save_todo(content,filepath=FILEPATH):
    with open(filepath, 'w') as file:
        file.writelines(content)