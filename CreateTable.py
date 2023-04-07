import sqlite3

conn = sqlite3.connect("Member.db", isolation_level=None)

sql = """
CREATE TABLE SecMember (
    student_id INTEGER(7),
    name TEXT,
    status TEXT
);
"""

conn.execute(sql)

conn.close()
