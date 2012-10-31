#coding=utf-8

import os
p=os.listdir("./")
os.system('mkdir o')
for i in p:
    if i == "o":continue
    if i == "a.py":continue
    if i == "date":continue
    print(i)
    com="iconv -f cp936 -t utf-8 " + i +">"+ "o"+os.sep+i
    os.system(com)
    print(i +"   is OVER")

print('OK')
os.system('cp o/* ./ -f')
print("COPY is OK")
os.system('rm o -rf')
print("o have been REMOVE")
print("conve is OVER")