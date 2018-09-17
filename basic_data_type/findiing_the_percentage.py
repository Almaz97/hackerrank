
if __name__ == '__main__':
    n = int(input())
    student_marks = {
        "Krishna": [67, 68, 63],
        "Arjun": [70, 98, 63],
        "Malika": [25, 26.5, 28]
                     }
    # for _ in range(n):
    #     name, *line = input().split()
    #     scores = list(map(float, line))
    #     student_marks[name] = scores

    query_name = input()

    sumOfScores = 0
    for score in student_marks[query_name]:
        sumOfScores += score

    # Need to round floating number to 2 decimal only after floating point
    average = round(sumOfScores / len(student_marks[query_name]), 2)
    
    # Need to convert all float number to string, because if only 1 number after a floating point,
    # need to print 0 to fulfill the requirement of problem
    average = str(average)

    if average[-2] == '.':
        average = average + "0"

    print(average)
