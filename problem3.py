# -*- coding: utf-8 -*-
"""
Created on Mon Jan 09 14:42:46 2017

@author: yukik_000
"""
    
if __name__ == "__main__":
    k = 600851475143
    #k = 15
    i = 2
    soinsu = list()
    while k > 1:
        if k % i == 0:
            soinsu.append(i)
            k = k / i
            i = 2
        else: i += 1
    soinsu.sort(reverse = True)
    result = soinsu[0]
    print result
            