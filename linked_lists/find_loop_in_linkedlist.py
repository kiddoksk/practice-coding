import re


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def print_linked_list(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next
    
    def detect_loop(self):
        temp = self.head
        s = set()

        while(temp):
            # if data is already in set, we can confirm there is a loop
            if(temp in s):
                return True
            
            # add all nodes to set
            s.add(temp)
            temp = temp.next
    
        return False

    # Floyd’s cycle detection algorithm
    def detect_cycle(self):
        slow = fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
            if slow == fast:
                print(slow.data)
                return slow

        return None

    def remove_cycle(self, node):
        head = self.head
        while head:
            ptr = node
            while ptr.next is not node and ptr.next is not head:
                ptr = ptr.next
            
            if ptr.next == head:
                ptr.next = None
                return
            head = head.next


llist = LinkedList()
llist.push(1)
llist.push(2)
llist.push(3)
llist.push(4)

# create a loop
llist.head.next.next.next.next = llist.head

if llist.detect_cycle():
    print("Loop found")
else:
    print("No Loop Found")

d = llist.detect_cycle()
llist.remove_cycle(d)

if llist.detect_cycle():
    print("Loop found")
else:
    print("No Loop Found")
