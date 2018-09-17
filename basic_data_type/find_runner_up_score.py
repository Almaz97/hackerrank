

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr = list(arr)
    # arr = [2, 3, 6, 6, 5]
    arr.sort()
    maxScore = -2 ** 32
    runnerUpScore = -2 ** 32

    for score in arr:
        if score > maxScore:
            runnerUpScore = maxScore
            maxScore = score

    print(runnerUpScore)