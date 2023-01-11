"""
Stack Data structure 
"""

class Stack():
    def __init__(self) -> None:
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
       return  self.items.pop()

    def get_stack(self):
        """
        
        """
        return self.items

    def is_empty(self):
        """
        It will return weather or not stack is empty.
        """
        return self.items == []

    def peek(self):
        """
        peek check if the stack is empty or not, if it not empty then it will return 
        the last element of the list.
        """
        if not self.is_empty():
            return self.items[-1]


myStack = Stack()
myStack.push("A")
myStack.push("B")
print(myStack.get_stack())
myStack.push("C")
print(myStack.get_stack())
myStack.pop()
print(myStack.get_stack())
