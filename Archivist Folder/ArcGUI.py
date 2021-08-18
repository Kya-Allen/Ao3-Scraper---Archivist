# -*- coding: utf-8 -*-
"""
Created on Tue Aug 17 23:00:13 2021

@author: Kya Allen
"""

from tkinter import *
from Archivist import *

root = Tk()
root.title('Archivist')
root.iconbitmap('c:/Users/Noah/Documents/Textbooks/Professional/fancourse_logo.ico')
root.geometry('800x600')
root.configure(background='#2b2b2b')

id_var = IntVar(value=ID_option)
title_var = IntVar(value=title_option)
auth_var = IntVar(value=author_option)
date_var = IntVar(value=datetime_option)
fandom_var = IntVar(value=fandom_option)
req_tag_var = IntVar(value=archive_tags_option)
tag_var = IntVar(value=tags_option)
stat_var = IntVar(value=stats_option)

def save_url():
    #url = urlsearch.get()
    return

def url_click():
    url_method.pack_forget()
    custom_search.pack_forget()
    
    urlsearch = Entry(root)
    searchbtn = Button(root, text='scrape', command=save_url)
    
    id_check = Checkbutton(root, text='Work ID', variable=id_var)
    title_check = Checkbutton(root, text='Title', variable=title_var)
    auth_check = Checkbutton(root, text='Author', variable=auth_var)
    date_check = Checkbutton(root, text='Date', variable=date_var)
    fandom_check = Checkbutton(root, text='Fandom', variable=fandom_var)
    req_tag_check = Checkbutton(root, text='Required Archive Tags', variable=req_tag_var)
    tag_check = Checkbutton(root, text='Tags', variable=tag_var)
    stat_check = Checkbutton(root, text='Work Stats', variable=stat_var)
    
    
    urlsearch.pack(pady=160)
    searchbtn.pack()
    id_check.pack()
    title_check.pack()
    auth_check.pack()
    date_check.pack()
    fandom_check.pack()
    req_tag_check.pack()
    tag_check.pack()
    stat_check.pack()
    return

def custom_click():
    url_method.pack_forget()
    custom_search.pack_forget()
    return

url_method = Button(root, text="Start from URL", command=url_click)
custom_search = Button(root, text="Custom Filters", command=custom_click)

url_method.pack(pady=150)
custom_search.pack(pady=0)

root.mainloop()