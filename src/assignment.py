from not_yet_set_exception import NotYetSetException


class Assignment:
    def __init__(self):
        self.__mark = -1            # -1 artinya nilai belum di-set

    def get_mark(self):
        if self.__mark == -1:
            raise NotYetSetException("Mark is not yet set")
        return self.__mark

    def set_mark(self, mark):
        self.__mark = mark
