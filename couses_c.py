import courses_m as cm
import courses_v as cv


def main():
    choose = cv.what_course()
    courses = {1: cm.CourseFactory(cm.EpamCourse, cm.Timchuck, cm.Matsetska), 2: cm.CourseFactory(cm.ExcadelCourse,
                                                                                                  cm.Nicoluck)}
    cv.printing_course(courses[choose])


if __name__ == '__main__':
    main()
