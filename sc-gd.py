
from unicodedata import name
from bs4 import BeautifulSoup
from bs4.dammit import EncodingDetector
import requests
import creds
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
            b[a[0]]=a[0]
            a[0]+=1
            return
       
        
while a[0]<5024:
    funf(a)


for x in range(1000):
    if(x!=None):
        print ("dow",b[x])


