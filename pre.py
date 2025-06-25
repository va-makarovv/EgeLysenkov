# 2
print("x y z w")
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                f = (x and not (y)) or (y == z) or not (w)
                if f == 0:
                    print(x, y, z, w)

# 5
for i in range(1, 500):
    r = str(bin(i)[2:])
    if r.count("1") % 2 == 0:
        r = r + "00"
    else:
        r = r + "11"
    r = int(r, 2)

    if r > 114:
        print(r)
# 5
for i in range(1000, 2000):
    startNum = str(i)
    num1 = int(startNum[0] + startNum[1] + startNum[2])
    num2 = int(startNum[1] + startNum[2] + startNum[3])
    endNum = abs(num1 - num2)

    if endNum == 415:
        print(i)
        break

# 6
from turtle import *

screensize(2000, 200)
k = 30
lt(90)
down()
tracer(90)

for i in range(7):
    rt(45)
    fd(k * 11)
    rt(45)

up()

for x in range(-30, 30):
    for y in range(-30, 30):
        goto(x * k, y * k)
        dot(3, "green")
done()

# 8

c = 0
alpha = "НОБЕЛИЙ"
for n1 in alpha:
    for n2 in alpha:
        for n3 in alpha:
            for n4 in alpha:
                for n5 in alpha:
                    for n6 in alpha:
                        for n7 in alpha:
                            word = n1 + n2 + n3 + n4 + n5 + n6 + n7
                            wordSet = set(word)
                            if len(wordSet) == len(word) and (n1 != "Й" and "ИЙО" not in word):
                                c += 1
print(c)

c = 0
for n1 in range(0, 9):
    for n2 in range(0, 9):
        for n3 in range(0, 9):
            for n4 in range(0, 9):
                for n5 in range(0, 9):
                    num = str(n1) + str(n2) + str(n3) + str(n4) + str(n5)
                    if num.count("3") <= 1 and n1 % 2 == 0 and n1 != 0 and (n5 != 1 and n5 != 8) and len(num) == 5:
                        c += 1
print(c)

# 8
alpha = "ДГИАШЭ"
sogl = "ДГШ"
glas = "ИАЭ"

с = 0
for n1 in sogl:
    for n2 in alpha:
        for n3 in alpha:
            for n4 in alpha:
                for n5 in glas:
                    с += 1
print(с)

# 9
a = open("n9recall")
c = 0

for line in a:
    line = [int(i) for i in line.split()]
    res = [line.count(j) for j in line]

    if res.count(2) == 2 and res.count(1) == 4:
        repSum = 0
        nonRepSum = 0
        for i in range(len(line)):
            if res[i] == 2:
                repSum += line[i]
            else:
                nonRepSum += line[i]

        nonRepAv = nonRepSum // 4

        if nonRepAv <= repSum:
            c += 1
print(c)

# 12
x = '8' * 68
while '222' in x or '888' in x:
    if '222' in x:
        x = x.replace('222', '8', 1)
    else:
        x = x.replace('888', '2', 1)

print(x)

# 13.4
from ipaddress import *

net = ip_network("192.168.32.160/255.255.255.240", False)
c = 0

for ip in net:
    strIP = bin(int(ip))[2::]
    if strIP.count("1") % 2 == 0:
        c += 1

print(c)
# 13.5
from ipaddress import *

net = ip_network("202.75.38.176/255.255.255.240")

for ip in net:
    strIP = bin(int(ip))[2::]
    if "111" not in strIP and "000" not in strIP:
        print(ip, strIP)

# 14
for x in range(0, 11):
    for y in range(0, 11):
        d1 = x * 11 ** 4 + 3 * 11 ** 3 + 4 * 11 ** 2 + 1 * 11 ** 1 + y * 11 ** 0
        d2 = 5 * 19 ** 4 + 6 * 19 ** 3 + x * 19 ** 2 + 1 * 19 ** 1 + y * 19 ** 0
        sumR = d1 + d2
        if sumR % 305 == 0:
            print(sumR // 305)


# 14
def change(n, sys):
    res = ''
    while n:
        res = str(n % sys) + res
        n //= sys
    return res


val = 49 ** 6 + 7 ** 18 - 21
val7 = change(val, 7)
num = val7.count("6")
print(num)

# 15
P = [i for i in range(130, 172)]
Q = [i for i in range(150, 186)]

for a_down in range(130, 186):
    for a_up in range(a_down + 1, 186):
        ok = True
        A = [i for i in range(a_down, a_up + 1)]
        for x in range(-3000, 3000):
            f = not (x in P) or (not ((x in Q) and not (x in A)) or not (x in P))
            if f == False:
                ok = False

        if ok:
            print(a_up - a_down)
# 16
from functools import lru_cache


@lru_cache(None)
def f(n):
    if n < 10:
        return n
    else:
        return 3 * n + f(n - 3)


for i in range(6250):
    f(i)
print((f(6250) + 2 * f(6244)) / f(6238))

# 17
aa = open("17 (2).txt")
data = [int(i) for i in aa]
l = sorted(data)
m13 = 0
sums = []

for i in range(len(data) - 1, 0, -1):
    if l[i] % 100 == 13:
        m13 = l[i]
        break

for j in range(len(data) - 2):
    a = data[j]
    b = data[j + 1]
    c = data[j + 2]
    sum = a + b + c
    if sum <= m13:
        if (len(str(abs(a))) == 3 and len(str(abs(b))) == 3 and len(str(abs(c))) != 3) or (
                len(str(abs(c))) == 3 and len(str(abs(b))) == 3 and len(str(abs(a))) != 3) or (
                len(str(abs(a))) == 3 and len(str(abs(c))) == 3 and len(str(abs(b))) != 3):
            sums.append(sum)

print(len(sums), min(sums))


# 23
def f(x, y):
    if x < y:
        return 0
    elif x == y:
        return 1
    else:
        return f(x - 2, y) + f(x // 2, y) + f(x // 3, y)


print(f(40, 20) * f(20, 4))

# 24.11
import re

a = open("task24.11_24.txt").readline()

num = "(([1-9][0-9]*)|0)"
reg = f"({num}([\+\*]{num})*)"

for m in re.findall(reg, a):
    print(m[0])

a = open("task24.4_24.txt").readline()

# 24.4
# max идущих подряд пар согл+глас
c = 0
cMax = 0
g = "AO"  # 0
s = "CDF"  # 1

a = a.replace("A", "0").replace("O", "0")
a = a.replace("C", "1").replace("D", "1").replace("F", "1")
a = a.replace("10", "9")

for i in range(len(a) - 1):
    if a[i] == "9":
        c += 1
        if c > cMax:
            cMax = c
    else:
        c = 0

print(cMax)

# 24.6
# макс длина
a = open("task24.6_24.txt").readline()

indT = []

for i in range(len(a)):
    if a[i] == "T":
        indT.append(i)

maxDiff = 0
for j in range(len(indT) - 101):

    curDiff = indT[j + 101] - indT[j]
    if curDiff > maxDiff:
        maxDiff = curDiff

maxLen = maxDiff - 1
maxLen = max(maxLen, len(a[0:indT[100]]))
maxLen = max(maxLen, len(a[indT[-101] + 1:]))

print(maxLen)


# 25
def f(n):
    num = set()
    for d in range(2, int(n ** 0.5) + 1):
        if n % d == 0:
            num.add(d)
            num.add(n // d)

    return sorted(num)


for i in range(300_000_000 + 1, 10 ** 9 + 1):
    y = f(i)

    if len(y) > 4:
        m = y[-5]
        print(m)

# 25
from fnmatch import *

for i in range(0, 10 ** 8, 317):
    if fnmatch(str(i), "12??1*56"):
        print(i, i // 317)

# 26
# 26.10
a = open("task26.10_26upd.txt")
skip = a.readline()
qValue = [int(i) for i in a.readline().split()]
data = []

for line in a:
    line = [int(i) for i in line.split()]
    pId = line[0]

    qSum = 0
    qFine = 0
    qSkip = 0

    line = line[1:]

    for j in range(len(line)):
        if line[j] == 0:
            qSkip += 1
        elif line[j] == 1:
            qSum += qValue[j]
        else:
            qFine += qValue[j]
            qSum -= qValue[j]

    data.append((pId, qSum, qFine, qSkip))

data.sort(key=lambda x: (-x[1], x[2], x[3], x[0]))

pLucky = len(data) // 3 - 1
pResLastLucky = data[pLucky][1:]
pLastOneIn3 = 0

for k in range(pLucky, pLucky + 1200):
    if data[k][1:] == pResLastLucky:
        pLastOneIn3 = k

pBestNotToWin = data[pLastOneIn3 + 1]
print(pBestNotToWin)

pRes1200 = data[1199][1:]
c = 0

for s in range(300, 2400):
    if data[s][1:] == pRes1200:
        c += 1
print(c)


# 27
def center(num):
    mS = 234567823456789
    mPos = 0
    for i in range(len(num)):
        x, y = num[i]
        sumAbc = 0
        for j in range(len(num)):
            x1, y1 = num[j]
            l = ((x - x1) ** 2 + (y - y1) ** 2) ** 0.5
            sumAbc += l
        if sumAbc < mS:
            mS = sumAbc
            mPos = (x, y)
    return mPos


a = open("task27.28_27-А.txt")
skip = a.readline()
data = []

for line in a:
    line = line.replace(",", '.')
    num = line.split()
    num = list(map(float, num))
    a, b = num
    data.append((a, b))

cl1 = []
cl2 = []
for i in range(len(data)):
    x, y = data[i]
    if x < 1.111 and y < 3:
        cl1.append((x, y))
    else:
        cl2.append((x, y))

cent1 = center(cl1)
a, b = cent1

cent2 = center(cl2)
c, d = cent2

Px = ((a + c) / 2) * 10_000
Py = ((b + d) / 2) * 10_000

print(Px, Py)


# 27

def center(num):
    sM = 234567898765432
    sPos = 0
    for x, y in num:
        sumAbc = 0
        for x1, y1 in num:
            l = ((y1 - y) ** 2 + (x - x1) ** 2) ** 0.5
            sumAbc += l

        if sumAbc < sM:
            sM = sumAbc
            sPos = x, y
    return sPos


def dist(n, n1):
    x, y = n
    x1, y1 = n1
    l = ((y1 - y) ** 2 + (x - x1) ** 2) ** 0.5
    return l


a = open("task27.32_27-Б.txt")
data = []

for line in a:
    line = line.replace(',', '.')
    x, y = list(map(float, line.split()))
    data.append((x, y))

clS = []

while data:
    cl = []
    q = [data.pop()]
    while q:
        p0 = q.pop()
        cl.append(p0)

        for p in data:
            if dist(p0, p) < 0.2:
                q.append(p)
                data.remove(p)
    clS.append(cl)

cl1 = clS[0] + clS[-1]
cl2 = clS[1]
cl3 = clS[2]
cl4 = clS[3] + clS[4]

clS = [cl1, cl2, cl3, cl4]
xP = 0
yP = 0
for c in clS:
    cent = center(c)
    xP += cent[0]
    yP += cent[1]

xP = int(xP / 4 * 10000)
yP = int(yP / 4 * 10000)

print(xP, yP)