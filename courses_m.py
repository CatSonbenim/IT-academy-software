"""Program by @CatSonbenim (Lisa Bulala) 10.11.2018"""

from abc import ABCMeta, abstractmethod
from datetime import date


class Teacher(metaclass=ABCMeta):

    @abstractmethod
    def get_name(self):
        raise NotImplementedError

    @abstractmethod
    def get_all_courses(self):
        raise NotImplementedError

    @abstractmethod
    def ITeacher(self):
        raise NotImplementedError

    @abstractmethod
    def __str__(self):
        raise NotImplementedError


class Courses(metaclass=ABCMeta):

    @abstractmethod
    def get_name(self):
        raise NotImplementedError

    @abstractmethod
    def get_date(self):
        raise NotImplementedError

    @abstractmethod
    def get_program(self):
        raise NotImplementedError

    @abstractmethod
    def ICourse(self):
        raise NotImplementedError

    @abstractmethod
    def __str__(self):
        raise NotImplementedError


class LocalCourses(Courses, metaclass=ABCMeta):

    @abstractmethod
    def ILocalCourse(self):
        raise NotImplementedError


class OffsiteCourses(Courses, metaclass=ABCMeta):

    @abstractmethod
    def IOffsiteCourse(self):
        raise NotImplementedError


class Factory(Courses, metaclass=ABCMeta):

    @abstractmethod
    def get_teacher(self):
        raise NotImplementedError

    @abstractmethod
    def ICourseFactory(self):
        raise NotImplementedError


class CourseFactory(Factory):

    def __init__(self, course, *teachers):
        self.teachers = []
        for i in range(len(teachers)):
            self.teachers.append(teachers[i]())
        self.course = course()
        for i in teachers:
            i.courses.append(self.course.get_name())

    def get_name(self):
        return self.course.get_name()

    def get_teacher(self):
        s = ''
        for i in self.teachers:
            s = s + i.get_name() + '\n'
        return s

    def get_date(self):
        return self.course.get_date()

    def get_program(self):
        return self.course.get_program()

    def ICourse(self):
        return self.course.ICourse()

    def ICourseFactory(self):
        pass

    def __str__(self):
        return self.get_name() + '\nTeacher: ' + self.get_teacher() + '\nDate: ' + str(self.get_date()) + '\n\n' \
               + self.get_program()


class Timchuck(Teacher):

    courses = []

    def get_name(self):
        return 'Timchuk Oleg Sergeevich'

    def get_all_courses(self):
        c = ''
        for i in Timchuck.courses:
            c = c + i + '\n'
        return c

    def ITeacher(self):
        pass

    def __str__(self):
        return 'Timchuk O.S.\nCourses: ' + self.get_all_courses()


class Matsetska(Teacher):

    courses = []

    def get_name(self):
        return 'Matsetska Natalia Arturovna'

    def get_all_courses(self):
        c = '\n'
        for i in Matsetska.courses:
            c = c + i + '\n'
        return c

    def ITeacher(self):
        pass

    def __str__(self):
        return 'Matsetska N.A.\nCourses: ' + self.get_all_courses()


class Nicoluck(Teacher):

    courses = []

    def get_name(self):
        return 'Nicoluck Petro Karpovich'

    def get_all_courses(self):
        c = '\n'
        for i in Nicoluck.courses:
            c = c + i + '\n'
        return c

    def ITeacher(self):
        pass

    def __str__(self):
        return 'Nicoluck P.K.\nCourses: ' + self.get_all_courses()


class EpamCourse(LocalCourses):

    def get_name(self):
        return 'EpamCourse: Python OOP'

    def get_date(self):
        dat = date(2019, 2, 6)
        return '%d.%d.%d' % (dat.day, dat.month, dat.year)

    def get_program(self):
        return 'Program:\n' \
               '1. Object-oriented programming\n' \
               '2. Encapsulation\n' \
               '3. Inheritance\n' \
               '4. Polymorphism\n'

    def ICourse(self):
        return self.ILocalCourse()

    def ILocalCourse(self):
        pass

    def __str__(self):
        return self.get_name() + '\nDate of beginning:' + str(self.get_date()) + '\n\n' + self.get_program()


class ExcadelCourse(LocalCourses):

    def get_name(self):
        return 'ExcadelCourse: Java OOP'

    def get_date(self):
        dat = date(2019, 4, 5)
        return '%d.%d.%d' % (dat.day, dat.month, dat.year)

    def get_program(self):
        return 'Program:\n' \
               '1. Object-oriented programming\n' \
               '2. Encapsulation\n' \
               '3. Inheritance\n' \
               '4. Polymorphism\n'

    def ICourse(self):
        return self.ILocalCourse()

    def ILocalCourse(self):
        pass

    def __str__(self):
        return self.get_name() + '\nDate of beginning:' + str(self.get_date()) + '\n\n' + self.get_program()


all_courses = ['EpamCourse: Python OOP', 'ExcadelCourse: Java OOP']
