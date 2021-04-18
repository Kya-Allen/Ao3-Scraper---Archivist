#Eventually Intend to add write-to-DataFrame functionality.
import pandas as pd
from bs4 import BeautifulSoup
import requests
import time

#Global Variables to hold the target data
WorkIds = []
WorkText = []


#Function Takes a URL and a number of pages to return a list of all Work Id's from those pages
def PageScraperID(url, pages=1):
    for i in range(pages):
        time.sleep(2)
        html = requests.get(url).text
        soup = BeautifulSoup(html, features='lxml')
        page = soup.find('div')
        body = page.find('div', class_='wrapper')
        bodyCenter = body.find('div')
        Pagebar = bodyCenter.find('ol', role='navigation')
        NextTag = Pagebar.find('a', rel='next')
        NextPage = NextTag.get('href')
        PageWorks = bodyCenter.find('ol', class_='work index group')
        workinfo = PageWorks.find_all('li', role='article')

        for li in workinfo:
            theid = li.get('id')
            WorkIds.append(theid[5:])  
            
        url = 'https://archiveofourown.org/' + NextPage
    
    return


#Function takes a list of Work Id's to return a list of the text for the first chapter of each fic               
def WorkTextScraper(IdList):
    if IdList == []:
        print("There are no work ID's in this list")
        return
    for i in IdList:
        time.sleep(2)
        html = requests.get('https://archiveofourown.org/works/' + i).text
        soup = BeautifulSoup(html, features='lxml')
        page = soup.find('div')
        body = page.find('div', class_='wrapper')
        bodyCenter = body.find('div')
        TheWork = bodyCenter.find('div', id='workskin')
        Chapter = TheWork.find('div', id='chapters')
        MessyText = Chapter.find_all('p')
        CleanText = []
        for i in MessyText:
            j = i.text.replace('<p>', ' ')
            CleanText.append(j)
        WorkText.append(CleanText)
        
    return

    
