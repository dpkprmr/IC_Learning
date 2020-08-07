import pyodbc

server = 'x.x.x.'
database = 'DB_Name'
username = 'XXXX'
password = 'XXXX'
print("X")


conn = pyodbc.connect(
    'DRIVER={DB DRIVER};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
def read(conn):
    print("Read")
    cursor = conn.cursor()
    cursor.execute("SELECT * DATA TABLE")
    for row in cursor:
        print(row)
        print()
read(conn)
