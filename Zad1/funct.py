
def load_todo(filepath):
    with open(filepath, 'r') as file:
        list = file.readlines()
    return list

def save_todo(filepath,content):
    with open(filepath, 'w') as file:
        file.writelines(content)