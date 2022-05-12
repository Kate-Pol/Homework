class Person:
    def __init__(self, name, status, salary, pay_basis, position_title):
        self.name = name
        self.status = status
        self.salary = salary
        self.pay_basis = pay_basis
        self.position_title = position_title
    def __repr__(self):
        return self.name
    
class WH:
    def __init__(self, name_file):
        self.sotr = []
        self.get_sotr(name_file)
        
    def get_sotr(self, name_file):
        f = open(name_file, 'r', encoding = 'utf-8')
        t = f.readlines()
        f.close()
        for s in t[1:]:
            sp = s.strip().split(';')
            k = sp[2]
            salary = float(k.strip().replace('$','').replace(',',''))
            p = Person(sp[0], sp[1], salary, sp[3], sp[4])
            self.sotr.append(p)
    
    def summa(self):
        su = 0
        for s in self.sotr:
            su += s.salary 
        return su/len(self.sotr)
        
    def top10(self):
        def sal(i):
            return i.salary
        top = self.sotr.copy()
        top2 = sorted(top, key=sal, reverse = True)
        return top2[:10]

    def detailees(self):        
        return [i for i in self.sotr if i.status == 'Detailee' ]
        
    def staff(self):        
        return len([i for i in self.sotr if i.position_title == 'STAFF ASSISTANT' ])
        
    def rep(self):
        for i in self.sotr:
            print(i)
            
        
    
wh = WH('white_house_2017_salaries_com.csv')
wh.rep()
print(wh.sotr[3], wh.sotr[3].salary, type(wh.sotr[3].salary))
print(wh.top10())
for i in wh.top10():
    print(i.name , i.salary)

print(wh.detailees())
print(wh.staff())
