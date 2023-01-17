from node import Node

class linkedlist:
    def __init__(self):
        self.head_node = None

    def get_head(self):
        return self.head_node

    def insert_at_head(self, data):
        temp_node = Node(data)
        temp_node.next_element = self.head_node
        self.head_node = temp_node
        return self.head_node

    def is_empty(self):
        print(self.head_node)
        if self.head_node is None:
            return True
        else:
            return False

    def print_list(self):
        if (self.is_empty()):
            print("List is empty")
            return False
        temp = self.head_node
        while temp.next_element is not None:
            print(temp.data, end=" -> ")
            temp = temp.next_element
        print(temp.data, "-> None")
        return True



lst = linkedlist()
#print(lst.get_head())
#print(lst.is_empty()) 

for i in range(1, 10):
    lst.insert_at_head(i)
lst.print_list()                        