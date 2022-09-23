import os
import psutil
from pprint import pprint

sum_of_numbers = sum(n for n in range(1, 1000000))
print(f"sum is {sum_of_numbers}")
print(str(psutil.Process(os.getpid()).memory_info().rss / 1024 ** 2) + "MB")

rows = [i for i in range(0, 9)]
columns = "A B C D E F G H".split()
seating = [None] + [{column: None for column in columns} for _ in rows]
pprint(seating)
# print(seating[1]['B'])
