#-coding- unicode

def collatz(n):
    nseq = 1
    while(True):
        if n==1:
            break
        if n % 2 == 0:
            n = n/2
        else:
            n = 3*n + 1
        nseq += 1
    return nseq

if __name__ == "__main__":
    #set search range
    m = 1000000
    #calculation
    l = 1
    num = 1
    longestn = 1
    while num < m:
        length = collatz(num)
        if length >= l:
            l = length
            longestn = num
        num += 1
    print longestn
