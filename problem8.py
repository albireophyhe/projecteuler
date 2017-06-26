# -*- coding: utf-8 -*-
"""
Created on Thu Jan 12 15:20:57 2017

@author: yukik_000
"""

if __name__ == '__main__':
    source_file = open('p8source.txt')
    source = source_file.read()
    digilength = 13
    product = 0
    numberlist = list(source[i:i+digilength] for i in range(0,len(source)-digilength))
    for numbergroup in numberlist:
        p = 1
        for x in range(0,digilength):
          p = p * int(numbergroup[x])
        if p > product:
            product = p
    print product