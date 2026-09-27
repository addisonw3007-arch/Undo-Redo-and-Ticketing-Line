from node import Node

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, value):
        new_node = Node(value)

        if self.rear is None:
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if self.front is None:
            return None

        value = self.front.value
        self.front = self.front.next

        if self.front is None:
            self.rear = None

        return value

    def peek(self):
        if self.front is None:
            return None

        return self.front.value

    def print_queue(self):
        current = self.front

        while current is not None:
            print(current.value)
            current = current.next

queue = Queue()

while True:
    print("\nHelp Desk Queue")
    print("1. Add customer")
    print("2. Help next customer")
    print("3. View next customer")
    print("4. View all waiting customers")
    print("5. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        name = input("Enter customer name: ")
        queue.enqueue(name)

    elif choice == "2":
        customer = queue.dequeue()

        if customer is not None:
            print(customer, "has been helped")
        else:
            print("No customers are waiting")

    elif choice == "3":
        customer = queue.peek()

        if customer is not None:
            print("Next customer:", customer)
        else:
            print("No customers are waiting")

    elif choice == "4":
        queue.print_queue()

    elif choice == "5":
        break