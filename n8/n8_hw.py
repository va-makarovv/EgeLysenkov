from itertools import *

'''k = 0

for i in product("0123456", repeat = 5):
    s = ''.join(i)
    if s[0] != '0' and s.count("6") == 1 and "00" not in s and "11" not in s and "22" not in s  and "33" not in s and" 44" not in s and "55" not in s and "66" not in s:
        k+=1
        print(k)'''

'''k = 0
for i in product("АКОРСТ", repeat =5):
    s = ''.join(i)
    k +=1
    print(s,k)'''

'''
№ 12917 PRO100 ЕГЭ 26.01.24 (Уровень: Базовый)
Петя составляет слова путём перестановки букв в слове ПРОСТО.
 Сколько он сможет составить слов, если запрещено ставить рядом две одинаковые буквы?
Показать ответ'''

'''from itertools import  permutations,product
k = 0
for i in set(permutations('ПРОСТО')):
    s = ''.join(i)
    if 'ОО' not in s:
        k += 1
        print(k,s)

k = 0
for i in  product('ПРОСТ',repeat = 6):
    s = ''.join(i)
    if 'ОО' not in s and s.count('П') == 1 and s.count('Р') == 1 and s.count('О') == 2 and s.count('Т') == 1 and s.count('С') == 1:
        k += 1
        print(k)'''

'''
№ 11657 (Уровень: Базовый)
(Л. Шастин) Сколько существует восьмеричных шестизначных чисел, не содержащих в своей записи цифру 3,
в которых все цифры различны и хотя бы две чётные стоят рядом?
Показать ответ'''

'''from itertools import  *
k = 0
for i in product('01234567',repeat = 6):
    s = ''.join(i)
    if s[0] != '0' and len(set(s)) == 6 and '3' not in s:
        s = s.replace('0','?').replace('2','?').replace('4','?').replace('6','?')
        if '??' in s:
            k += 1
            print(k)'''


