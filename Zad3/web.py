import streamlit as st
from Zad1 import funct



st.set_page_config(layout="wide")
def add_todo():
    newTodo=st.session_state["new_todo"]
    todos.append(f"{newTodo}\n")
    print(todos)
    funct.save_todo(todos,r"C:\Users\olejn\Desktop\PythonCourse40Days\1Project\Zad1\todos.txt")

def complete_task():
    for elem in todos:
        if st.session_state[elem]==True:
            todos.remove(elem)
            del st.session_state[elem]

    funct.save_todo(todos, r"C:\Users\olejn\Desktop\PythonCourse40Days\1Project\Zad1\todos.txt")


todos=funct.load_todo(r"C:\Users\olejn\Desktop\PythonCourse40Days\1Project\Zad1\todos.txt")

st.title("My todo App")
st.subheader("This is my todo app.")



for todo in todos:
    st.checkbox(todo,key=todo, on_change=complete_task)
    #print(index,": ",todo)

st.text_input(label="Emter a todo",placeholder="Add a new todo...",on_change=add_todo,key='new_todo')


st.session_state