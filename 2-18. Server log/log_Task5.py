with open('red_apple_2.log') as wwwlog:

    total_lines = len(list( line for line in wwwlog if line.rsplit(maxsplit=2)[1] == '404' ))
    print(total_lines)
