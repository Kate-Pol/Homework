import convert as c
    
assert c.converter('75F') == (24, 'C', '24C')
    
def test_measure(T):
    measure = T[-1] 
    assert measure.upper() == 'C' or measure.upper() == 'F', 'do not equal'
test_measure('30C')


def test_30C(T):
    assert c.converter('30C') == (86, 'F', '86F'), 'need to change number'
test_30C('30C')
