import sqlite3
import os

import debug
from debug import logger

# flags 
DEBUG_DATABASE = True

if not DEBUG_DATABASE:
    logger.setLevel(debug.logging.INFO)


current_directory = os.getcwd()
database_name = current_directory + "/" + "pdf.db"

class database:

    column_names = ["FILE_NAME", "CONTENTS", "PATH"]


    def __init__(self):
        
        self.conn = sqlite3.connect(database_name)
        self.conn.text_factory = str
        self.conn.execute('''CREATE TABLE IF NOT EXISTS PDF(
                ID INTEGER PRIMARY KEY NOT NULL,
                FILE_NAME TEXT NOT NULL UNIQUE,
                CONTENTS TEXT NOT NULL,
                PATH TEXT NOT NULL
        );
        ''')


    def __enter__(self):
        return self

    def insert_row(self, file_name, contents, path):

        row_data = [file_name, contents, path]

        self.conn.execute("INSERT INTO PDF (FILE_NAME ,CONTENTS ,PATH) VALUES (?,?,?);", (file_name, contents, path))
        self.conn.commit()


    def check_if_exists(self, table, column, entry):
        # this could probably be combined with search
        entry = (entry,)
        cursor = self.conn.execute("SELECT * FROM " + table + " WHERE " + column + "=?", entry)
        result = cursor.fetchone()
        if result is not None:
            return True
        else:
            return False

    def search(self, table, column, query):

        rows = []
        
        command = \
        "SELECT *" +\
        " FROM " + table +\
        " WHERE instr(" + column + ", " + "'" + query + "'" + ");"

        logger.debug("Search query: \n%s" % command)
        cursor = self.conn.execute(command)
        for row in cursor:
            rows.append(row)

        print rows
        return rows

    def print_rows(self):
        cursor = self.conn.execute("SELECT ID, FILE_NAME, CONTENTS, PATH FROM PDF")
        for row in cursor:
            print str(row[0]) + " " + row[1] + " " + row[2] + " " + row[3]

    def get_rows(self):
        cursor = self.conn.execute("SELECT ID, FILE_NAME, CONTENTS, PATH FROM PDF")
	return cursor

    def __exit__(self, exc_type, exc_value, traceback):
        self.conn.close()

