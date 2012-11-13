#encoding=utf-8

add = open('add.html')
addhtml = add.read()
add.close()
#print(addhtml)
import os

files = os.listdir("./")
for i in files:
	if i=="add.html": continue
	if i=="b.py": continue
	handlef = open(i,'a')
	handlef.write(addhtml)
	handlef.close()
	print(i + "           is OVER")

print("that's ALL'")
