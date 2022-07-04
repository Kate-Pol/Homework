#coding:utf-8

import sys
sys.path.insert(0, "C:\\Users")
sys.path.insert(0, 'C:\\Users\\katep\\mk\\Lib\\site-packages')
sys.stdout.reconfigure(encoding="utf-8")

cust = []
import sqlite3
con = sqlite3.connect("C:\\Users\\katep\\chinook.db")
cur = con.cursor()
for i in cur.execute('''SELECT LastName FROM customers;'''):
    cust.append(i[0])
    
con.close()

from mako.template import Template
t = Template(filename = "C:\\Users\\katep\\html_hw\\tmpl\\cus_table.html")

print("Content-type: text/html")
print()
print(t.render(customers = cust))
