class BinaryTree:

    class Node:
        def __init__(self, data):
            self.data = data
            self.right = None
            self.left = None

    def __init__(self):
        self.root = None

    def add(self, data, root):
        if root is None:
            # Create a new root
            self.root = BinaryTree.Node(data)
        elif data > root.data:
            # go right
            if root.right is None:
                # Create a new node
                # Attach it to root on the right
                node = BinaryTree.Node(data)
                root.right = node
            else:
                self.add(data, root.right)
        else:
            # go left
            if root.left is None:
                # Create a new node
                # Attach it to root on the left
                node = BinaryTree.Node(data)#
                root.left = node
            else:
                self.add(data, root.left)

    def inorder(self, root):
        if root is None:
            return
        else:
            self.inorder(root.left)
            print(root.data)
            self.inorder(root.right)
