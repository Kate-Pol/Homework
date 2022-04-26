class Mathematician():
    def square_nums(self, lst):
        lst = [i ** 2 for i in lst]
        return lst
    
    def remove_positives(self, lst):
        lst = [i for i in lst if i > 0]
        return lst
    
    def filter_leaps(self, lst):
        year = []
        for i in lst: 
            if i % 4 == 0:
                year.append(i)
        return year

m = Mathematician()
assert m.square_nums([7, 11, 5, 4]) == [49, 121, 25, 16]
assert m.remove_positives([26, -11, -8, 13, -90]) == [-11, -8, -90]
assert m.filter_leaps([2001, 1884, 1995, 2003, 2020]) == [1884, 2020]
