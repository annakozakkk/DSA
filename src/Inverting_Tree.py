class BinaryTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def inverting_tree(root):
    if (root == None):
        return
    queue = []
    queue.append(root)
    while (len(queue)):
        current = queue[0]
        queue.pop(0)
        current.left, current.right = current.right, current.left
        if (current.left):
            queue.append(current.left)
        if (current.right):
            queue.append((current.right))
    return root


def preorder(root):
    if (root == None):
        return
    print(root.data, end=" ")
    preorder(root.left)
    preorder(root.right)


root = BinaryTree(1)
root.left = BinaryTree(2)
root.right = BinaryTree(3)
root.left.left = BinaryTree(4)
root.left.right = BinaryTree(5)
root.right.left = BinaryTree(6)
root.right.right = BinaryTree(7)
print("Before inverting: ")
preorder(root)
print("\n")
inverting_tree(root)
print("After inverting: ")
preorder(root)
