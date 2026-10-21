from student import Student
from assignment import Assignment
from course_record import CourseRecord
from course import Course
from not_yet_set_exception import NotYetSetException


def buat_record(nama, nilai_list):
    cr = CourseRecord(Student(nama))
    for n in nilai_list:
        a = Assignment()
        if n is not None:
            a.set_mark(n)
        cr.add_assignment(a)
    return cr


if __name__ == "__main__":
    course = Course("Implementasi dan Pengujian Sistem Informasi")
    course.add_course_record(buat_record("Ilaria", [80, 90, 85]))
    course.add_course_record(buat_record("Chindy", [55, 60, None]))
    course.add_course_record(buat_record("Ipan", [40, 50, 45]))

    course.print_course_students()
    print()
    course.print_best_student()
    print()
    course.print_final_exam_students()

    # Demo exception handling
    print()
    try:
        Assignment().get_mark()
    except NotYetSetException as e:
        print("Exception tertangkap:", e)
