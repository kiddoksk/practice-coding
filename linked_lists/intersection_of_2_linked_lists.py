import re


class Node:
    def __init__(self, data = 0, next = None):
        self.data = data
        self.next = next


def intersection_point(head1, head2):
    ptr1 = head1
    ptr2 = head2

    if (ptr1 == None or ptr2 == None):
        return
    
    while(ptr1 != ptr2):
        ptr1 = ptr1.next
        ptr2 = ptr2.next

        if(ptr1 == ptr2):
            return ptr1
        
        if(ptr1 == None):
            ptr1 = head2
        
        if(ptr2 == None):
            ptr2 = head1
    
    return ptr1

def print_node(node):
    if (node == None):
        print("None")
    while (node.next != None):
        print(node.data,end="->")
        node = node.next
    print(node.data)


head1 = Node()
head1.data = 10

head2 = Node()
head2.data = 3

newNode = Node()
newNode.data = 6
head2.next = newNode

newNode = Node()
newNode.data = 9
head2.next.next = newNode

newNode = Node()
newNode.data = 15
head1.next = newNode

head2.next.next.next = newNode

newNode = Node()
newNode.data = 30
head1.next.next = newNode

head1.next.next.next = None
intersect_node = None
 
  # Find the intersection node of two linked lists
intersect_node = intersection_point(head1, head2)
print(intersect_node.data)
print("INTERSEPOINT LIST :",end="")
 
# print_node(intersect_node)
