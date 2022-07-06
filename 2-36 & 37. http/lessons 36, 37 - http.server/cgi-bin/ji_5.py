#coding:utf-8
import sys
sys.path.insert(0, "C:\\Users")
sys.path.insert(0, 'C:\\Users\\katep\\mk\\Lib\\site-packages')
sys.stdout.reconfigure(encoding="utf-8")

import jinja2 as j2

name = ['DED', 'MEDVED', 'NE_MEDVED', 'MEDVED-1', 'MEDVED-2']
template = j2.Template(open('tmpl_5.txt').read())


print("Content-type: text/html")
print()

print(template.render(medveds = name))
