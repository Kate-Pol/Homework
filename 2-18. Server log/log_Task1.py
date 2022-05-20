with open('red_apple_2.log') as wwwlog:
    

    bytes_total = ( line.rsplit(maxsplit=1)[1] for line in wwwlog )
    byte_int = ( int(x) for x in bytes_total if x.isdigit() )
    total_sum = sum(byte_int)
    print(f'Total bytes: {total_sum}')



with open('red_apple_2.log') as wwwlog:

    pages200 = ( line for line in wwwlog if line.rsplit(maxsplit=2)[1] == '200' )
    byte_column = ( line.rsplit(maxsplit=1)[1] for line in pages200 )
    byte_sent = ( int(x) for x in byte_column if x != '-' )
    total_200 = sum(byte_sent)
    print(f"Code '200' bytes: {total_200}")

