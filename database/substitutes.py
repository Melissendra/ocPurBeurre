import records

db = records.Database()


class Substitute:
    def __init__(self, db):
        self.db = db
