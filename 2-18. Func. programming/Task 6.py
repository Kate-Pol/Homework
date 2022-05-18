with open('access-log') as wwwlog:
    pages200 = list( line for line in wwwlog if line.rsplit(maxsplit=2)[1] == '200' )
    byte_column_1 = ( line.rsplit(maxsplit=1)[1] for line in pages200 )
    byte_sent_1 = ( int(x) for x in byte_column_1 if x != '-' )
    
    print("Code '200' average bytes: ", sum(byte_sent_1)/len(pages200))





with open('access-log') as wwwlog:
    pages404 = list( line for line in wwwlog if line.rsplit(maxsplit=2)[1] == '404' )
    byte_column_2 = ( line.rsplit(maxsplit=1)[1] for line in pages404 )
    byte_sent_2 = ( int(x) for x in byte_column_2 if x != '-' )
    
    print("Code '404' average bytes: ", sum(byte_sent_2)/len(pages404))
