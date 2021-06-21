class Node:
    """
    class Node, has properties for the value stored in the Node
    it has a pointer to the next node
    """
    def __init__(self, value, next=None):
        self.value = value
        self.next = next 
        


class LinkedList:
    """
    class LinkedList includes a head property
    upon instantiation an empty list will be created

    class LinkedList includes methods: 

        - "insert" which takes in any value as an argument and adds a new node with that value to the head of the list with an O(1) time performance

        - "includes" which takes in any value as an argument and returns a boolean result depending on whether that value exists as a Node's value somewhere within the list

        - "__str__" which takes in no arguments and returns a string representing all the values in the Linked List, formatted as:

        "{a} -> {b} -> {c} -> None"

    """
    def __init__(self, head=None):
        self.head = head

    def insert(self, value):
        node = Node(value)

    def includes(self, value):
        if self.head is not in None:
            node.next = self.head

    # def __init__(self, value, next=None):
    #     self.value = value
    #     self.next = next


    # def some_method(self):
    #     # method body here
    #     pass
