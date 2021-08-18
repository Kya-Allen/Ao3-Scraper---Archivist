#Eventually Intend to add write-to-DataFrame functionality.
import pandas as pd
from bs4 import BeautifulSoup
import requests
import time

#Global Variables to hold the target data
work_ids = []
work_text = []
works_data = []


#class Work:
#    
#    def __init__(self, ID, title, author, datetime, rating, warnings, category, status, warning_tags, relationship_tags, freeform_tags, Language, wordcount, chapter_count, comment_count, Bookmark_count, Kudos_count, hits):
#        self.ID = ID
#        
#    def set_title(self, title):
#        self.title = title
#    
#    def set_author(self, author):
#        self.title = title


#Function Takes a URL and a number of pages to return a list of all Work Id's from those pages
def info_from_searchpage(url, pages=1):
    global work_ids
    global works_data
    work_ids = []
    works_data = []
    for i in range(pages):
        time.sleep(2)
        html = requests.get(url).text
        soup = BeautifulSoup(html, features='lxml')
        
        #get a reference to the next page
        NextTag = soup.find('a', rel='next')
       
        #get Id's
        workinfo = soup.find_all('li', role='article')            

        for li in workinfo:
            theid = li.get('id')
            work_ids.append(theid[5:])
            
            work_headers = li.find('h4', {'class': 'heading'})
            titles = work_headers.find('a')
            
            authors = work_headers.find('a', rel='author')
            
            datetime = li.find('p', {'class': 'datetime'})
            
            fandomheading = li.find('h5', 'fandoms heading')
            fandom = fandomheading.find('a')
            
            req_tagbox = li.find('ul', {'class': 'required-tags'})
            req_taglist = req_tagbox.find_all('span', {"class": 'text'})
            
            warnings = li.find_all('li', {'class': 'warnings'})
            warninglist = []
            for warning in warnings:
                entry = warning.find('a')
                warninglist.append(entry.text)
                
            relationships = li.find_all('li', {'class': 'relationships'})
            relationlist = []
            for relation in relationships:
                entry = relation.find('a')
                relationlist.append(entry.text)
                
            characters = li.find_all('li', {'class': 'characters'})
            characterlist = []
            for character in characters:
                entry = character.find('a')
                characterlist.append(entry.text)
            
            freeforms = li.find_all('li', {'class': 'freeforms'})
            freeformlist = []
            for freeform in freeforms:
                entry = freeform.find('a')
                freeformlist.append(entry.text)
            
            this_work = [theid[5:], titles.text, authors.text, datetime.text, fandom.text, req_taglist[0].text, req_taglist[1].text, req_taglist[2].text, req_taglist[3].text, warninglist, relationlist, characterlist, freeformlist, ]
            works_data.append(this_work)
            
            
        url = 'https://archiveofourown.org/' + NextTag.get('href')
        
    return

#Function takes a list of Work Id's to return a list of the text for the first chapter of each fic               
def chapter_from_id(IdList):
    global work_text
    work_text = []
    if IdList == []:
        print("There are no work ID's in this list")
        return
    for i in IdList:
        time.sleep(2)
        html = requests.get('https://archiveofourown.org/works/' + str(i)).text
        soup = BeautifulSoup(html, features='lxml')
        Chapter = soup.find('div', id='chapters')
        MessyText = Chapter.find_all('p')
        CleanText = []
        for i in MessyText:
            j = i.text.replace('<p>', ' ')
            CleanText.append(j)
        work_text.append(CleanText)
        
    return

#def get_tags()
    
