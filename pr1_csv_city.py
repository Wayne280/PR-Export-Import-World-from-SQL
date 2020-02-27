import mysql.connector
import csv

dbku = mysql.connector.connect(
    host = 'localhost',
    port = 3306,
    user = 'wayneuntu', 
    passwd = '***', 
    database = 'world'
)

x = dbku.cursor(dictionary=True)
x.execute('select * from city')
y = list(x)
print(y[0])

with open('pr1_csv_city.csv', 'w', newline='') as csvku:
    csvmu = csv.DictWriter(csvku, delimiter=",",
    fieldnames = ['ID', 'Name', 'CountryCode', 'District', 'Population'])
    
    csvmu.writeheader()
    csvmu.writerows(y)




