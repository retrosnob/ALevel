class LinkedList:

    class Node:
        def __init__(self, item, nxt):
            self.item = item
            self.nxt = nxt

    def __init__(self):
        self.head = None

    def add(self, item):
        if self.head is None:
            self.head = LinkedList.Node(item, self.head)
        else:
            p = LinkedList.Node(item, self.head)
            self.head = p

    def print(self):
        p = self.head
        while p is not None:
            print(p.item)
            p = p.nxt
