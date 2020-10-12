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

    def preorder(self, root):
        if root:
            print(root.data)
            self.preorder(root.left)
            self.preorder(root.right)

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.data)
            self.inorder(root.right)

    def postorder(self, root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data)

if __name__ == '__main__':
    tree = BinaryTree()
    tree.add('I', tree.root)
    tree.add('P', tree.root)
    tree.add('M', tree.root)
    tree.add('C', tree.root)
    tree.add('H', tree.root)
    tree.add('S', tree.root)
    print('preorder')
    tree.preorder(tree.root)
    print('inorder')
    tree.inorder(tree.root)
    print('postorder')
    tree.postorder(tree.root)