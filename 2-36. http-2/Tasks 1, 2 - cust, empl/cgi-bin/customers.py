#coding:utf-8
import sys
sys.path.insert(0, "C:\\Users")
sys.path.insert(0, 'C:\\Users\\katep\\mk\\Lib\\site-packages')
sys.stdout.reconfigure(encoding="utf-8")


cust = []

import sqlite3
con = sqlite3.connect("C:\\Users\\katep\\chinook.db")
cur = con.cursor()

req = '''SELECT 
            CustomerId, 
            LastName, 
            FirstName, 
            Email,
            SupportRepId 
            FROM customers
            ;'''


for i in cur.execute(req):
    d = {}
    d['CustomerId'] = i[0]
    d['FirstName'] = i[2]
    d['LastName'] = i[1]
    d['Email'] = i[3]
    d['SupportRepId'] = i[4]
    cust.append(d)


    
con.close()

from mako.template import Template
t = Template(filename = "C:\\Users\\katep\\html\\tmpl\\customers.html")
html = t.render(customers = cust)

print("Content-type: text/html")
print()
print(html)
