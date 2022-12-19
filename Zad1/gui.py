import funct
#import cli
import PySimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box=sg.InputText(tooltip="Enter todo",key="todo")
add_button=sg.Button("Add")
listBox=sg.Listbox(values=funct.load_todo(),key="listbox",enable_events=True,size=[45,10])
edit_button=sg.Button("Edit")
complete_button=sg.Button("Complete")
exit_button=sg.Button("Exit")

layout=[[label],
        [input_box,add_button],
        [listBox,edit_button],
        [complete_button,exit_button]]

window = sg.Window("Todo App",layout=layout,
                   font=('Helvetica',16),
                   size=(700,500)
                   )
while True:
    event,values=window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todos=funct.load_todo()
            new_todo=values["todo"]
            todos.append(f"{new_todo}\n")
            funct.save_todo(todos)

            window["listbox"].update(values=todos)
        case "Edit":
            todo=values["listbox"][0]
            new_value=values["todo"]


            load=funct.load_todo()
            index = load.index(todo)
            load[index] = f"{new_value}\n"
            funct.save_todo(load)

            window["listbox"].update(values=load)
        case "listbox":
            window["todo"].update(value=values["listbox"][0])
        case "Complete":
            todo=funct.load_todo()
            actual_todo=values["listbox"][0]
            todo.remove(actual_todo)
            funct.save_todo(todo)

            window["listbox"].update(values=todo)
            window["todo"].update(value="")
        case sg.WIN_CLOSED | "Exit":
            break

window.close()