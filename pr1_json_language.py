import mysql.connector
import json

dbku = mysql.connector.connect(
    host = 'localhost',
    port = 3306,
    user = 'wayneuntu', 
    passwd = '***', 
    database = 'world'
)

x = dbku.cursor(dictionary=True)
x.execute('select * from countrylanguage')
y = list(x)

with open("pr1_json_language.json", "w") as jsonku:
    json.dump(y,jsonku)




