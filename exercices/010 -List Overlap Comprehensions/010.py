'''
  Author: Diogo Costa
  010 - List Overlap Comprehensions
  
  Description: README.md
'''
import random

if __name__ == "__main__":
    # Generate two random lists
    list1 = random.sample(range(1, 100), random.randint(1, 20))
    list2 = random.sample(range(1, 100), random.randint(1, 20))

    # Solving the issue using list comprehension
    result = list([x for x in set(list1) if x in list2])

    # Print list, list2 and resulting list
    print(list1)
    print(list2)
    print(result)
