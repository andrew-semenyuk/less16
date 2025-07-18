def del_x(a):
    l = len(a)
    read = 0
    write = 0
    while read < l:
        if a[read] != 'x':
            a[write] = a[read]
            read += 1
            write += 1
        else:
            start = read
            while read < l and a[read] == 'x':
                read += 1
            count = read - start
            if count > 2:
                write += 1
                if not read == l:
                    a[write] = a[read]
            else:
                a[write] = 'x'
                write += 1
                if read < l and a[write] == 'x':
                    a[write] = 'x'
                    write += 1
                if read == l and count == 2:
                    a[write] = 'x'
                    write += 1
    del a[write:]
    return (a)

print(del_x(list(input())))