
import sys
import time
f=open("cidian.txt","r",encoding='UTF-8')
line=f.readline()
while line:
    print(line)
    line=f.readline()
    time.sleep(0)
f.close()
    
