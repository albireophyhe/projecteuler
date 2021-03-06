# -*- coding: utf-8 -*-
"""
Created on Wed Jan 25 15:06:04 2017

@author: yukik_000
"""
import math
import time

def create_prime_number_list(k):
    pl = [2]
    i = 2
    while k >= len(str(i)):
        s = math.sqrt(i)
        for p in pl:
            if i % p == 0:
                i += 1
                break
            elif s < p:
                pl.append(i)
                i += 1
                break
    return(pl)
    
if __name__ == "__main__":
    init = time.time()
    plist = create_prime_number_list(16)
    plist.sort(reverse = True)
    print plist[0]
    t = time.time()-init
    print t
