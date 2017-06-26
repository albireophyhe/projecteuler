# -*- coding: utf-8 -*-
"""
Created on Mon Jan 09 14:06:10 2017

@author: yukik_000
"""

if __name__ == "__main__":
    Sum = 0
    n = 1
    while n < 1000:
        if n % 3 == 0:
            Sum = Sum + n
        if n % 5 == 0:
            Sum = Sum + n
        if n % 15 == 0:
            Sum = Sum - n
        n += 1
    print Sum