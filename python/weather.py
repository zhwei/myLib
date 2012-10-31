#coding=utf-8
__author__ = 'zhwei'

import re
import urllib
city={
    'city_name':'http://wap.weather.com.cn/wap/weather/??????.shtml',
}
msg1=""
for key in city:
    content=urllib.urlopen(city[key]).read()
    regex=ur"(?<=<(dt)>).*(?=<\/\1>)" #regex
    match = re.search(regex, content)
    result = match.group()
    wea=result.replace("<br />&nbsp;","  ")
    msg1=msg1 +key +"\n"+wea+"\n"
#print(msg1)

#send mail
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
msg = MIMEMultipart()
msg['From'] = "weather"
msg['To'] = 'YOU'
msg['Subject'] = 'Weather'

#mail content
txt =MIMEText(msg1,'plain','utf-8')
msg.attach(txt)

smtp=smtplib.SMTP()
smtp.connect("smtp.163.com","25")
smtp.login("username","passwd")
smtp.sendmail("zh_yes@163.com","zh_yes@139.com",msg.as_string())
smtp.quit()
print("OK!")
#print(msg.as_string())

