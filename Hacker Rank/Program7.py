//Nested Lists

if __name__ == '__main__':
    students = []

    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])

    score_list = []

    for student in students:
        score_list.append(student[1])

    lowest = min(score_list)

    final_list = []

    for score in score_list:
        if score != lowest:
            final_list.append(score)

    second_lowest = min(final_list)

    names = []

    for student in students:
        if student[1] == second_lowest:
            names.append(student[0])

    names.sort()

    for name in names:
        print(name)
