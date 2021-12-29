import csv
from id import *

file = open('t_kjv.csv')
csvfile = csv.reader(file)
verses = []
for row in csvfile:
    verses.append(row)

kor_b = open('kor_bible_csv.csv',encoding='UTF8')
kor_verses = []
kor_csv = csv.reader(x.replace('\0', '') for x in kor_b)
for k_row in kor_csv:
    kor_verses.append(k_row)

def return_verse(msg1,msg2):
    msg1 = msg1.split()
    book1 = msg1[0].lower()
    chp_ver1 = msg1[1].split(':')
    chapter_num1 = chp_ver1[0].replace(' ','')
    verse_num1 = chp_ver1[1].replace(' ','')
    id1 = return_id(book1,chapter_num1,verse_num1)
    
    msg2 = msg2.split()
    book2 = msg2[0].lower()
    chp_ver2 = msg2[1].split(':')
    chapter_num2 = chp_ver2[0].replace(' ','')
    verse_num2 = chp_ver2[1].replace(' ','')
    id2 = return_id(book2,chapter_num2,verse_num2)
    
    response = ''
    for i,v in enumerate(verses):
        if i>0 and int(v[0])>=id1 and int(v[0])<=id2:
            response += kor_verses[i][1] + '\n' + v[4] + '\n\n'

    if response == '':
        return "Nothing found. Please check again book name, chapter number, or verse number."
    else:
        return response