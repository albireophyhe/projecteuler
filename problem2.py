# -*- coding: utf-8 -*-
"""
Created on Mon Jan 09 14:13:57 2017

@author: yukik_000
"""

def fib(k):
    if k > 2:
        n = fib(k-1) + fib(k-2)
        return n
    elif k == 1:
        return 1
    elif k == 2:
        return 2
    else: print "error"

if __name__ == "__main__":
    Sum = 0
    k = 1
    while(1):
        if fib(k) > 4000000:
            break
        elif fib(k) % 2 == 0:
            Sum = Sum + fib(k)
        k = k + 1
    print Sum