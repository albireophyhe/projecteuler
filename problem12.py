#/usr/bin/python
#coding:utf-8

def mktrnum(k):
    sum = 0
    n = 1 
    while n<=k:
        sum = sum + n
        n += 1
    return sum

def findfactor(k):
    factorlist = list()
    f = 1
    while f <= k:
        if k%f == 0:
            factorlist.append(f)
        f += 1
    return factorlist

if __name__ == "__main__":
    n = 1
    while True:
        tr = mktrnum(n)
        fl = findfactor(tr)
#        print tr
#        print len(fl)
        if len(fl) > 500:
            break
        else:
            n += 1
    print tr
