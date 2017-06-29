#-coding- unicode

#make numlist from data
def strtonumline(line):
    l = list()
    for num in range(0,len(line)):
        a = line[num]
        try:
            a = int(a)
            l.append(a)
        except:
            b = 0
    return l


if __name__ == '__main__':
    sumdata = open("bigsum.dat")
    llist=list()
    sum = 0
    #direct sum
    for nline in sumdata:
        k = int(nline)
        sum += k
    print sum
    sumdata.close()

    #calculate in limit digits
    #prepare number list
    sumdata = open("bigsum.dat")
    for mline in sumdata:
        llist.append(strtonumline(mline))

    #digits wanted
    ndigit = 10
    #calculation
    sum2 = 0
    err = 9*len(llist[0])
    digit = ndigit+len(str(err))
    k = 0

    while digit > -1:
        for i in llist:
            sum2 += i[digit]*(10**k)
        digit -= 1
        k += 1
    print sum2
