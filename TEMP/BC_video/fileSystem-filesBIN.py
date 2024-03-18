import os, sys, random, operator

#generator random
def randomBytes(size):
    bytes = []
    for x in range(size):
        bytes.append(random.randrange(0,255))
    return bytes

def displayBytes(bytes):
    print("-"*20)  #wyświetli pasek z 20 znaczków
    for index, item in enumerate(bytes, start=1):
        print(f'{index} = {item}({hex(item)})')
    print("-"*20)

# b =  randomBytes(10)
# displayBytes(b)
    
#write bytes binary
def  writeBytes(fileName, bytes):
    with open(fileName, 'wb') as file:
        for i in bytes:
            file.write(i.to_bytes(1, byteorder='big'))

#read bytes binary
def readBytes(fileName):
    bytes = []
    with open(fileName, 'rb') as file:
        while True:
            b = file.read(1)
            if not b:
                break
            bytes.append(int.from_bytes(b, byteorder='big'))    
    return bytes

#test
outBytes = randomBytes(10)
displayBytes(outBytes)
filePath = 'test.txt'
writeBytes(filePath, outBytes)
inBytes = readBytes(filePath)
displayBytes(inBytes)
print(operator.eq(outBytes,inBytes))

