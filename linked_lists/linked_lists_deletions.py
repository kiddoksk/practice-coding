from cgitb import text


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None


    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
    
    def delete(self, key):

        #store head in temp
        temp = self.head

        # deleted element is head ( 1st node in linkedlist )
        if temp is not None:
            if(key == temp.data):
                self.head = temp.next
                temp = None
                return            

        # search for key and track prev node as we need to point it to the next node
        while(temp is not None):
            if(temp.data == key):
                break
            prev = temp
            temp = temp.next
        
        if (temp == None):
            return
        
        prev.next = temp.next

        temp = None

    def print_linked_list(self):
        temp = self.head
        while(temp):
            print(temp.data, ' ')
            temp = temp.next

if __name__ == '__main__':
    llist = LinkedList()
    llist.push(7)
    llist.push(1)
    llist.push(3)
    llist.push(2)
    llist.print_linked_list()
    print('\n')
    llist.delete(7)
    llist.print_linked_list()