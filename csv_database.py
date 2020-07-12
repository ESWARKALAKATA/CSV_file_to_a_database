#!/usr/bin/python
import csv
import psycopg2
import sys

#open the source csv file
fd = open('users-data.csv', 'rt')

#reading data from csv
reader = csv.reader(fd)

#connecting to database
conn = None
conn = psycopg2.connect( database="gcontacts", user="uaura", host="127.0.0.1", password="jnjnuh")
cur = conn.cursor()

#insert each row of csv file and add to database
i = 0

for row in reader:
    if (i == 0):
        i = 1
        continue

    
    print("===", row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8])
    cur.execute("INSERT INTO students_list(name, fullname, uid, gid, phone, hphone, address, email, status) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", 
        (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], "1"))

conn.commit()

#closing csv
fd.close()

cur.execute("SELECT * FROM students_list")
rows = cur.fetchall()
