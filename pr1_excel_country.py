import mysql.connector

dbku = mysql.connector.connect(
    host = 'localhost',
    port = 3306,
    user = 'wayneuntu', 
    passwd = 'Kadalapi280', 
    database = 'world'
)

x = dbku.cursor(dictionary=True)
x.execute('select * from country')
y = list(x)
keys = y[0].keys()
print(list(keys))


a = dbku.cursor()
a.execute('select * from country')
b = list(a)

import xlrd
import xlsxwriter
book = xlsxwriter.Workbook('pr1_excel_country.xlsx')
sheet = book._add_sheet('sheet 1')

row = 0
for f, g, h, i, j, k, l, m, n, o, p, q, r, s, t in y:
    sheet.write(row, 0, f)
    sheet.write(row, 1, g)
    sheet.write(row, 2, h)
    sheet.write(row, 3, i)
    sheet.write(row, 4, j)
    sheet.write(row, 5, k)
    sheet.write(row, 6, l)
    sheet.write(row, 7, m)
    sheet.write(row, 8, n)
    sheet.write(row, 9, o)
    sheet.write(row, 10, p)
    sheet.write(row, 11, q)
    sheet.write(row, 12, r)
    sheet.write(row, 13, s)
    sheet.write(row, 14, t)
row = 1
for f, g, h, i, j, k, l, m, n, o, p, q, r, s, t in b:
    sheet.write(row, 0, f)
    sheet.write(row, 1, g)
    sheet.write(row, 2, h)
    sheet.write(row, 3, i)
    sheet.write(row, 4, j)
    sheet.write(row, 5, k)
    sheet.write(row, 6, l)
    sheet.write(row, 7, m)
    sheet.write(row, 8, n)
    sheet.write(row, 9, o)
    sheet.write(row, 10, p)
    sheet.write(row, 11, q)
    sheet.write(row, 12, r)
    sheet.write(row, 13, s)
    sheet.write(row, 14, t)
    row +=1
book.close()




