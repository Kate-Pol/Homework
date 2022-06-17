st = ('магистр Йода так говорит поскольку джедай')

def rev(st):
    new_st = st.split()
    if len(new_st) <= 1:
        return new_st
    else: 
        rev_st = list(reversed(new_st))
        print(' '.join(rev_st))

rev(st)
