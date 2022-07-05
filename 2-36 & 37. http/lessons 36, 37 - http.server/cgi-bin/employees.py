#coding:utf-8
import sys
sys.path.insert(0, "C:\\Users")
sys.path.insert(0, 'C:\\Users\\katep\\mk\\Lib\\site-packages')
sys.stdout.reconfigure(encoding="utf-8")


empl = []

import sqlite3
con = sqlite3.connect("C:\\Users\\katep\\chinook.db")
cur = con.cursor()

req = '''SELECT 
            EmployeeId, 
            LastName, 
            FirstName, 
            Title,
            Email
            FROM employees
            ;'''


for i in cur.execute(req):
    d = {}
    d['EmployeeId'] = i[0]
    d['LastName'] = i[1]
    d['FirstName'] = i[2]
    d['Title'] = i[3]
    d['Email'] = i[4]
    empl.append(d)


    
con.close()

from mako.template import Template
t = Template(filename = "C:\\Users\\katep\\html\\tmpl\\employees.html")
html = t.render(employees = empl)

print("Content-type: text/html")
print()
print(html)

