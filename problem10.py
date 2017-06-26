# -*- coding: utf-8 -*-
"""
Created on Thu Jan 26 14:29:30 2017

@author: yukik_000
"""
import numpy as np
import time

def create_prime_number_list(k):
    pl = [2]
    i = 2
    while k >= i:
        s = np.sqrt(i)
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
    plist = create_prime_number_list(2000000)
    Sum = 0
    print plist
    for p in plist:
        Sum = Sum + p
    print Sum
    t = time.time()-init
    print t