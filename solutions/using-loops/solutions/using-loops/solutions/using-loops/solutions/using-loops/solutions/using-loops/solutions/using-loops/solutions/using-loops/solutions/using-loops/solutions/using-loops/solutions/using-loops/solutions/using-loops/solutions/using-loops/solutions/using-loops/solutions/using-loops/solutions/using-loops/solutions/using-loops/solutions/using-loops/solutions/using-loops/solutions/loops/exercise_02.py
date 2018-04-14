number_of_students = eval(input('Enter the number of students: '))

if number_of_students <= 0:
    print('Invalid number of students')
elif number_of_students == 1:
    highest_score = eval(input(f'Enter student 1\'s score: '))
    print(f'Highest score is {highest_score}.')
else:
    first_score = eval(input(f'Enter student 1\'s score: '))
    second_score = eval(input(f'Enter student 2\'s score: '))

    highest_score = max(first_score, second_score)
    second_highest_score = min(first_score, second_score)

    for i in range(3, number_of_students + 1):
        score = eval(input(f'Enter student {i}\'s score: '))

        if score > highest_score:
            second_highest_score = highest_score
            highest_score = score
        elif score > second_highest_score:
            second_highest_score = score

    print(f'Highest score is {highest_score}.')
    print(f'Second highest score is {second_highest_score}.')
