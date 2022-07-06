#coding:utf-8
import sys
sys.path.insert(0, "C:\\Users")
sys.path.insert(0, 'C:\\Users\\katep\\mk\\Lib\\site-packages')
sys.stdout.reconfigure(encoding="utf-8")

import jinja2 as j2

f = open('tmpl.txt', 'r')
tmpl = f.read()
f.close()

template = j2.Template(tmpl)

print("Content-type: text/html")
print()

print(template.render(name='MEDVED'))
