class Person:
    
    count = 0
    staff = 0
    all_salary = 0
    
    def __init__(self, name, status, salary, pay_basis, position_title):
        self.name = name
        self.status = status
        self.salary = salary
        self.pay_basis = pay_basis
        self.position_title = position_title
        self.__class__.count += 1
        self.__class__.all_salary += self.salary
        if self.status != 'Detailee':
            self.__class__.staff += 1
        
    def __del__(self):
        self.__class__.count -= 1
        self.__class__.all_salary -= self.salary
        if self.status != 'Detailee':
            self.__class__.staff -= 1

    def __repr__(self):
        return self.name

    
class WH:
    def __init__(self, name_file):
        self.sotr = []
        self.titles = []
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
            self.titles.append(sp[4])  #added one more list for titles for titles counting
    
    def recount(self):
        su = 0
        for s in self.sotr:
            su += s.salary
        Person.all_salary = su
         
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
    
    def staff_aver_salary(self):         # this method was not completed from 05.07
        su_2 = 0
        staff_count = len([i for i in self.sotr if i.position_title == 'STAFF ASSISTANT' ])
        for s in self.sotr:
            if s.position_title == 'STAFF ASSISTANT':
                su_2 += s.salary
        return su_2/staff_count            
        
    def rep(self):
        for i in self.sotr:
            print(i)
    
    def count_sotr(self):
        print(f'Total {Person.count} with full-time employees in total {Person.staff}, combined salary is {Person.all_salary}')
            
        
    def posit_titles(self):              # this method was not completed from 05.07
        titles_lst = []  
        for i in self.titles:
            if i not in titles_lst:
                titles_lst.append(i)
        print(titles_lst)
        print(f'Total count of the position titles: {len(titles_lst)}')

    def people_with_title(self):          # this method was not completed from 05.07
        people_count_dict = {i : self.titles.count(i) for i in self.titles}
        print(people_count_dict)

    
wh = WH('white_house_2017_salaries_com.csv')
#wh.rep()

print(wh.sotr[3], wh.sotr[3].salary, type(wh.sotr[3].salary))
print(wh.top10())
for i in wh.top10():
    print(i.name , i.salary)

print(wh.detailees())
print(wh.staff())

wh.count_sotr()

del wh.sotr[4:300]
print(len(wh.sotr))
wh.count_sotr()

print(wh.staff_aver_salary())

print(wh.posit_titles())

print(wh.people_with_title())




