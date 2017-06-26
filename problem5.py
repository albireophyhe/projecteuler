# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 17:27:32 2017

@author: yukik_000
"""

def pl(k):
    i = 2
    plist = list()
    while k > 1:
        if k % i == 0:
            plist.append(i)
            k = k / i
            i = 2
        else:
            i += 1
    return plist
    
def donothing():
    return()

if __name__ == '__main__':
    n = 20
    insu = list()
    while n > 1:
        for p in pl(n):
            if len(insu) == 0:
                insu.append(p)
            l = 1
            for ins in insu:
                if p == ins:
                    break
                elif l < len(insu):
                    l += 1
                else:
                    insu.append(p)
        n -= 1
    insu.sort()
    product = 1
    for ins in insu:
        noi = list()
        for x in range(1,21):
            ct = 0
            for p in pl(x):
                if p == ins:
                    ct += 1
            noi.append(ct)
        ni = max(noi)
        product = product * ins ** ni
    print product