import bs4
import requests
with open('sylabus.txt','w',newline='')as f:
    tr=requests.get('https://www.codechef.com/certification/prepare#foundation-syllabus')
    sopu = bs4.BeautifulSoup(tr.text, 'lxml')
    ka=sopu.findAll('div',class_="collapsible mt0")

    print(ka)

