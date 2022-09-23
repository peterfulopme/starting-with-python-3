from itertools import count
from itertools import islice


def rsequence():
    """ generator for Recamán's """
    a = 0
    seen = {a}
    yield a
    for n in count(1):
        print(f"n={n}")
        c = a - n
        if (c > 0) and not(c in seen):
            seen.add(c)
            a = c
            yield c
        else:
            c = a + n
            a = c
            seen.add(c)
            yield c


g = rsequence()
for x in list(islice(g, 0, 10)):
    print(x)



