import stuck

def converter(num):
    while(num > 0):
        stuck.push(str(num % 2))
        num //= 2
    poppedVal = stuck.pop()
    convertedNum = ""
    while(poppedVal != None):
        convertedNum += poppedVal
        poppedVal = stuck.pop()
    return convertedNum

numToConvert = int(input("Enter number to convert to binary: "))
print(converter(numToConvert))