# binary tree node

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def max_height(node):
    # if node is empty
    if node is None:
        return -1
    # if node is not empty
    else:
        # compute height of each subtree
        left_sub_tree_height = max_height(node.left)
        right_sub_tree_height = max_height(node.right)

        if(left_sub_tree_height > right_sub_tree_height):
            return left_sub_tree_height + 1
        else:
            return right_sub_tree_height + 1

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

# print(max_height(root))

def bitcount(n):
    count = 0
    while n > 0:
        count = count + 1
        # bitwise and
        n = n & (n-1)
    return count

# print(bitcount(5))


def setBits(N):
	# code here
    s = bin(N)
    count = 0
    for i in s:
        if (i == '1'):
            count +=1
    return count

print(setBits(2))
	