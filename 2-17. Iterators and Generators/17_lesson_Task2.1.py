class GreatNumerator:
    def __init__(self, lists):
        self.lists = lists    
    
    def __iter__(self):
        return GreatIterator(self.lists)
    
class GreatIterator:
    def __init__(self, l):
        self.l = l.copy() 
        self.n = -1
    
    def __next__(self):
        if len(self.l) > 0:            
            self.n += 1
            k = self.l.pop(0)
            return f'{self.n} {k}'
        else: 
            raise StopIteration
       
    
lists = ['111', 'cat', 'got', 'ddd', '222']
t = GreatNumerator(lists)
for i in t:
    print(i)
    
print(t.lists)
    