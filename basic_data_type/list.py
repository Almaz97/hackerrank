

if __name__ == '__main__':
    N = int(input())

    li = []
    for i in range(N):
        inp = str(input())
        command = inp.split()
        if command[0] == "insert":
            li.insert(int(command[1]), int(command[2]))
        elif command[0] == "print":
            print(li)
        elif command[0] == "remove":
            li.remove(int(command[1]))
        elif command[0] == "append":
            li.append(int(command[1]))
        elif command[0] == "sort":
            li.sort()
        elif command[0] == "pop":
            li.pop()
        else:
            li.reverse()

