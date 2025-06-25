def cc(n):
    s = ''
    while n != 0:
        s = str(n % 9) +  s
        n //= 9
    return s

def f(n):
    s = cc(n)
    if s[0] == '7':
        s = s.replace('6','*').replace('3','6').replace('*','3')
        s = '34' + s
    else:
        s += '45'
        s = '3' + s[1:]
    return int(s,9)

#1 способ
a = []
for i in range(1,100000):
    if f(i) <  2876:
        a.append([-f(i),-i])
a.sort()
print(abs(a[0][1]))
#2 способ
max_el = float('-inf')
max_N = 0
for i in range(1,100000):
    if f(i) <  2876:
        if max_el <= f(i):
            max_el = f(i)
            max_N = i
print(max_N)