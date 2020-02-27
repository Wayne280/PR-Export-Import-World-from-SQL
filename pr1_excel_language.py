import mysql.connector

dbku = mysql.connector.connect(
    host = 'localhost',
    port = 3306,
    user = 'wayneuntu', 
    passwd = '***', 
    database = 'world'
)

x = dbku.cursor(dictionary=True)
x.execute('select * from countryLanguage')
y = list(x)
keys = y[0].keys()
print(list(keys))


a = dbku.cursor()
a.execute('select * from countryLanguage')
b = list(a)

import xlrd
import xlsxwriter
book = xlsxwriter.Workbook('pr1_excel_language.xlsx')
sheet = book._add_sheet('sheet 1')

row = 0
for CountryCode, Language, IsOfficial, Percentage in y:
    sheet.write(row, 0, CountryCode)
    sheet.write(row, 1, Language)
    sheet.write(row, 2, IsOfficial)
    sheet.write(row, 3, Percentage)
row = 1
for CountryCode, Language, IsOfficial, Percentage in b:
    # print(ccode, lang, isoff, pct)
    sheet.write(row, 0, CountryCode)
    sheet.write(row, 1, Language)
    sheet.write(row, 2, IsOfficial)
    sheet.write(row, 3, Percentage)
    row +=1
book.close()




