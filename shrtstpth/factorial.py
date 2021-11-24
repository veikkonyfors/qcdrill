

import timeit
#from functools import cache
import sys
sys.setrecursionlimit(5000)

#@cache
def factorial(n):
    return n * factorial(n-1) if n else 1

if __name__ == '__main__':
    print(timeit.timeit("factorial(10)", setup="from __main__ import factorial"))