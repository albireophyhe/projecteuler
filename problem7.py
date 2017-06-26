# -*- coding: utf-8 -*-
"""
Created on Thu Jan 12 14:07:54 2017

@author: yukik_000
"""

def create_prime_number_list(k):
    pl = list()
    i = 2
    ct = 1
    if len(pl) == 0:
        pl.append(2)
    while k > ct:
        l = 1
        for p in pl:
            if i % p == 0:
                i += 1
                break
            elif l < len(pl):
                l += 1
            else:
                pl.append(i)
                ct += 1
                i += 1
    return(pl)
    
if __name__ == "__main__":
    plist=create_prime_number_list(10001)
    plist.sort(reverse = True)
    print plist[0]