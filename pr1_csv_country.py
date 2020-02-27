import mysql.connector
import csv

dbku = mysql.connector.connect(
    host = 'localhost',
    port = 3306,
    user = 'wayneuntu', 
    passwd = '****', 
    database = 'world'
)

x = dbku.cursor(dictionary=True)
x.execute('select * from country')
y = list(x)
print(y[0])

with open('pr1_csv_country.csv', 'w', newline='') as csvku:
    csvmu = csv.DictWriter(csvku, delimiter=",",
    fieldnames = ['Code', 'Name', 'Continent', 'Region', 'SurfaceArea', 'IndepYear', 'Population', 'LifeExpectancy', 'GNP', 'GNPOld', 'LocalName', 'GovernmentForm', 'HeadOfState', 'Capital', 'Code2'])
    csvmu.writeheader()
    csvmu.writerows(y)




