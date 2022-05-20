with open('red_apple_2.log') as wwwlog:

    pages404 = ( line for line in wwwlog if line.rsplit(maxsplit=2)[1] == '404' )
    byte_column = ( line.rsplit(maxsplit=1)[1] for line in pages404 )
    byte_sent = ( int(x) for x in byte_column if x != '-' )
    total_404 = sum(byte_sent)
    print(f"Code '404' bytes: {total_404}")

