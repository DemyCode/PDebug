import sys


class Tree:
    def __init__(self, value: str = None, children=None):
        self.value = value
        if children is None:
            self.children = []

    def insert(self, value, n):
        if n == 0:
            self.children.append(Tree(value=value))
        else:
            self.children[-1].insert(value, n - 1)

    def prettyprint(self, spacing=0):
        print(' ' * spacing + self.value)
        for child in self.children:
            child.prettyprint(spacing=spacing + 1)


class Tracer:
    def __init__(self):
        self.tree = Tree('activate')
        self.deepness = 0
        self.tracefunc = sys.gettrace()

    def activate(self):
        def printer(frame, event, args):
            # print(self.deepness)

            if event == 'call':
                self.tree.insert(value=frame.f_code.co_name, n=self.deepness)
                self.deepness += 1

            if event == 'return':
                self.deepness -= 1

            return printer

        sys.settrace(printer)

    def deactivate(self):
        sys.settrace(self.tracefunc)
