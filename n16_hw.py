#13855
from functools import lru_cache

@lru_cache(None)
def f(n):
    if n >= 7777:
        return n
    else:
        return n + 5 + f(n+5)

for i in range(7772,0,-1):
    f(i)

print(f(1101) - f(1111))

#22558
'''def f(n):
    if n < 1_000:
        return 66
    if n >= 1000:
        return f(n-5)+ 100

for i in range(1000_000):
    f(i)'''






