'''
Return converted degrees 

first example C convert into F

>>> converter('30C')
(86, 'F', '86F')

second example F convert into C

>>> converter('75F')
(24, 'C', '24C')

'''


def converter(T):

    
    measure = T[-1]                 #last elevment is degree scale
    degree = int(T[:-1])            #elevments befor - number - degree digit 
    if measure.upper() == "C":      #if user has degrees in C - we are converting into F
      result = int(round((9 * degree) / 5 + 32))
      out_measure = "F"
    elif measure.upper() == "F":    #if user has degrees in F - we're converting into C
      result = int(round((degree - 32) * 5 / 9))
      out_measure = "C"
    else:
      raise ValueError("Input proper convention")    #raise error in case if wrong input
      
    return result, out_measure, f'{result}{out_measure}'


if __name__ == "__main__":
    import doctest
    doctest.testmod()


