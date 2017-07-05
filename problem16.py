#-coding- unicode


if __name__ == "__main__":
    num = 2**1000
    string = str(num)
    sum = 0
    for digit in string:
        sum = sum + int(digit)
    print sum
