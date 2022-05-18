with open('access-log') as wwwlog:
    
    lines = ( line for line in wwwlog )
    ip_list = [ int(line.split()[0].replace('.', '')) for line in lines ]
    
    unique_ip = []
    for i in ip_list: 
        if i not in unique_ip:
            unique_ip.append(i)
            
    print("List of unique ip's: ", (unique_ip))                # Task 7
    print("Total count of unique ip's: ", (len(unique_ip)))    # Task 8
