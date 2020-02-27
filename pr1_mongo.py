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
x.execute('select * from city')
a = list(x)
print(a[0])

# #for i in a: #CATATAN: Jika data bentuk desimal tidak bisa di export ke mongoDB
#     for j in i:
#         i['masukin index']=float (i['masukin index']) #CATATAN: kalau datanya tidak none
#         if i['masukin index2'] is not None: #CATATAN: kalau datanya ada yang none    
#             i['masukin index2']=float (i['masukin index2'])
           
      
x.execute('select * from country')
b = list(x)
print(b[0])

x.execute('select * from countrylanguage')
c = list(x)
print(c[0])



import pymongo

urldb = "mongodb://localhost:27017"
mongoku = pymongo.MongoClient(urldb)
dbku = mongoku['pr1_mongo_world']
colku1 = dbku['pr1_mongo_city']
colku2 = dbku['pr1_mongo_country']
colku3 = dbku['pr1_mongo_language']

kirim1 = colku1.insert_many(a)
kirim2 = colku2.insert_many(b)
kirim3 = colku3.insert_many(c)




