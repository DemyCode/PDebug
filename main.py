import sys

from tracer import Tracer

class Fraction:
    def __init__(self, num, denum):
        self.num = num
        self.denum = denum

    def __add__(self, rhs):
        return Fraction(self.num * rhs.denum + rhs.num * self.denum, self.denum * rhs.denum)

    def __str__(self):
        return '({}/{})'.format(self.num, self.denum)

def adder(a, b, c, d):
    return Fraction(a, b) + Fraction(c, d)


def quicksort(l):
    if len(l) <= 1:
        return l
    left = [x for x in l[1:] if x < l[0]]
    right = [x for x in l[1:] if x >= l[0]]
    return quicksort(left) + [l[0]] + quicksort(right)


def sub_sub_main():
    return 2


def sub_main(a, b):
    return sub_sub_main()

def main():
    print(adder(1, 2, 1, 2))
    print(quicksort([0, 12, -5, 6, 24, 3, 1]))

import time

if __name__ == '__main__':
    tracer = Tracer()
    tracer.activate()
    main()
    main()
    tracer.deactivate()
    tracer.tree.prettyprint()