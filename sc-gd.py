
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from unicodedata import name
from bs4 import BeautifulSoup
from bs4.dammit import EncodingDetector
import requests
x=0
c=[0]
b=[None] * 30000
a=[0]
a[0]=int(1)
def funf(a):
     while a[0] < 5024:
        html_text = requests.get('https://bestlightnovel.com/novel_888109183/chapter_%s'%a[0],headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}).text

        soup = BeautifulSoup(html_text,'html.parser')
        try:
            list=soup.find('div',class_='vung_doc').text
            a[0]+=1
            file1 = open("myfile.txt", "a")  # append mode
            file1.write(list)
            file1.close()
            a[0]=int(a[0])
            print(a[0])
        except:
            
            b[c[0]]=a[0]
            c[0]+=1
            return
       
        
while a[0]<5024:
    funf(a)

print("///")
while x<10:
    if(b[x]==None):
        
        x+=1
    elif(b[x]!=None):
        file1 = open("myfile.txt", "a")
        file1.write(str(b[x]-1))
        file1.write(',')
        x+=1

fromaddr = "testscrapformee@gmail.com"
toaddr = "testscrapformee@gmail.com"

# instance of MIMEMultipart
msg = MIMEMultipart()

# storing the senders email address
msg['From'] = fromaddr

# storing the receivers email address
msg['To'] = toaddr

# storing the subject
msg['Subject'] = "Subject of the Mail"

# string to store the body of the mail
body = "Body_of_the_mail"

# attach the body with the msg instance
msg.attach(MIMEText(body, 'plain'))

# open the file to be sent
filename = "myfile.txt"
attachment = open("/home/scrap/myfile.txt", "rb")

# instance of MIMEBase and named as p
p = MIMEBase('application', 'octet-stream')

# To change the payload into encoded form
p.set_payload((attachment).read())

# encode into base64
encoders.encode_base64(p)

p.add_header('Content-Disposition', "attachment; filename= %s" % filename)

# attach the instance 'p' to instance 'msg'
msg.attach(p)

# creates SMTP session
s = smtplib.SMTP('smtp.gmail.com', 587)

# start TLS for security
s.starttls()

# Authentication
s.login(fromaddr, "aa20052005")

# Converts the Multipart msg into a string
text = msg.as_string()

# sending the mail
s.sendmail(fromaddr, toaddr, text)

# terminating the session
s.quit()
