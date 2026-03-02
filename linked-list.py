
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class SingleLinkedList:
    def __init__(self):
        self.head=None
    def insert_beginning(self,data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node
    def insert_end(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            return
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=new_node
    def delete_by_value(self,value):
        temp=self.head
        while temp.next.data != value:
            temp=temp.next
        temp.next=temp.next.next
    def traversal(self):
        temp=self.head
        while temp:
            print(temp.data)
            temp=temp.next

sll=SingleLinkedList()
sll.insert_beginning(10)
sll.insert_end(20)
sll.insert_end(30)
sll.delete_by_value(20)
sll.traversal()



# SIR'S METHOD :



# Creating a class named Node
# class → used to create user-defined data type
# Node → name of the class
class Node:
    
    # __init__ → constructor function
    # self → reference to current object
    # data → value stored in node
    def __init__(self, data):
        
        # self.data → variable to store data in node
        self.data = data
        
        # self.next → pointer to next node
        # None → means no next node (null)
        self.next = None


# Creating a class for Linked List
class LinkedList:
    
    # Constructor for LinkedList
    def __init__(self):
        
        # self.head → stores address of first node
        # Initially list is empty, so head is None
        self.head = None


    # Function to insert a new node at the end
    def insert(self, data):
        
        # Create a new node using Node class
        new_node = Node(data)
        
        # If linked list is empty
        if self.head is None:
            
            # Make new node as first node
            self.head = new_node
            return
        
        # temp → temporary variable to traverse list
        temp = self.head
        
        # while → loop runs until condition is False
        # temp.next != None → move until last node
        while temp.next is not None:
            temp = temp.next
        
        # Connect last node to new node
        temp.next = new_node


    # Function to display all elements (Traversal)
    def traverse(self):
        
        # temp starts from head node
        temp = self.head
        
        # If list is empty
        if temp is None:
            print("Linked List is empty")
            return
        
        # Loop through linked list
        while temp is not None:
            
            # Print data of current node
            print(temp.data, end=" -> ")
            
            # Move to next node
            temp = temp.next
        
        # Print None at end of list
        print("None")


    # Function to search an element
    def search(self, key):
        
        # temp starts from head
        temp = self.head
        
        # position → keeps track of node number
        position = 1
        
        # Loop until end of list
        while temp is not None:
            
            # If data matches key
            if temp.data == key:
                print(f"Element {key} found at position {position}")
                return
            
            # Move to next node
            temp = temp.next
            position += 1
        
        # If element not found
        print(f"Element {key} not found in linked list")


# Creating object of LinkedList class
ll = LinkedList()

# Inserting elements
ll.insert(10)
ll.insert(20)
ll.insert(30)
ll.insert(40)

# Traversing linked list
print("Linked List elements:")
ll.traverse()

# Searching elements
ll.search(30)
ll.search(50)

ll.insert(4893)
ll.insert(2501010070)

print("Linked List elements:")
ll.traverse()

ll.search(2501010070)




# new linked list program - sir code 



# ---------------- LINKED LIST PROGRAM IN PYTHON ----------------
# Linked List is a linear data structure
# It is made of nodes
# Each node has two parts:
# 1. data  -> stores the value
# 2. next  -> stores address of next node


# ---------------- NODE CLASS ----------------
# class keyword is used to create a class
class Node:
    
    # __init__ is a constructor
    # It is automatically called when object is created
    def __init__(self, data):
        # self refers to the current object
        # data stores the value of the node
        self.data = data
        
        # next stores address of next node
        # Initially it is set to None
        self.next = None


# ---------------- LINKED LIST CLASS ----------------
class LinkedList:
    
    # Constructor of LinkedList
    def __init__(self):
        # head stores address of first node
        # Initially list is empty, so head is None
        self.head = None


    # ---------------- INSERT OPERATION ----------------
    # This function inserts node at the end
    def insert(self):
        # input() takes value from user
        # int() converts input to integer
        value = int(input("Enter value to insert: "))
        
        # Create new node using Node class
        new_node = Node(value)
        
        # If linked list is empty
        if self.head is None:
            # New node becomes first node
            self.head = new_node
            print("Node inserted as first node")
        else:
            # temp is used to traverse the list
            temp = self.head
            
            # Traverse till last node
            while temp.next is not None:
                temp = temp.next
            
            # Link last node to new node
            temp.next = new_node
            print("Node inserted at end")


    # ---------------- DELETE OPERATION ----------------
    # This function deletes first node
    def delete(self):
        # If list is empty
        if self.head is None:
            print("Linked list is empty, cannot delete")
        else:
            # Store head node in temp
            temp = self.head
            
            # Move head to next node
            self.head = self.head.next
            
            # Delete reference of temp
            del temp
            print("First node deleted")


    # ---------------- TRAVERSAL OPERATION ----------------
    # This function displays all nodes
    def traversal(self):
        # If list is empty
        if self.head is None:
            print("Linked list is empty")
        else:
            print("Linked list elements are:")
            
            # temp starts from head
            temp = self.head
            
            # Loop till last node
            while temp is not None:
                # Print data of each node
                print(temp.data)
                
                # Move to next node
                temp = temp.next


    # ---------------- SEARCH OPERATION ----------------
    # This function searches a value in list
    def search(self):
        # input() takes value to search
        value = int(input("Enter value to search: "))
        
        # temp starts from head
        temp = self.head
        
        # position keeps track of node number
        position = 1
        
        # Traverse list
        while temp is not None:
            # If value found
            if temp.data == value:
                print("Value found at position", position)
                return
            
            # Move to next node
            temp = temp.next
            position += 1
        
        # If value not found
        print("Value not found in linked list")


# ---------------- MAIN PROGRAM ----------------
# Create LinkedList object
ll = LinkedList()

# Infinite loop for menu driven program
while True:
    print("\nLinked List Operations")
    print("1. Insert")
    print("2. Delete")
    print("3. Traversal")
    print("4. Search")
    print("5. Exit")
    
    # Take user choice
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        ll.insert()
    elif choice == 2:
        ll.delete()
    elif choice == 3:
        ll.traversal()
    elif choice == 4:
        ll.search()
    elif choice == 5:
        print("Exiting program")
        break
    else:
        print("Invalid choice, try again")