# use Python 3
import socket
from sys import stdout, exit
from time import time

# invervals for 1 and 0
int0 = 0.05
# enables debugging output
DEBUG = True

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
	stdout.write(asciiString + "\n")
	stdout.flush()

def seven_bit_convert(binary):
	count = 0
	binaryString = ""
	asciiString = ""
	for number in range(len(binary)):
		if binary[number] not in ["0", "1"]:
			exit(1)
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
	stdout.write(asciiString + "\n")



# set the server's IP address and port
ip = "10.4.4.100"
port = 12345

# create the socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect to the server
s.connect((ip, port))

# make array for bits
bits =  ""
# receive data until EOF
data = s.recv(4096).decode()
while (data.rstrip("\n") != "EOF"):
	# output the data
	stdout.write(data)
	stdout.flush()
	# start the "timer", get more data, and end the "timer"
	t0 = time()
	data = s.recv(4096).decode()
	t1 = time()
	# calculate the time delta (and output if debugging)
	delta = round(t1 - t0, 3)
	if (DEBUG):
		stdout.write(" {}\n".format(delta))
		stdout.flush()
	if (delta < int0):
		bits += "0"
	else:
		bits += "1"

# close the connection to the server
s.close()

print(bits)
eight_bit_convert(bits)
print("-------------------------")
seven_bit_convert(bits)
print()
