import requests
from bs4 import BeautifulSoup
import csv
import time

rmKeyword = '동사구문사전 : '

f = open('verb.csv', 'a', newline='')
wr = csv.writer(f)
link = "http://waks.aks.ac.kr/rsh/dir/rdirItem.aspx?rshID=AKS-2012-EBZ-3102&rptID=AKS-2012-EBZ-3102_DES&dirRsh=&curPage=1&pageSize=100"
for i  in range(1, 52):
    url = "http://waks.aks.ac.kr/rsh/dir/rdirItem.aspx?rshID=AKS-2012-EBZ-3102&rptID=AKS-2012-EBZ-3102_DES&dirRsh=&curPage="
    url += str(i)+"&&pageSize=100"
    print(url)

    webpage = requests.get(url)
    soup = BeautifulSoup(webpage.content, "html.parser")
    verbList = soup.select("section.list_wrap > ul > li > div.type1_title > span")
    for verb in verbList:
        verbid = verb.attrs["id"]
        verbVal = verb.get_text().strip(rmKeyword)
        wr.writerow([verbid, verbVal])
    
    time.sleep(10)
f.close()
