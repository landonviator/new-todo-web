file_path = 'todos.txt'

container = []

def init_file():
    with open(file_path, 'r') as file:
        container = file.readlines()

def get_todos(path = file_path):
    with open(path, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local

def add_todo(_user_input):
    with open(file_path, 'w') as file:
        file.writelines(_user_input) 

def show_todos():
    new_todos = []
    for item in container:
        new_item = item.strip('\n')
        new_todos.append(new_item)
    for index, todo in enumerate(new_todos):
        print(index, todo)


def edit_todo():
    try:
        item_to_edit = int(input("Which item do you want to edit?"))
        item_to_edit -= 1
        should_replace = input("Do you want to replace it with another item?")
        # match should_replace:
        #     case 'yes':
        #         replacement = input("What's the new item?")
        #         if item_to_edit < container.__len__():
        #             container[item_to_edit] = replacement
        #     case 'no':
        #         container.remove(container[item_to_edit])
    except IndexError:
        print("Your command was not valid!")

def close_file():
    file.close()