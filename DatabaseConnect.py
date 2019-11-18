# PROGRAM DatabaseConnect:

import mysql.connector    
cnx = mysql.connector.connect(host='localhost', database='SampleDB',
                              user='root', password='password')

cursor = cnx.cursor()
cursor.execute(""" select * from StudentRecords """)
result = cursor.fetchall()
print(result)
cnx.close()

# END DatabaseConnect.
