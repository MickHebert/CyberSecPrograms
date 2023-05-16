# Team: Spinosaurs

import sys

KEY_FILE_HARD_CODED = True
KEY = "./key"

if __name__ == '__main__':
    if KEY_FILE_HARD_CODED:
        try:    
            keyFile = open(KEY, "rb")
        except:
            sys.exit(1)
    else:
        if len(sys.argv) != 2 : # input validation
            print('Usage: python XOR.py keyfile')
            sys.exit(1)
        try:    
            keyFile = open(sys.argv[1], "rb")
        except:
            sys.exit(1)
        
    keyData = bytearray(keyFile.read())
    inputData = bytearray(sys.stdin.buffer.read())
    inputSize = len(inputData)
    keySize = len(keyData)
    outputData = bytearray(inputSize)
    for i in range(inputSize):
        outputByte = inputData[i] ^ keyData[i]
        outputData[i] = outputByte
    
    sys.stdout.buffer.write(outputData)
    
    keyFile.close()
