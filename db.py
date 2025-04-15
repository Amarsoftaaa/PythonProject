import pymysql

connection = pymysql.connect(host='localhost',
                             user='root',
                             password='123456',
                             db='lybrary1',)

if connection.open:
    print("Connection established")
else:
    print("Connection failed")