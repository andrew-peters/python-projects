
# A simple Python program for traversal of a linked list
# Node class
class Node:
    # Function to initialise the node object
    def __init__(self, data):
        self.val = data  # Assign data
        self.next = None  # Initialize next as null
  
# Linked List class contains a Node object
class LinkedList:
    # Function to initialize head
    def __init__(self):
        self.head = None
 
    # This function prints contents of linked list
    # starting from head
    def printList(self):
        temp = self.head
        while (temp):
            print (temp.data)
            temp = temp.next
 
llist = LinkedList()
llist.head = Node(1)
second = Node(2)
third = Node(1)
llist.head.next = second; # Link first node with second
second.next = third; # Link second node with the third node

def isLinkedListPal(head):
    temp = []
    while head is not None:
        temp.append(head.val)
        head = head.next
    return temp == temp[::-1]

print(isLinkedListPal(llist.head))

# if __name__=='__main__':
 
#     # Start with the empty list
#     llist = LinkedList()
 
#     llist.head = Node(1)
#     second = Node(2)
#     third = Node(3)
 
#     llist.head.next = second; # Link first node with second
#     second.next = third; # Link second node with the third node
 
#     llist.printList()
    