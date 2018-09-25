

from collections import Counter, OrderedDict

class OrderedCounter(Counter, OrderedDict):
    pass


if __name__ == '__main__':
    [print(*c) for c in OrderedCounter(sorted(input())).most_common(3)]