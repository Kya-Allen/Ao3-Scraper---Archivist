import pandas as pd
from bs4 import BeautifulSoup
import requests

WorkIds = []
#https://archiveofourown.org/works?utf8=%E2%9C%93&work_search%5Bsort_column%5D=title_to_sort_on&work_search%5Bother_tag_names%5D=&work_search%5Bexcluded_tag_names%5D=&work_search%5Bcrossover%5D=&work_search%5Bcomplete%5D=&work_search%5Bwords_from%5D=&work_search%5Bwords_to%5D=&work_search%5Bdate_from%5D=&work_search%5Bdate_to%5D=&work_search%5Bquery%5D=&work_search%5Blanguage_id%5D=en&commit=Sort+and+Filter&tag_id=POV+First+Person
def PageScraperID(url, pages=1):
    for i in range(pages):
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
            WorkIds.append(theid[6:])
            
        url = 'https://archiveofourown.org/' + NextPage

    print(WorkIds)
    print(url)
    
    return

html = requests.get('https://archiveofourown.org/works/' + '49526').text
soup = BeautifulSoup(html, features='lxml')
page = soup.find('div')
body = page.find('div', class_='wrapper')
bodyCenter = body.find('div')
TheWork = bodyCenter.find('div', id='workskin')
Chapter = TheWork.find('div', id='chapters')
RawText = Chapter.find_all('p').text

print(RawText)
        
        
#def WorkScraper(IdList):
    #if IdList == []:
        #print("There are no work ID's in this list")
        #return
    #for i in IdList:
#        html = requests.get('https://archiveofourown.org/works/' + '523577')
#        soup = BeautifulSoup(html, features='lxml')
#        page = soup.find('div')
#        body = page.find('div', class_='wrapper')
#        bodyCenter = body.find('div')
#        Ficstuff = bodyCenter.find('div', class_='work')
#        Workskin = Ficstuff.find('div', id_='workskin')
#        Chapter = Workskin.find('div', id_='chapter')
#        textblock = Chapter.find('div')
#        MainText = textbloack.find('div', role='article')
#        RawText = MainText.find_all('p').text
        
#print(RawText)
            
    
    #return
    

#PageScraperID('https://archiveofourown.org/works?utf8=%E2%9C%93&work_search%5Bsort_column%5D=title_to_sort_on&work_search%5Bother_tag_names%5D=&work_search%5Bexcluded_tag_names%5D=&work_search%5Bcrossover%5D=&work_search%5Bcomplete%5D=&work_search%5Bwords_from%5D=&work_search%5Bwords_to%5D=&work_search%5Bdate_from%5D=&work_search%5Bdate_to%5D=&work_search%5Bquery%5D=&work_search%5Blanguage_id%5D=en&commit=Sort+and+Filter&tag_id=POV+First+Person', pages=2)


    
