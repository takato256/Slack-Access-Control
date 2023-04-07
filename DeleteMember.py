import sqlite3

conn = sqlite3.connect("Member.db", isolation_level = None)
c = conn.cursor()

c.execute("SELECT * FROM SecMember")

print("-----SecMember Table-----")
for row in c:
    print(row)

student_id = int(input("Input Delete Student_Id:"))
sql = "DELETE FROM SecMember WHERE student_id=?"
data = [(student_id)]

conn.execute(sql, data)
conn.commit()

print("-----SecMember Table-----")
c.execute("SELECT * FROM SecMember")

for row in c:
    print(row)


conn.close()
