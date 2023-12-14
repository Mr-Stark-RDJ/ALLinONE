import mysql.connector as ms
import csv
import pickle
data = [["Rno", "Name", "Marks"]]
ch = "Y"

#INPUT DATA

while ch == "Y" or ch == "y":
    Rno = int(input("Enter Roll No. :- "))
    Name = input("Enter Name :- ")
    Marks = int(input("Enter Marks :- "))
    a = [Rno, Name, Marks]
    data.append(a)
    ch = input("Any more data (Y/N) ? :- ")

#STORING IN TEXT

with open("students.txt", "w") as f:
    for i in data:
        f.write(','.join(map(str, i)) + '\n')

# STORING IN CSV

with open("students.csv", "w", newline='') as c:
    wr = csv.writer(c,delimiter = ",")
    wr.writerows(data)

#STORING IN BINARY


with open("students.bin", "wb") as b:
    pickle.dump(data, b)

#STORING IN MySQL
    
db = ms.connect(host="localhost", user="root", passwd="6667", database="new")
cr = db.cursor()
cr.execute("CREATE TABLE STUDENTS(RollNo INT(4), Name Varchar(20), Marks INT(5));")
for i in range(1, len(data)):
    cr.execute("INSERT INTO STUDENTS (RollNo, Name, Marks) VALUES (%s, %s, %s)", tuple(data[i]))
db.commit()

#PRINTING THE DATA


p = input("Do you want to print data? (Y/N): ")
if p.lower() == "y":
    print('''
    1.) Text File
    2.) CSV File
    3.) Binary File
    4.) MySQL
    Choose from [1, 2, 3, 4]: 
    ''')
    cd = input()

    #PRINTING IN TEXT

    if cd == "1":
        with open("students.txt", "r") as f:
            for line in f:
                print(line.strip())

    #PRINTING IN CSV


    elif cd == "2":
        with open("students.csv", "r", newline='') as c:
            reader = csv.reader(c)
            for row in reader:
                print(row)

    #PRINTING IN BINARY


    elif cd == "3":
        with open("students.bin", "rb") as b:
            try:
                while True:
                    print(pickle.load(b))
            except EOFError:
                pass

    #PRINTING IN MySQL

    
    elif cd == "4":
        cr.execute("SELECT * FROM STUDENTS")
        results = cr.fetchall()
        for row in results:
            print(row)
db.close()
