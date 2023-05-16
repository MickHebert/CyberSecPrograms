# Team: Spinosaurs

import sys

SENTINEL = bytearray([0, 0xff, 0, 0, 0xff, 0])

def getArgs():
    args = []
    for i in range(1,6):
        if (i - 2) < 1:
            args.append(sys.argv[i])
        else:
            args.append(sys.argv[i][2:])
    if args[0] == "-s":
        args.append(sys.argv[6][2:])
    return args
    
def byteStore(wrapper, hidden, offset=0, interval=1):
    wrapperFile = open(wrapper, "rb")
    hiddenFile = open(hidden, "rb")
    
    wrapperBytes = bytearray(wrapperFile.read())
    hiddenBytes = bytearray(hiddenFile.read())
    
    wrapperSize = len(wrapperBytes)
    i = 0
    position = offset
    
    while(i < wrapperSize):
        wrapperBytes[position] = hiddenBytes[i]
        position += interval
        i += 1
        
    i = 0
    while( i < len(SENTINEL)):
        wrapperBytes[position] = SENTINEL[i]
        position += interval
        i += 1
        
    wrapperFile.close()
    hiddenFile.close()
    
    return wrapperBytes
        
def byteExtract(wrapper, offset=0, interval=1):
    wrapperFile = open(wrapper, "rb")
    wrapperBytes = bytearray(wrapperFile.read())
    
    outputBytes = bytearray()
    
    wrapperSize = len(wrapperBytes)
    position = offset
    while(position < wrapperSize):
        b = wrapperBytes[position]
        if b == 0b00:
            lookAheadPos = position + interval
            sent = True
            for i in range(5):
                if (lookAheadPos < wrapperSize):
                    lookAheadB = wrapperBytes[lookAheadPos]
                else:
                    sent = False
                    break
                if (lookAheadB != SENTINEL[i+1]):
                    sent = False
                    break
                lookAheadPos += interval
            if sent:
                return outputBytes
        outputBytes.append(b)
        position += interval
        
    wrapperFile.close()
    
    return outputBytes
    
    
def bitStore(wrapper, hidden, offset=0, interval=1):
    wrapperFile = open(wrapper, "rb")
    hiddenFile = open(hidden, "rb")
    
    wrapperBytes = bytearray(wrapperFile.read())
    hiddenBytes = bytearray(hiddenFile.read())
    
    wrapperSize = len(wrapperBytes)
    i = 0
    position = offset
    while(i < wrapperSize):
        for  j in range(8):
            wrapperBytes[position] &= 0b11111110
            wrapperBytes[position] |= ((hiddenBytes[i] & 0b10000000) >> 7)
            hiddenBytes[i] <<= 1
            position += interval
        i += 1
        
    i = 0
    while( i < len(SENTINEL)):
        for j in range(8):
            wrapperBytes[position] &= 0b11111110
            wrapperBytes[position] |= ((SENTINEL[i] & 0b10000000) >> 7)
            hiddenBytes[i] <<= 1
            position += interval
        i += 1
    
    wrapperFile.close()
    hiddenFile.close()
        
    return wrapperBytes

def bitExtract(wrapper, offset=0, interval=1):
    wrapperFile = open(wrapper, "rb")
    wrapperBytes = bytearray(wrapperFile.read())
    
    outputBytes = bytearray()
    
    wrapperSize = len(wrapperBytes)
    position = offset
    while((position + 7*interval) < wrapperSize):
        b = 0
        for j in range(8):
            b |= (wrapperBytes[position] & 0b00000001)
            if (j < 7):
                b <<= 1
                position += interval
        #print(hex(b))
        if (b == 0b00):
            lookAheadPos = position + interval
            sent = True
            for i in range(5):
                if ((lookAheadPos+ 7*interval) < wrapperSize):
                    lookAheadB = 0
                    for k in range(8):
                        lookAheadB |= (wrapperBytes[lookAheadPos] & 0b00000001)
                        if (k < 7):
                            lookAheadB <<= 1
                            lookAheadPos += interval
                    if (lookAheadB != SENTINEL[i+1]):
                        sent = False
                        break
                else:
                    break
                lookAheadB += interval
            if sent:
                return outputBytes
                
        outputBytes.append(b)
        position += interval
        
    wrapperFile.close()
    
    return outputBytes
        
if __name__ == '__main__':
    if len(sys.argv) < 4 : # input validation
        print("Usage: python Steg.py -(sr) -(bB) -o<val> [-i<val>] -w<val> [-h<val>]")
        print("-s store\n-r retrieve\n-b bit mode\n-B byte mode\n-o<val> set offset to <val> (default is 0)\n-i<val> set interval to <val> (default is 1)\n-w<val> set wrapper file to <val>\n-h<val> set hidden file to <val>")
        
    args = getArgs()
    if (args[0] == "-s"):
        if (args[1] == "-b"):
            output = bitStore(args[4], args[5], int(args[2]), int(args[3]))
        else:
            output = byteStore(args[4], args[5], int(args[2]), int(args[3]))
    else:
        if (args[1] == "-b"):
            output = bitExtract(args[4], int(args[2]), int(args[3]))
        else:
            output = byteExtract(args[4], int(args[2]), int(args[3]))
    
    #print(output)
    
    sys.stdout.buffer.write(output)
