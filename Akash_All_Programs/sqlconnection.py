import pyodbc

server = '20.20.1.20'
database = 'X941Q1_DERIVE'
username = 'aurade'
password = 'Admin@1234'


conn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
def read(conn):
    print("Read")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM COST_CENTER_MASTER")
    for row in cursor:
        print(row)
        print()
read(conn)
