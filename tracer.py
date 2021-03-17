import sys


class Tree:
    def __init__(self, value, children: list):
        self.value = value
        self.children = children


class Tracer:
    def __init__(self, function_names='', function_filter='exclude'):
        self.digraph = 'digraph G { \n'
        self.gid = 0
        self.linker = []
        self.function_names = function_names
        self.function_filter = function_filter
        self.memtree = None
    
    def activate():
        def printer(frame, event, args):
            passing = (function_filter == 'include' and frame.f_code.co_name in self.function_names) or \
                    (function_filter == 'exclude' and not frame.f_code.co_name in self.function_names)
            if event == 'call':
                self.gid += 1
                if passing:
                    self.linker.append([self.gid, ''])
                    self.linker[-1][1] = '{} [ label = " NAME : {}\nARGS : '.format(self.gid, frame.f_code.co_name)
                    for i in range(frame.f_code.co_argcount):
                        name = frame.f_code.co_varnames[i]
                        self.linker[-1][1] += '{} '.format(frame.f_locals[name])
                    self.linker[-1][1] += '\n'

            if passing and event == 'return':
                self.linker[-1][1] += 'REVS : {} " ] ;\n'.format(args)
                if len(self.linker) >= 2:
                    self.linker[-1][1] += '{} -> {} ;\n'.format(self.linker[-2][0], self.linker[-1][0])
                self.digraph += self.linker[-1][1]
                self.linker.pop(-1)
            return printer

        sys.settrace(printer)

    def save(self):
        sys.settrace(None)
        self.digraph += '}'
        f = open('digraph.txt', 'w')
        for c in self.digraph:
            f.write(c)
        f.close()
