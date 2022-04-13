import mysql.connector

def link_formatter(link):
    if "https://www.youtube.com/watch?v=" in link:
        return link
    else:
        split_link = link.split('/')
        return "https://www.youtube.com/watch?v=" + split_link[-1]

# local so idgaf 
mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="Garter242@#",
    database="activities",
)

cursor = mydb.cursor(buffered=True)
cursor.execute('SELECT * FROM activities.tbl_activity_master;')
row = cursor.fetchone()
update_sql = """UPDATE activities.tbl_activity_master SET video = %s WHERE id = %s"""
while row:
    cursor2 = mydb.cursor()
    list_row = list(row)
    cursor2.execute(update_sql, (link_formatter(list_row[4]), list_row[0]))
    mydb.commit()
    row = cursor.fetchone()

mydb.commit()
