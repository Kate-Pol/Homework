with open('access-log') as wwwlog:
    
    total_requests = len(list( line for line in wwwlog ))
    print(total_requests)
