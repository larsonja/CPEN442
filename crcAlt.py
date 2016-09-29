import crcCalc
import sys
import string
import random
import time

def crcCrush(a):
	return [str(crcCalc.encMsgCalc(a) % (1<<32))]
	
if __name__ == '__main__':
	random.seed(time.time())
	
	while(1):
		str1 = "aaaaa"+str(random.random())
		crc1 = crcCrush(str1)
		str2 = "aaaaa"+str(random.random())
		crc2 = crcCrush(str2)
					
		if crc1 == crc2:
			sys.stdout.write(str1)
			sys.stdout.write(str2)
			sys.stdout.write(crc1)
			sys.stdout.write(crc2)