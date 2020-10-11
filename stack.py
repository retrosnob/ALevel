class Stack1:
    def __init__(self, maxitems):
        self._stack = []
        self._maxitems = maxitems

    def push(self, item):
        if not self.isfull():
            self._stack.append(item)

    def pop(self):
        if not self.isempty():
            return self._stack.pop()

    def isempty(self):
        return len(self._stack) == 0

    def isfull(self):
        return len(self._stack) == self._maxitems


class Stack2:
    class StackEntry:
        def __init__(self, item):
            self.item = item
            self.nextentry = None

    def __init__(self, maxitems):
        self._itemcount = 0
        self._top = None
        self._maxitems = maxitems

    def push(self, item):
        if not self.isfull():
            entry = self.StackEntry(item)
            entry.nextentry = self._top
            self._top = entry
            self._itemcount += 1

    def pop(self):
        if not self.isempty():
            entry = self._top
            self._top = self._top.nextentry
            return entry.item

    def isempty(self):
        return self._itemcount == 0

    def isfull(self):
        return self._itemcount == self._maxitems

if __name__ == '__main__':
    s = Stack1(10)
    s.push(23)
    s.push(65)
    s.push(89)
    s.push(34)
    s.push(91)
    print(s.pop())
    print(s.pop())

    s = Stack2(10)
    s.push(23)
    s.push(65)
    s.push(89)
    s.push(34)
    s.push(91)
    print(s.pop())
    print(s.pop())