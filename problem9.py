# -*- coding: utf-8 -*-
"""
Created on Thu Jan 26 14:02:51 2017

@author: yukik_000
"""

if __name__ == '__main__':
    Sum = 1000
    c = 499
    while c > 0:
        b = c
        a = 1000 - 2 * c
        c2 = c * c
        while b > a:
            b2 = b*b
            a2 = a*a
            d = c2 - a2 - b2
            
            if d < 0:
                b -= 1
                a += 1
            else:
                break
        if c2 == a2 + b2:
            break
        else:
            c -= 1
    pro = a*b*c
    print pro
