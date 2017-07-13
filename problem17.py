#-coding- unicode

def num_to_str(n):
    strnum = str(n)
    ndigit = len(strnum)
    htd = list()
    i = 0
    while i < ndigit:
        s = strnum[ndigit-1-i]
        htd.append(int(s))
        i += 1
    return htd

def transnum_to_word(num):
    onedict = {0:"",1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine"}
    tendict = {0:"ten",1:"eleven",2:"twelve",3:"thirteen",4:"fourteen",5:"fifteen",6:"sixteen",7:"seventeen",8:"eighteen",9:"nineteen"}
    tdict = {0:"",2:"twenty",3:"thirty",4:"forty",5:"fifty",6:"sixty",7:"seventy",8:"eighty",9:"ninety"}
    word = ""
    digit = len(num)
    if digit >1:
        if num[1] == 1:
            word += tendict[num[0]]
        else:
            word += tdict[num[1]]
            word += onedict[num[0]]
    else:
        word +=onedict[num[0]]

    if digit > 2:
        if num[2]>0:
            word += onedict[num[2]]+"hundred"
            if num[1]>0 or num[0]>0:
                word += "and"
        if digit > 3:
            word += "onethousand"

    return len(word)

if __name__ == '__main__':
    totallen = 0
    for i in range(1,1001):
        num = num_to_str(i)
        lennum = transnum_to_word(num)
        totallen += lennum
    print totallen
