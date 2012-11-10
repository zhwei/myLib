#encoding=utf-8

import os

input_pwd="zh"
output_pwd="12"
files=os.listdir(input_pwd)
for i in files:
    command='cp '+input_pwd +os.sep+i+' '+output_pwd+os.sep+i+'.html'
    os.system(command)
    print(i+".html is OK")

print('OVER')