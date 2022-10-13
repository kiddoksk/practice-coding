# Create Node class
class Node:
    # function to init node object
    def __init__(self, data):
        self.data = data
        self.next = None

# Create LinkedList Class

class LinkedList:
    # Function to initialize the Linked List object
    def __init__(self):
        self.head = None


    # insert a node in the beginning 
    def insert_in_the_beginnning(self, new_data):
        # Create a node and append data
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def insert_after(self, prev_node, new_data):
        if prev_node is None:
            print("Previous node not in linked list")
            return

        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node
    
    def insert_at_the_end(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        
        last = self.head
        while(last.next):
            last = last.next

        last.next = new_node

    def print_linked_list(self):
        temp = self.head
        while(temp):
            print(temp.data, " ")
            temp = temp.next

if __name__ == '__main__':
    llist = LinkedList()
    llist.insert_in_the_beginnning(5)
    llist.insert_at_the_end(10)
    llist.insert_after(llist.head, 17)
    llist.print_linked_list()
