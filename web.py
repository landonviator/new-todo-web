import functions
import streamlit as sl

todos = functions.get_todos()

def add_todos_local():
    input = sl.session_state["new_todo"]
    todos.append(input + "\n")
    functions.add_todo(todos)

sl.title("Viator DSP")
sl.subheader("Todo App, April 18 2024")
sl.text("Learning python and how to make web apps and stuff")

for todo in functions.get_todos():
    sl.checkbox(todo)

sl.text_input(label = "Enter Todos", placeholder = "Enter a todo...", on_change = add_todos_local, key = "new_todo")