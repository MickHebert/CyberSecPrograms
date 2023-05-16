# Team Spinosaurs
# Dr. Timofeyev/Dr. Kiremire
# 3/23/23

import sys


def seven_bit_convert(binary):
    count = 0
    binaryString = ""
    asciiString = ""
    for number in range(len(binary)):
        if binary[number] not in ["0", "1"]:
            sys.exit("Input is not a binary number")
        count += 1
        if count % 7 != 0:
            binaryString += binary[number]
            continue
        else:
            binaryString += binary[number]
            decimalNum = int(binaryString, 2)  # conversion from base-2 string to base-10 int
            letter = chr(decimalNum)  # conversion from int to ASCII
            binaryString = ""
            count = 0
        asciiString += letter
    sys.stdout.write(asciiString + "\n")
    sys.exit(1)


def eight_bit_convert(binary):
    count = 0
    binaryString = ""
    asciiString = ""
    for number in range(len(binary)):
        if binary[number] not in ["0", "1"]:
            sys.exit("Input is not a binary number")
        count += 1
        if count % 8 != 0:
            binaryString += binary[number]
            continue
        else:
            binaryString += binary[number]
            decimalNum = int(binaryString, 2)  # conversion from base-2 string to base-10 int
            letter = chr(decimalNum)  # conversion from int to ASCII
            binaryString = ""
            count = 0
        asciiString += letter
    sys.stdout.write(asciiString + "\n")
    sys.exit(1)


# MAIN #
if len(sys.argv) != 1:  # usage checking
    sys.exit("Usage: python binary.py '< filename' or python binary.py [ENTER] 'binary string'")
binary = sys.stdin.readline().strip()  # gets user input from stdin, idea from https://www.geeksforgeeks.org/difference-between-input-and-sys-stdin-readline/
if len(binary) % 7 == 0:
    seven_bit_convert(binary)
elif len(binary) % 8 == 0:
    eight_bit_convert(binary)
else:
    sys.exit("Must input a 7 or 8-bit encoded binary string")