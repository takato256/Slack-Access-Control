import sqlite3

conn=sqlite3.connect("Member.db", isolation_level=None)

c=conn.cursor()
c.execute("SELECT * FROM SecMember")

print("-----SecMember Table-----")
for row in c:
    print(row)

conn.close()
