class BinaryTree:

    class Node:
        def __init__(self, data):
            self.data = data
            self.right = None
            self.left = None

    def __init__(self):
        self.root = None

    def add(self, root, data):
        if root is None:
            pass
            # Create a new root
        elif data > root.data:
            # go right
            if root.right is None:
                # Create a new node
                # Attach it to root on the right
                node = BinaryTree.Node(data)
                root.right = node
            else:
                self.add(root.right, data)
        else:
            # go left
            if root.left is None:
                # Create a new node
                # Attach it to root on the left
                node = BinaryTree.Node(data)#
                root.left = node
            else:
                self.add(root.left, data)
