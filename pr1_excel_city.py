import mysql.connector

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
keys = y[0].keys()
print(list(keys))


a = dbku.cursor()
a.execute('select * from city')
b = list(a)

import xlrd
import xlsxwriter
book = xlsxwriter.Workbook('pr1_excel_city.xlsx')
sheet = book._add_sheet('sheet 1')

row = 0
for f, g, h, i, j in y:
    sheet.write(row, 0, f)
    sheet.write(row, 1, g)
    sheet.write(row, 2, h)
    sheet.write(row, 3, i)
    sheet.write(row, 4, j)
row = 1
for f, g, h, i, j in b:
    # print(ccode, lang, isoff, pct)
    sheet.write(row, 0, f)
    sheet.write(row, 1, g)
    sheet.write(row, 2, h)
    sheet.write(row, 3, i)
    sheet.write(row, 4, j)
    row +=1
book.close()




