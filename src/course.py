from not_yet_set_exception import NotYetSetException


class Course:
    PASSING_AVERAGE = 60            # batas rata-rata layak ujian akhir (asumsi)

    def __init__(self, title=""):
        self.__title = title
        self.__course_records = []

    def get_title(self):
        return self.__title

    def set_title(self, title):
        self.__title = title

    def add_course_record(self, cr):
        self.__course_records.append(cr)

    def get_course_records(self):
        return iter(self.__course_records)

    def print_course_students(self):
        """Cetak seluruh mahasiswa yang mengambil course."""
        print(f"Mahasiswa yang mengambil {self.__title}:")
        for cr in self.__course_records:
            print(f"- {cr.get_student().get_name()}")

    def print_best_student(self):
        """Cetak mahasiswa dengan nilai rata-rata terbaik."""
        best, best_avg = None, -1
        for cr in self.__course_records:
            try:
                avg = cr.get_average()
            except NotYetSetException:
                continue
            if avg > best_avg:
                best, best_avg = cr, avg
        if best is None:
            print("Belum ada mahasiswa yang memiliki nilai.")
        else:
            print(f"Mahasiswa terbaik: {best.get_student().get_name()} "
                  f"(rata-rata {best_avg:.2f})")

    def print_final_exam_students(self):
        """Cetak mahasiswa yang layak ujian akhir (rata-rata >= PASSING_AVERAGE)."""
        print("Mahasiswa yang layak ujian akhir:")
        found = False
        for cr in self.__course_records:
            try:
                avg = cr.get_average()
            except NotYetSetException:
                continue
            if avg >= Course.PASSING_AVERAGE:
                print(f"- {cr.get_student().get_name()} (rata-rata {avg:.2f})")
                found = True
        if not found:
            print("(tidak ada)")
