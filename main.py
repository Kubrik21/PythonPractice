from funct import load_todo,save_todo



while True:
    choice = input("Add, Show, Exit, Edit")
    choice=choice.strip()

    if choice.startswith("Add"):

        todo=input("Enter a todo") +"\n"

        list=load_todo("todos.txt")

        list.append(todo.capitalize())

        save_todo("todos.txt",list)

    elif choice.startswith("Show"):
        with open("todos.txt","r") as file:
            for index, x in enumerate(file):
                print(index,". ",x)

    elif choice.startswith("Exit"):
        break

    elif choice.startswith("Edit"):
        try:
            which=input("Whitch one?")
            new=input("Enter a todo")

            todos=load_todo("todos.txt")
            todos[int(which) - 1] = f"{new}\n"

            save_todo(filepath="todos.txt",content=todos)
        except ValueError:
            print("błąd przy edycji")
            continue

    else:
        print("No maching")


