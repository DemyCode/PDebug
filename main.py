import sys

from tracer import Tracer


def quicksort(l):
    if len(l) <= 1:
        return l
    left = [x for x in l[1:] if x < l[0]]
    right = [x for x in l[1:] if x >= l[0]]
    return quicksort(left) + [l[0]] + quicksort(right)


def sub_sub_main():
    return 2


def sub_main():
    return sub_sub_main()


def main():
    quicksort([2, 4, 0, 23, -8, 4])


if __name__ == '__main__':
    tracer = Tracer()
    tracer.activate()
    main()
    tracer.deactivate()
    tracer.tree.prettyprint()
