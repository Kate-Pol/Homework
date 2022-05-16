# 1.1 Task
def gen(N): 
    for i in range(N):
        yield str(i)
    
k = gen(10)
print([i for i in k])


# 1.4 Task
def gen(N):
    new_lst = [x for x in N if (x.isdigit())] 
    yield new_lst
    

k = gen(['111', 'cat', 'got', 'ddd', '222'])
print([i for i in k])


# 1.5 Task
def gen(N):
    new_lst = []
    new_lst.append(i for i in enumerate(N) if i.isdigit())
    yield new_lst
    
k = gen(['111', 'cat', 'got', 'ddd', '222'])
print([i for i in k])


# 1.6 Task
def gen(N):
    new_lst = list(({ind: i for ind, i in enumerate(N) if i.isdigit()}).items())
    yield new_lst
    
k = gen(['111', 'cat', 'got', 'ddd', '222'])
print([i for i in k])
