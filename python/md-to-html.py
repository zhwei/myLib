#encoding=utf-8

import os

files=os.listdir("./")
if "1" not in files:
	os.system("mkdir 1")
for i in files:
    if i=="1": continue
    if i=="add.html": continue
    if i=="b.py": continue
    if i=="a.py": continue
#    print(i[:-2])
    com="pandoc "+i+" -o 1"+os.sep+i[:-3]+".html"
    os.system(com)
    print("OVER")

print("ALL OVER")
