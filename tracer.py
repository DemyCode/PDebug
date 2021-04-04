import sys
import json
import time

class Tree:
    def __init__(self, value = None, children = None):
        self.value = value
        if children is None:
            self.children = []

    def insert(self, value, n):
        if n <= 0:
            self.children.append(Tree(value=value))
            return self.children[-1]
        else:
            return self.children[-1].insert(value, n - 1)

    def prettyprint(self, spacing=0):
        print('  ' * spacing + str(self.value))
        for child in self.children:
            child.prettyprint(spacing=spacing + 1)
        
    def serialize(self):
        # TODO
        pass

class Tracer:
    def __init__(self):
        self.tree = Tree({
            'function' : 'activate',
            'parameters' : [],
            'parameters_values' : [],
            'return_values' : []
        })
        self.deepness = 0
        self.tracefunc = sys.gettrace()
        self.currenttree = []

    def activate(self):
        def printer(frame, event, args):
            
            if event == 'call':
                value = {
                    'function' : frame.f_code.co_name,
                    'parameters' : [frame.f_code.co_varnames for i in range(frame.f_code.co_argcount)],
                    'parameters_values' : [frame.f_locals[frame.f_code.co_varnames[i]] for i in range(frame.f_code.co_argcount)],
                    'return_values' : [],
                    'time' : time.time()
                }
                self.currenttree.append(self.tree.insert(value=value, n=self.deepness))
                self.deepness += 1

            elif event == 'return':
                self.deepness -= 1
                self.currenttree[-1].value['time'] = time.time() - self.currenttree[-1].value['time']
                self.currenttree[-1].value['return_values'] = args
                self.currenttree.pop(-1)

            return printer

        sys.settrace(printer)

    def deactivate(self):
        sys.settrace(self.tracefunc)
    
    def prettyprint(self):
        self.tree.prettyprint()

    def serialize(self):
        self.tree.serialize()