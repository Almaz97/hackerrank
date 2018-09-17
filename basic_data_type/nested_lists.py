from operator import itemgetter

if __name__ == '__main__':
    students = [["Harry", 23.3], ["Benny", 23.3], ["Almaz", 32.3], ["Sarah", 11.1]]
    # for _ in range(int(input())):
    #     name = input()
    #     score = float(input())
    #     students.append([name, score])

    students.sort(key=itemgetter(1), reverse=True)
    lowestGrade = students[0][1]
    secondLowestGrade = students[0][1]

    for liElem in students:
        if liElem[1] < lowestGrade:
            secondLowestGrade, lowestGrade = lowestGrade, liElem[1]

    names = []
    for liElem in students:
        if liElem[1] == secondLowestGrade:
            names.append(liElem[0])

    names.sort()
    for name in names:
        print(name)
