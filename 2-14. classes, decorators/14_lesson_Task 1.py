class Employee():
    
    def __init__(self, name, status, salary, pay_basis, position_title):
        self.name = name
        self.status = status
        self.pay_basis = pay_basis
        self.position_title = position_title
        
class WH():
    
    f = open('white_house_2017_salaries_com.csv', 'r', encoding='utf-8')
    t = f.readlines()
    f.close()

    headers = t[0].strip().split(';')
    print(headers)

    def original_lst(self):
        hr = []
        for i in t[1:]:
            s = i.split(';')
            k = {}
            for n,h in enumerate(headers):
                if h == 'SALARY':
                    k[h] = float(s[n].replace('$','').replace(',',''))
                else: 
                    k[h] = s[n].strip()
            hr.append(k)
            return hr

    def sort_list(self):
        global hr
        names = []
        for h in hr:
            if h['NAME'] == True:
                print(h['NAME'])
    
    def aver_salary(self):
        global hr
        for h in hr:
            if h['POSITION TITLE,,,,'] == 'STAFF ASSISTANT,,':
                summa += h['SALARY']
                aver_sum = summa/len(hr)
                return aver_sum
            
    def higher_salaries(self):
        global hr
        for h in hr:
            if h['SALARY'] > 0.0:
                higher_lst = heapq.nlargest(10, zip(h['SALARY']))
                return higher_lst
            
    def detailee(self):
        global hr
        for h in hr:
            if h['STATUS'] == 'Detailee':
                print(h['\ufeffID'], h['NAME']) 
            
    def staff_aver(self):
        global hr
        for h in hr:
            if h['POSITION TITLE,,,,'] == 'STAFF ASSISTANT,,':
                summa += h['SALARY']
                print(summa/len(hr))
        

wh = WH()
wh.detailee()
