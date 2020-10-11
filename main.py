from binarytree import BinaryTree

tree = BinaryTree()
tree.add(50, tree.root)
tree.add(25, tree.root)
tree.add(75, tree.root)
tree.add(33, tree.root)
tree.inorder(tree.root)