#coding:utf-8
import sys
sys.path.insert(0, "C:\\Users")
sys.path.insert(0, 'C:\\Users\\katep\\mk\\Lib\\site-packages')
sys.stdout.reconfigure(encoding="utf-8")

import cgi
form = cgi.FieldStorage()

import sqlite3
con = sqlite3.connect("C:\\Users\\katep\\chinook.db")
cur = con.cursor()

for i in cur.execute(f'''SELECT FirstName, LastName, Phone, Email FROM customers WHERE CustomerId = {form['cust'].value};'''):
    print(i)

con.close()

print("Content-type: text/html")
print()
print(f"Customer info: Customer Id {form['cust'].value} --- {i}")
