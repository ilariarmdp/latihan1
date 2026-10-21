class NotYetSetException(Exception):
    """Dilempar saat nilai (mark) belum di-set."""

    def __init__(self, message):
        super().__init__(message)
