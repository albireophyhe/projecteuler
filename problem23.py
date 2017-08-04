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

def abundant(n):
    divisorlist = finddivisor(n)
    divisorsum = 0
    for divisor in divisorlist:
        divisorsum += divisor
    if divisorsum > n:
        return 1
    else:
        return 0

def abundantlist(k):
    ablist = list()
    i = 1
    while i <= k:
        if abundant(i) == 1:
            ablist.append(i)
        i += 1
    return ablist

if __name__ == '__main__':
    print "Making abundant number list..."
    numlist = range(0, 28124)
    abunlist = abundantlist(28123)
    print "Calculating abundant sum..."
    possiblesum = set()
    for i in range(len(abunlist)):
        j = i
        num1 = abunlist[i]
        if j < len(abunlist):
            k = j
            while k < len(abunlist):
                num2 = abunlist[k]
                numsum = num1 + num2

                if numsum > 28123:
                    break
                possiblesum.add(numsum)
                k += 1
        else:
            print "All abundant sum calcutated."

    for posisum in possiblesum:
        numlist.remove(posisum)
    print "Calculating sum of non-abundant sum number"
    Allsum = 0
    for num in numlist:
        Allsum += num
    print Allsum
