#KEGE Kabanov

#7
from math import *


'''alph = 250
i = ceil(log2(alph))
id = ceil(86*i/8)
print(id * 256)
'''
#ans: 22016

#8
'''for dop in range(1,100):
    alph = 2 + 7
    i = ceil(log2(alph))
    id = ceil(20 * i / 8)
    sum = id + 4 + dop
    forUser = 6 * 1024 / 192

    if sum == forUser:
        print(dop)'''
#ans: 18

#9

'''alph = 4090 + 10
i = ceil(log2(alph))
id = ceil(101*i/8)
print(id*2048/1024)'''

#ans: 330

#10
'''for len in range(0,1000):

    alph = 52 + 10 +458
    i = ceil(log2(alph))
    id = ceil(len* i / 8)

    if id <= 276 * 1024 / 862:
        print(len)
'''
#ans: 261

#11
'''for l in range(1000):
    alph = 10 + 26 + 450
    i = ceil(log2(alph))
    id = ceil(l * i /8)

    if id > 213 * 1024 / 708:
        print(l)
'''
#ans: 274

#12
'''for alph in range(2,10000):
    i = ceil(log2(alph))
    id = ceil(80* i / 8)
    if id <= 150 * 1024 / 1200:
        print(alph)'''
#ans: 4096

#13
'''for alph in range(2,1000):
    i = ceil(log2(alph))
    id = ceil(261*i/8)

    if id > 31*1024*1024/252500:
        print(alph)'''
#ans: 9

#14
'''for dop in range(2,1000):
    alph = 10 + 510
    i = ceil(log2(alph))
    id = ceil(99 * i / 8)

    if id + dop > 543*1024/4322:
        print(dop)'''
#ans: 5

#15
'''for dop in range(1000):
    alph = 10 + 999
    i = ceil(log2(alph))
    id = ceil(745 * i / 8)

    if id + dop <= 311 * 1024 / 312:
        print(dop * 312)'''
#ans: 27456

#=======================================

#19360

'''alph = 66 + 10 + 50*5
i = ceil(log2(alph))
mes = ceil(1016 * i / 8)
print(mes)'''
#ans: 1143

#19243

'''for alph in range(2,100000):
    i = ceil(log2(alph))
    id = ceil(377 * i / 8)

    if id > 5536 * 1024 / 23155:
        print(alph)
        break'''
#ans: 33

#19155
'''c = 0
for alpha in range(2,1000):
    i = ceil(log2(alpha))
    id = ceil(157*i/8)

    if 30*1024*1024 / 233700 <= id <= 31 * 1024 * 1024 / 233700:
        c+=1
print(c)'''
#ans: 64

#17697

#ans:

#17696
'''alph = 10 + 1267
i = ceil(log2(alph))
id = ceil(623 * i / (8 * 1024))
print(id)
res = ceil(id * 2048 / 1024)
print(res)'''
#ans: 2

#212
'''for dop in range(1000):
    alph= 10 + 52 + 6
    i = ceil(log2(alph))
    id = ceil(9*i/8)
    if id + dop == 500/20:
        print(dop)'''

#ans: 17

#134

alph = 52 + 10
i = ceil(log2(alph))
id = ceil(11*i/8)
user = id + 13

print(1024/user)

#ans: 46

#19360
#ans: 1143

#19360
#ans: 1143

#19360
#ans: 1143

#19360
#ans: 1143

#19360
#ans: 1143

#19360
#ans: 1143






