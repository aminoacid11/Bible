import csv
file = open('key_abbreviations_english.csv')
csvfile = csv.reader(file)
information = []
for row in csvfile:
    information.append(row)

def return_id(book,chapter,verse):
    id = 0
    for info in information:
        b_info = info[0].lower()
        if book == b_info:
            id += (int(info[1]) * 1000000)
    id += (int(chapter) * 1000) + (int(verse))
    return id