with open('access-log') as wwwlog:
    bytes_total = ( line.rsplit(maxsplit=1)[1] for line in wwwlog )
    byte_int = ( int(x) for x in bytes_total if x != '-' )
    print('Total bytes: ', sum(byte_int))


with open('access-log') as wwwlog:
    pages200 = ( line for line in wwwlog if line.rsplit(maxsplit=2)[1] == '200' )
    byte_column = ( line.rsplit(maxsplit=1)[1] for line in pages200 )
    byte_sent = ( int(x) for x in byte_column if x != '-' )
    print("Code '200' bytes: ", sum(byte_sent))
