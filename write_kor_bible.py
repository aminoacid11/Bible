import csv

eng_file = open('t_kjv.csv')
eng_csvfile = csv.reader(eng_file)

ids = []
for index,each_row in enumerate(eng_csvfile):
    if index > 0:
        ids.append(each_row[0])

with open('kor_bible_info.txt') as f:
    lines = f.readlines()

lists = []
for ind,line in enumerate(lines):
    temp = []
    temp.append(ids[ind])
    temp.append(line.strip())
    lists.append(temp)

header = ['field','field']

with open('kor_bible_csv.csv','w',encoding='UTF8',newline='') as q:
    writer = csv.writer(q)
    writer.writerow(header)
    writer.writerows(lists)

q.close()