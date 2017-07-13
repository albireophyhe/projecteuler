#-coding- unicode

def readsource():
    filename = "p18.txt"
    #filename = "p067_triangle.txt" #for problem67
    f = open(filename,"r")
    rawdata = f.read()
    numlines = list()
    rawdata_to_line=rawdata.split("\n")
    for line in rawdata_to_line:
        content = line.split(" ")
        numlines.append(content)
    f.close()
    return numlines

def findprodutct(numberline_data):
    step_product = None
    step = len(numberline_data)-1
    while step>0:
        if step_product is None:
            line1 = numberline_data[step]
        else:
            line1 = step_product
        line2 = numberline_data[step-1]
        step_product=list()
        for n in range(len(line2)):
            num1 = int(line2[n])
            num2_1 = int(line1[n])
            num2_2 = int(line1[n+1])
            n_product = max(num1+num2_1,num1+num2_2)
            step_product.append(n_product)
        step -= 1
    max_product = step_product[0]
    return max_product



if __name__ == '__main__':
    lines=readsource()
    ans = findprodutct(lines)
    print ans
