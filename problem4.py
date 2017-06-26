# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 17:06:47 2017

@author: yukik_000
"""

def find_palindromic(i):
    for j in range(i,0,-1):
        product = i * j
        chain = str(product)
        if len(chain)<6:
            break
        apart = chain[0:3]
        bpart = chain[3:6]
        bpart = bpart[::-1]
        if apart == bpart:
            break
    return(product)


if __name__ == "__main__":
    i = 999
    pnl = list()
    while i > 1:
        pn = find_palindromic(i)
        if len(str(pn)) >= 6:
            pnl.append(pn)
        i -= 1
    pnl.sort(reverse = True)
    print pnl[0]