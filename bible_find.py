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

msg = input("Please input the books of the bible, chapter, ':', and verse (e.g. Genesis 2:15): ").split()

if len(msg) == 3:
    msg[0] = msg[0] + msg[1]
    msg[1] = msg[2]
    msg.pop()
elif len(msg) == 4:
    msg[0] = msg[0] + msg[1] + msg[2]
    msg[1] = msg[3]
    msg.pop()
    msg.pop()

book = msg[0].lower()
chp_ver = msg[1].split(':')
chapter_num = chp_ver[0].replace(' ','')
verse_num = chp_ver[1].replace(' ','')

id = return_id(book,chapter_num,verse_num)

response = ''
for i,v in enumerate(verses):
    if i>0 and id == int(v[0]):
        response = kor_verses[i][1] + '\n' + v[4]
        print(response)
if response == '':
    print("Nothing found. Please check again the book name, chapter number, or the verse number.")