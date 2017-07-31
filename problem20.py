# -*- coding: utf-8 -*-

def Gamma(n):
    if n==1:
        return 1
    else:
        return (n-1)*Gamma(n-1)


if __name__ == '__main__':
    n100 = Gamma(101)
    strn100 = str(n100)
    sum = 0
    for i in strn100:
        num = int(i)
        sum += num
    print sum
