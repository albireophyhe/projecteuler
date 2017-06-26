# -*- coding: utf-8 -*-
"""
Created on Thu Jan 12 14:05:31 2017

@author: yukik_000
"""

if __name__ == "__main__":
    sum1 = 0
    sum2 = 0
    for x in range(1,101):
        sum1 = sum1 + x**2
        sum2 = sum2 + x
    print sum1 - sum2**2
        