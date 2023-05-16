from datetime import datetime
from hashlib import md5
import pytz, sys

def toSeconds(dateInput):
    year = int(dateInput[0])
    month = int(dateInput[1])
    day = int(dateInput[2])
    hour = int(dateInput[3])
    minute = int(dateInput[4])
    second = int(dateInput[5])
    dt = datetime(year, month, day, hour, minute, second).astimezone(pytz.UTC)

    return dt

def makeCode(seconds):
    # https://www.geeksforgeeks.org/md5-hash-python/
    letters = "abcdef"
    numbers = "0123456789"
    hashedSeconds = str(md5(str(md5(seconds.encode()).hexdigest()).encode()).hexdigest())
    
    letterCount = 0
    for i in hashedSeconds:
        if i in letters:
            print(i, end="")
            letterCount += 1
            if letterCount == 2:
                break
    
    numberCount = 0
    for i in reversed(hashedSeconds):
        if i in numbers:
            print(i, end="")
            numberCount += 1
            if numberCount == 2:
                break
    print()


if len(sys.argv) != 1:  # usage checking
    sys.exit("Usage: python timelock.py '< filename' or python timelock.py [ENTER] year month day hour min sec")
epoch = sys.stdin.readline().rstrip()
epochList = epoch.split()
epoch = toSeconds(epochList)

testD = "2017 04 23 18 02 30" # CHANGE THIS TO TEST

testD = testD.split()
testD = toSeconds(testD)
now = datetime.now().astimezone(pytz.UTC)

# https://pynative.com/python-datetime-to-seconds/
e = epoch.timestamp()
now = now.timestamp()
testD = testD.timestamp()
td = int(testD - e)
adjtd = td - (td % 60)
timeSinceTest = str(int(adjtd))

secs = int(now - e)
adjSecs = secs - (secs % 60)
timeSince = str(int(adjSecs))

print("Test Case:")
makeCode(timeSinceTest)
print()
print("System Time:")
makeCode(timeSince)
