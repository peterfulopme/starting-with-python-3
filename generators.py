import random
from itertools import count


def take(count, iterable):
    counter = 0
    for item in iterable:
        if counter == count:
            return
        counter += 1
        yield item


def distinct(iterable):
    seen = set()
    for item in iterable:
        if item in seen:
            continue
        yield item
        seen.add(item)


def run_pipeline():
    items = [random.randint(i, 2*i) for i in range(8, random.randint(15, 25))]
    print(items)
    for item in take(3, distinct(items)):
        print(item)


def sequence():
    for n in count(1):
        yield n


# print("testing pipelines")
# run_pipeline()
s = sequence()
print(next(s))
print(next(s))
print(next(s))
print(next(s))