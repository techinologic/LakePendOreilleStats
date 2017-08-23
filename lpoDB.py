import sqlite3

__version__ = '0.3.2'


class lpoDB():
    def __init__(self, **kwargs):
        self.filename = kwargs.get('filename', 'lpo.db')
        self.table = kwargs.get('table', 'Weather')
        self.db = sqlite3.connect(self.filename)
        self.db.row_factory = sqlite3.Row
        self.db.execute(
            '''CREATE TABLE IF NOT EXISTS {} (Date TEXT, Time TEXT, Status TEXT, Air_Temp FLOAT, Barometric_Press FLOAT, Wind_Speed FLOAT)'''.format(
                self.table)

    def __iter__(self):
        """
        Return generator object with dicts of entire DB contents
        """
        cursor = self.db.execute('SELECT * FROM {} ORDER BY Date, Time'.format(self.table))
        for row in cursor: yield dict(row)

    def get_data_for_range(self, start, end):
        dates_to_update = []
        for year in range(start.year, 2007):
            if list(self._get_status_for_range(date(year, 1, 12), date(year, 1, 12))) == []:
                dates_to_update.append(date(year, 1, 12))

    def clear(self):
        """
        clears out the database by dropping the current table
        """
        self.db.execute('DROP TABLE IF EXIST {}'.format(self.table))

    def close(self):
        self.db.close()
        del self.filename
