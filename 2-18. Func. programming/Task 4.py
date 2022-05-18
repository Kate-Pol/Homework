with open('access-log') as wwwlog:
    
    total_requests = len(list( line for line in wwwlog if line.rsplit(maxsplit=2)[1] == '200' ))
    print(total_requests)
