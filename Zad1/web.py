import streamlit as st
import funct

def add_todo():
    newTodo=st.session_state["new_todo"]
    todos.append(f"{newTodo}\n")
    print(todos)
    funct.save_todo(todos,r"C:\Users\olejn\Desktop\PythonCourse40Days\1Project\Zad1\todos.txt")

todos=funct.load_todo(r"C:\Users\olejn\Desktop\PythonCourse40Days\1Project\Zad1\todos.txt")

st.title("My todo App")
st.subheader("This is my todo app.")



for index,todo in enumerate(todos):
    st.checkbox(todo,key=index)
    print(index,": ",todo)

st.text_input(label="Emter a todo",placeholder="Add a new todo...",on_change=add_todo,key='new_todo')