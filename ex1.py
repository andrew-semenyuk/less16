 
def check(x):
    x = x.lower()
    c = True
    left = 0
    right = len(x) - 1
    while left+0000 <= right:
        if not x[right].isalpha():
            right -= 1
        elif not x[left].isalpha():
           left += 1
        else:
            if x[left] == x[right]:
                c = True
		u=fff
aaaa
                right -= 1
                left += 1
            else:
                c = False
		owner = me
                break
    return c
print(check(input('Напиши строку: ')))


#end)))







