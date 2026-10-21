from not_yet_set_exception import NotYetSetException


class CourseRecord:
    def __init__(self, student=None):
        self.__student = student
        self.__assignments = []

    def get_student(self):
        return self.__student

    def set_student(self, student):
        self.__student = student

    def add_assignment(self, assignment):
        self.__assignments.append(assignment)

    def get_assignments(self):
        return iter(self.__assignments)

    def get_average(self):
        """Rata-rata nilai tugas yang sudah di-set.
        Jika belum ada satu pun nilai, lempar NotYetSetException."""
        marks = []
        for a in self.__assignments:
            try:
                marks.append(a.get_mark())
            except NotYetSetException:
                continue            # tugas yang belum dinilai dilewati
        if not marks:
            raise NotYetSetException("Belum ada nilai yang di-set")
        return sum(marks) / len(marks)
