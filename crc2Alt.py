import crcCalc
import sys
import string
import random
import time

def crcCrush(a):
	return [str(crcCalc.encMsgCalc(a) % (1<<32))]
	
if __name__ == '__main__':
	random.seed(time.time())
	str1 = "4055D713D44A765735481FD81B5F5283"
	crc1 = crcCrush(str1)
	print crc1
	
	while(1):
		str2 = "4055D7"+str(random.random())
		crc2 = crcCrush(str2)
					
		if crc1 == crc2:
			sys.stdout.write(str1)
			sys.stdout.write(str2)
			sys.stdout.write(str(crc1))
			sys.stdout.write(str(crc2))