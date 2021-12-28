total_bible = []
for i in range(39):
    with open('1-{}.txt'.format(i+1)) as f:
        bk = f.readlines()
    total_bible.append(bk)

for i in range(27):
    with open('2-{}.txt'.format(i+1)) as f:
        bk = f.readlines()
    total_bible.append(bk)

print(len(total_bible))

kor_bible_info = open('kor_bible_info.txt','w+')
for row in total_bible:
    for r in row:
       kor_bible_info.write(r)

kor_bible_info.close()