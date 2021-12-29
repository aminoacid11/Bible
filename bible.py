import tkinter.ttk as ttk
import tkinter.messagebox as msgbox
from tkinter import *
import csv
from bible_find import *

chp_file = open('key_abbreviations_english.csv')
chp_csvfile = csv.reader(chp_file)
chp_info = []
for chp_row in chp_csvfile:
    chp_info.append(chp_row)

file_engbible = open('t_kjv.csv')
eng_csvfile = csv.reader(file_engbible)
verses_info = []
for eng_row in eng_csvfile:
    verses_info.append(eng_row)

root = Tk()
root.title("Eng-Kor Bible")
root.geometry("1250x750+70+20")
root.configure(bg='#9a8262')
root.resizable(False,False)

def alert_sign(response):
    msgbox.showerror('Error',response)

def clear():
    result_window.config(state=NORMAL)
    result_window.delete("1.0",END)
    result_window.config(state=DISABLED)

def search():
    result_window.config(state=NORMAL)
    bk_name = entry_book.get()
    chp_number = entry_chapter.get()
    verse_number1 = entry_verse1.get()
    verse_number2 = entry_verse2.get()
    z=0
    if verse_number2 == '':
        verse_number2 = verse_number1
        z=1
    if verse_number1 == '' and verse_number2 == '':
        verse_number1 = '0'
        verse_number2 = '200'
        z=2
    entry_chapter.delete(0,END)
    entry_verse1.delete(0,END)
    entry_verse2.delete(0,END)
    if '/' in bk_name:
        keyword = ' / '
        eng_bk, keyword, kor_bk = bk_name.partition(keyword)
        msg1 = eng_bk + ' ' + chp_number + ':' + verse_number1
        msg2 = eng_bk + ' ' + chp_number + ':' + verse_number2
    else:
        msg1 = bk_name + ' ' + chp_number + ':' + verse_number1
        msg2 = bk_name + ' ' + chp_number + ':' + verse_number2

    response = return_verse(msg1,msg2)
    if response == "Nothing found. Please check again book name, chapter number, or verse number.":
        alert_sign(response)
    else:
        if z==0:
            result_window.insert(END,'From  ' + msg1 + '  to  ' + msg2 + '\n\n' + response + '- '*61)
        elif z==2:
            msg1 = msg1[:-2]
            result_window.insert(END, msg1 + '\n\n' + response + '- '*61)
        else:
            result_window.insert(END, msg1 + '\n\n' + response + '- '*61)
        result_window.config(foreground='#000000',font=("Helvetica", 14))
        result_window.config(state=DISABLED)
        result_window.yview(END)

# Buttons
btn_search = Button(root, padx=15, pady=10,fg='white',bg='#8b5a2b',font='Helvetica',text='Search',command=search)
btn_search.place(x=320,y=330)
btn_clear = Button(root, padx=10, pady=5,fg='white',bg='#8b5a2b',font='Helvetica',text='Clear All',command=clear)
btn_clear.place(x=825,y=655)

# Labels
label_book = Label(root,fg='black',text="Book: ", font='Helvetica',bg='#9a8262')
label_book.place(x=40,y=100)
label_chapter = Label(root,fg='black',text="Chapter: ", font='Helvetica',bg='#9a8262')
label_chapter.place(x=40,y=170)
label_verse1 = Label(root,fg='black',text="Verse: ", font='Helvetica',bg='#9a8262')
label_verse1.place(x=40,y=240)
label_verse2 = Label(root,fg='black',text="to", font='Helvetica',bg='#9a8262')
label_verse2.place(x=280,y=237)

# EntryBox
books = ['Genesis / 창세기','Exodus / 출애굽기','Leviticus / 레위기','Numbers / 민수기','Deuteronomy / 신명기','Joshua / 여호수아','Judges / 사사기','Ruth / 롯기','1Samuel / 사무엘상','2Samuel / 사무엘하',\
        '1Kings / 열왕기상','2Kings / 열왕기하','1Chronicles / 역대상','2Chronicles / 역대하','Ezra / 에스라','Nehemiah / 느헤미야','Esther / 에스더','Job / 욥기','Psalms / 시편','Proverbs / 잠언',\
        'Ecclesiastes / 전도서','Song of Songs / 아가','Isaiah / 이사야','Jeremiah / 예레미야','Lamentations / 예레미야애가','Ezekiel / 에스겔','Daniel / 다니엘','Hosea / 호세아','Joel / 요엘',\
        'Amos / 아모스','Obadiah / 오바댜','Jonah / 요나','Micah / 미가','Nahum / 나훔','Habakkuk / 하박국','Zephaniah / 스바냐','Haggai / 학개','Zechariah / 스가랴','Malachi / 말라기','Matthew / 마태복음',\
        'Mark / 마가복음','Luke / 누가복음','John / 요한복음','Acts / 사도행전','Romans / 로마서','1Corinthians / 고린도전서','2Corinthians / 고린도후서','Galatians / 갈라디아서','Ephesians / 에베소서','Philippians / 빌립보서',\
        'Colossians / 골로새서','1Thessalonians / 데살로니가전서','2Thessalonians / 데살로니가후서','1Timothy / 디모데전서','2Timothy / 디모데후서','Titus / 디도서','Philemon / 빌레몬서','Hebrews / 히브리서','James / 야고보서',\
        '1Peter / 베드로전서','2Peter / 베드로후서','1John / 요한일서','2John / 요한이서','3John / 요한삼서','Jude / 유다서','Revelation / 요한계시록']

entry_book = ttk.Combobox(root, width=23,font='Helvetica',values=books) 
entry_book.place(x=150,y=100)
entry_book.current(0)
entry_chapter = Entry(root, width=25,font='Helvetica',bg='white')
entry_chapter.place(x=150,y=170)
entry_verse1 = Entry(root, width=9,font='Helvetica',bg='white')
entry_verse1.place(x=150,y=240)
entry_verse2 = Entry(root, width=9,font='Helvetica',bg='white')
entry_verse2.place(x=325,y=240)

# Verse appearing window
result_window = Text(root, bd=0, bg='#e4d5b7', height=29, width=60, font='Arial')
result_window.config(state=DISABLED)
scrollbar = Scrollbar(root, command=result_window.yview, cursor="heart")
result_window['yscrollcommand'] = scrollbar.set
result_window.place(x=530, y=30, height=600, width=670)

root.mainloop()