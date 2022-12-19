import funct
#import cli
import PySimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box=sg.InputText(tooltip="Enter todo",key="todo")
add_button=sg.Button("Add")
layout=[[label],[input_box,add_button]]

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
            todos.append(new_todo)
            funct.save_todo(todos)
        case sg.WIN_CLOSED:
            break

window.close()