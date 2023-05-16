#Team Spinosaurs
#Dr. Timofeyev/Dr. Kiremire
#3/22/23 
#Vigenere Cipher

import sys

def Vigenere(key, message, mode):
    key = key.upper().replace(' ', '') # removes case sensitive keys, replaces spaces in the key with nothing
    keyLen = len(key)
    messageLen = len(message)
    result = ''
    keyCount = 0
    for i in range(messageLen):
        char = message[i]
        if char.isalpha(): # if the letter is in the alphabet, encrypt or decrypt
            keyChar = key[keyCount % keyLen] # finds index based on keyCounter
            if mode == 'e':
                shift = ord(keyChar) - 65 # finds shift for encrypting
            elif mode == 'd':
                shift = 26 - (ord(keyChar) - 65) # finds shift for decrypting
            if char.isupper():
                result += chr((ord(char) - 65 + shift) % 26 + 65)
                keyCount += 1 # increments keyCounter if a letter is added
            else:
                result += chr((ord(char) - 97 + shift) % 26 + 97)
                keyCount += 1 # increments keyCounter if a letter is added
        else:
            result += char # if the letter is not in the alphabet, just add it to the result
    return result


if __name__ == '__main__':
    if len(sys.argv) != 3 or sys.argv[1] not in ['-e', '-d']: # input validation
        print('Usage: python vigenere.py {-e|-d} key')
        sys.exit(1)
    mode = sys.argv[1][1] # checks encrypt or decrypt mode
    key = sys.argv[2] # gets key
    message = sys.stdin.readline().strip() # gets user input, idea from https://www.geeksforgeeks.org/difference-between-input-and-sys-stdin-readline/
    print(Vigenere(key, message, mode)) # prints output based on function
