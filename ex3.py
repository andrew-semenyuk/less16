def make_dict(x):
    y = x.split('\t')
    d = {}
    for i in y:
        if '=' not in i:
            continue
        key, val= i.split(' = ', 1)
        # key = key.strip()
        d[key.strip()] = val
    print(y)
    print('eto d', d)
    return x

print(make_dict('ke=y1 = val1    \t key2 = va l2 \t key3\t key4 = v=al4 \t'))

# ['ke=y1 = val1    ', ' key2 = va l2 ', ' key3', ' key4 = v=al4 ', '']
# eto d {'ke=y1': 'val1    ', ' key2': 'va l2 ', ' key4': 'v=al4 '}
# ke=y1 = val1    	 key2 = va l2 	 key3	 key4 = v=al4