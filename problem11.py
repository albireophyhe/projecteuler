# -*- coding: utf-8 -*-
"""
Created on Thu Jan 26 14:37:11 2017

@author: yukik_000
"""

if __name__ == "__main__":
    grid = open('p11.txt')
    numgrid = grid.read()
    grid.close()

    newgrid = list()
    datagroup = numgrid.split("\n")
    for line in datagroup:
        if len(line) > 0:
            numline = list()
            newline = line.split(" ")
            for num in newline:
                numline.append(int(num))
            newgrid.append(numline)
    p = 0
    for l in range(len(newgrid) - 3):
        lp = 0
        for k in range(len(newgrid[l]) - 3):
            product1=newgrid[l][k]*newgrid[l][k+1]*newgrid[l][k+2]*newgrid[l][k+3]
            product2=newgrid[l][k]*newgrid[l+1][k]*newgrid[l+2][k]*newgrid[l+3][k]
            product3=newgrid[l][k]*newgrid[l+1][k+1]*newgrid[l+2][k+2]*newgrid[l+3][k+3]
            lp = max(lp,product1,product2,product3)
        for m in range(3,len(newgrid[l])):
            product4=newgrid[l][m]*newgrid[l+1][m-1]*newgrid[l+2][m-2]*newgrid[l+3][m-3]
            lp = max(lp,product4)
        p = max(p,lp)
    print p
