

if __name__ == '__main__':
    s = input()

    isalnum = False
    isalpha = False
    isdigit = False
    islower = False
    isupper = False

    for char in s:
        if char.isalnum():
            isalnum = True
        if char.isalpha():
            isalpha = True
        if char.isdigit():
            isdigit = True
        if char.islower():
            islower = True
        if char.isupper():
            isupper = True

    if isalnum is True:
        print(True)
    else:
        print(False)

    if isalpha is True:
        print(True)
    else:
        print(False)

    if isdigit is True:
        print(True)
    else:
        print(False)

    if islower is True:
        print(True)
    else:
        print(False)

    if isupper is True:
        print(True)
    else:
        print(False)