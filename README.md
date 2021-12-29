# Bible App

This is a bible application that provides bible verses to the users when requested. <br />
It provides bible verses in two languages: English and Korean. <br />

For the english bible, I used the open dataset from Kaggle, where the bible verses are provided in csv files. <br />
Link of the source: https://www.kaggle.com/oswinrh/bible?select=t_asv.csv  <br />

For the korean bible, I used the data from: <br />
https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=hit4079&logNo=60139979928  <br />
Out of these numerous datasets, I used the file where the korean bible verses were written in 66 different .txt files. <br />

## File informations: <br />
new_save.py contains the code that adds all the informations in 66 different .txt files into one txt file, which gives as a result 'kor_bible_info.txt'. <br />
write_kor_bible.py contains the code that convert the 'kor_bible_info.txt' file into 'kor_bible_csv' file and adds the unique id to each verse. <br />
id.py contains the code that finds the unique id of the requested verse(s). <br />
bible_find.py returns the bible verse requested by the user. <br />
bible.py is the python file that contains the gui of this bible app. <br />
<br />

To start the web application, run:
### `python bible.py` or `python3 bible.py`

Important functions and notes: <br />
Fill out the book, chapter, and verses sections and press 'Search' button in order to obtain the requested verses. <br />
If you want to clear out the screen, press 'Clear' button. <br />
When you want to get all verses in one whole chapter, fill in the book and chapter informations and leave the verses part blank. <br />
If you want to get only one specific verse, fill in the book, chapter informations and only the first part of the verses section. <br />
