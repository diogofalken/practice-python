'''
  Author: Diogo Costa
  005 - List Overlap
  
  Description: README.md
'''
import random

# Get random list with numbers beetwen 1 and 100
list1 = random.sample(range(1, 100), random.randint(1, 20))
list2 = random.sample(range(1, 100), random.randint(1, 20))

# Doing the entire operation in just one line of code
result = list(filter(lambda x: list2.count(x) > 0, list1))

print(list1)
print(list2)
print(result)