# -*- coding: utf-8 -*-
"""
Created on Tue Aug 17 23:00:13 2021

@author: Kya Allen
"""
#Eventually Intend to add write-to-DataFrame functionality.
import pandas as pd
from bs4 import BeautifulSoup
import requests
import time

#Global Variables to hold the target data
work_ids = []
work_text = []
works_data = []

ID_option = True
title_option = False
author_option = False
datetime_option = False
fandom_option = False
archive_tags_option = False
tags_option = False
stats_option = False

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
            current_data = []
            theid = li.get('id')
            work_ids.append(theid[5:])
            current_data.append(theid[5:])
            
            if title_option or author_option:
                work_headers = li.find('h4', {'class': 'heading'})
            if title_option:
                titles = work_headers.find('a')
                current_data.append(titles.text)
            
            if author_option:
                authors = work_headers.find('a', rel='author')
                current_data.append(authors.text)
            
            if datetime_option:
                datetime = li.find('p', {'class': 'datetime'})
                current_data.append(datetime.text)
            
            if fandom_option:
                fandomheading = li.find('h5', 'fandoms heading')
                fandom = fandomheading.find('a')
                current_data.append(fandom.text)
            
            if archive_tags_option:
                req_tagbox = li.find('ul', {'class': 'required-tags'})
                req_taglist = req_tagbox.find_all('span', {"class": 'text'})
                current_data.append(req_taglist[0].text)
                current_data.append(req_taglist[1].text)
                current_data.append(req_taglist[2].text)
                current_data.append(req_taglist[3].text)
            
            if tags_option:
                warnings = li.find_all('li', {'class': 'warnings'})
                warninglist = []
                for warning in warnings:
                    entry = warning.find('a')
                    warninglist.append(entry.text)
                if warninglist == []:
                    warninglist = 'N/A'
                current_data.append(warninglist)
                    
                relationships = li.find_all('li', {'class': 'relationships'})
                relationlist = []
                for relation in relationships:
                    entry = relation.find('a')
                    relationlist.append(entry.text)
                if relationlist == []:
                    relationlist = 'N/A'
                current_data.append(relationlist)
                    
                characters = li.find_all('li', {'class': 'characters'})
                characterlist = []
                for character in characters:
                    entry = character.find('a')
                    characterlist.append(entry.text)
                if characterlist == []:
                    characterlist = 'N/A'
                current_data.append(characterlist)
                
                freeforms = li.find_all('li', {'class': 'freeforms'})
                freeformlist = []
                for freeform in freeforms:
                    entry = freeform.find('a')
                    freeformlist.append(entry.text)
                if freeformlist == []:
                   freeformlist = 'N/A'
                current_data.append(freeformlist)
            
            if stats_option:
                language = li.find('dd', {'class': 'language'}).text
                word_count = li.find('dd', {"class": 'words'}).text
                chapters = li.find('dd', {'class': 'chapters'}).text
                comment_count = li.find('dd', {'class': 'comments'})
                if comment_count is None:
                    comment_count = 0
                else:
                    comment_count = comment_count.text
                kudos_count = li.find('dd', {'class': 'kudos'})
                if kudos_count is None:
                    kudos_count = 0
                else: 
                    kudos_count = kudos_count.text
                bookmarks_count = li.find('dd', {'class': 'bookmarks'})
                if bookmarks_count is None:
                    bookmarks_count = 0
                else:
                    bookmarks_count = bookmarks_count.text
                hits = li.find('dd', {'class': 'hits'})
                if hits is None:
                    hits = 0
                else:
                    hits = hits.text
                current_data.append(language)
                current_data.append(word_count)
                current_data.append(chapters)
                current_data.append(comment_count)
                current_data.append(kudos_count)
                current_data.append(bookmarks_count)
                current_data.append(hits)
                
            
            works_data.append(current_data)
            
            url = 'https://archiveofourown.org/' + NextTag.get('href')
        
    return

def as_csv():
    my_columns = []
    if ID_option:
        my_columns.append('Id')
    if title_option:
        my_columns.append('Title')
    if author_option:
        my_columns.append('Author')
    if datetime_option:
        my_columns.append('Published')
    if fandom_option:
        my_columns.append('Fandom')
    if archive_tags_option:
        my_columns.append('Rating')
        my_columns.append('Warning')
        my_columns.append('Category')
        my_columns.append('Status')
    if tags_option:
        my_columns.append('Warning Tags')
        my_columns.append('Relationships')
        my_columns.append('Characters')
        my_columns.append('Tags')
    if stats_option:
        my_columns.append('Language')
        my_columns.append('Word Count')
        my_columns.append('Chapters')
        my_columns.append('Comment Count')
        my_columns.append('Kudos Count')
        my_columns.append('Bookmarks Count')
        my_columns.append('hits')
    
    df = pd.DataFrame(works_data, columns = my_columns)
    df.to_csv('./testfol/testfile.csv', index=False)
    
    
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
