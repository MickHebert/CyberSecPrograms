# # Team Spinosaurs
# Dr. Timofeyev/Dr. Kiremire
# 3/29/23

from ftplib import FTP

# FTP server details gotten from from FTP tutorial in class
IP = "138.47.99.64"
PORT = 21
USER = "anonymous"
PASSWORD = ""
METHOD = 10 # change between 7 and 10 to do 7 or 10-bit conversion
FOLDER = f"/{METHOD}"
USE_PASSIVE = True  # set to False if the connection times out

# connect and login to the FTP server
ftp = FTP()
ftp.connect(IP, PORT)
ftp.login(USER, PASSWORD)
ftp.set_pasv(USE_PASSIVE)

# navigate to the specified directory and list files
ftp.cwd(FOLDER)
files = []
ftp.dir(files.append)

# exit the FTP server
ftp.quit()


# remove extraneous file info
def fileTruncate(file, bitValue):
    bitString = ""
    if bitValue == "/7":  # 7 bit
        # check 0, 1, and 2 for anything but ---
        if file[0:3] == "---":
            for binary in range(3, 10):
                if file[binary] == "-":
                    bitString += "0"
                else:
                    bitString += "1"
    if bitValue == "/10":  # 10 bit
        for binary in range(0, 10):
            if file[binary] == "-":
                bitString += "0"
            else:
                bitString += "1"
    return bitString

# turns binary value into ascii
def decoder(bitString):
    text = ""
    binString = ""
    count = 0
    for ch in bitString:
        count += 1
        binString += ch
        if count % 7 == 0:
            text += chr(int(binString, 2))
            binString = ""
    return text


decodedText = ""
bitString = ""
# grabs file names, makes long binary string
for file in files:
        bitString += fileTruncate(file, FOLDER)

decodedText = decoder(bitString)
print(decodedText)
