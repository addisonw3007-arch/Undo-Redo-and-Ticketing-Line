from node import Node

class Stack:
    def __init__(self):
        self.top = None

def push(self, value):
    new_node = Node(value)
    new_node.next = self.top
    self.top = new_node

def pop(self):
    if self.top is None:
        return None

    value = self.top.value
    self.top = self.top.next
    return value

def peek(self):
    if self.top is None:
        return None

    return self.top.value

def print_stack(self):
    current = self.top

    while current is not None:
        print(current.value)
        current = current.next

undo_stack = Stack()
redo_stack = Stack()

while True:
    print("\nUndo/Redo System")
    print("1. Perform Action")
    print("2. Undo")
    print("3. Redo")
    print("4. View Undo Stack")
    print("5. View Redo Stack")
    print("6. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        action = input("Enter action: ")
        undo_stack.push(action)
        redo_stack = Stack()

    elif choice == "2":
        action = undo_stack.pop()

        if action is not None:
            redo_stack.push(action)
        else:
            print("No actions to undo")

    elif choice == "3":
        action = redo_stack.pop()

        if action is not None:
            undo_stack.push(action)
        else:
            print("No actions to redo")

    elif choice == "4":
        undo_stack.print_stack()

    elif choice == "5":
        redo_stack.print_stack()