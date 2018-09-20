

def print_formatted(number):
    # your code goes here
    n = str(bin(number))
    n = n[2:]
    nlen = len(n)
    for i in range(1, number+1):
        o = str(oct(i))
        o = o[2:]
        h = str(hex(i))
        h = h[2:]
        b = str(bin(i))
        b = b[2:]

        print("{:>{}} {:>{}} {:>{}} {:>{}}".format(i, nlen, o, nlen, h.upper(), nlen, b, nlen))


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
