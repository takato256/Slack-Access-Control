import sqlite3

conn = sqlite3.connect("Member.db", isolation_level = None)

student_id = int(input("Input Student_Id:"))
name = input("Input Name:")
data = (student_id, name, "exit")

sql = "INSERT INTO SecMember (student_id, name, status) VALUES (?, ?, ?)"

conn.execute(sql, data)
conn.commit()

c = conn.cursor()
c.execute("SELECT * FROM SecMember")

print("-----SecMember Table-----")

for row in c:
    print(row)


conn.close()
