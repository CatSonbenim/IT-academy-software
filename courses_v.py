from courses_m import all_courses, CourseFactory


def what_course():
    print('Our courses:')
    for i in range(len(all_courses)):
        print(i+1, '-', all_courses[i], '\n')

    while True:
        try:
            inp = int(input('Info about what course do you whant to see? Enter it\'s number: '))
            if inp-1 not in range(len(all_courses)):
                raise Warning
            break
        except (ValueError, Warning):
            print('Incorrect input. Retry entering!\n')

    return inp


def printing_course(course):
    if type(course) is not CourseFactory:
        raise TypeError('Course has to be <CourseFactory>')
    else:
        print('Info about your course:\n\n', course)