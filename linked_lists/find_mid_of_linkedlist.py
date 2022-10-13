from hashlib import new


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data=data)
        new_node.next = self.head
        self.head = new_node

    def print_list(self):
        temp = self.head
        while(temp):
            print(str(temp.data) + "->", end="")
            temp = temp.next

    def find_middle(self):
        slow = self.head
        fast = self.head

        while(fast and fast.next):
            slow = slow.next
            fast = fast.next.next
        
        print("\n Mid element is ", slow.data)

if __name__=='__main__':
   
    # Start with the empty list
    llist = LinkedList()
    
    llist.insert(1)
    llist.insert(2)
    llist.insert(3)
    llist.insert(4)
    llist.insert(5)
    llist.insert(6)
    llist.insert(7)

    
    llist.print_list()
    llist.find_middle()
 