# -*- coding: utf-8 -*-

def finddivisor(n):
    maxdiv = n/2
    i = 1
    divisorlist = list()
    while i <= maxdiv:
        if n%i==0:
            divisorlist.append(i)
        i+=1
    return divisorlist

def d(n):
    alldivisors = finddivisor(n)
    sum = 0
    for divisor in alldivisors:
        sum += divisor
    return sum

if __name__ == '__main__':
    sumd = 0
    num = 1
    dset = set()
    while num <= 10000:
        d1 = d(num)
        d2 = d(d1)
        if d2 == num and d1!=d2:
            dset.add(num)

        num += 1

    for dnum in dset:
        sumd += dnum
    print sumd
