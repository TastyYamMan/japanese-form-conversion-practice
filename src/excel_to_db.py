from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Word

import pandas as pd

engine = create_engine('sqlite:///src/japanese_practice.db')
Session = sessionmaker(bind=engine)
session = Session()

df_words = pd.read_excel('src/words/words.xlsx')

for index, row in df_words.iterrows():
    check = session.query(Word).filter(
                Word.kanji == row['kanji'],
                Word.kana == row['kana'],
                Word.meaning == row['meaning']
            ).first()
    if not check is None:
        continue
    word = Word(kanji = row['kanji'],
                kana = row['kana'],
                romaji = row['romaji'],
                meaning = row['meaning'],
                lesson = row['lesson'])
    if word.kana == 'なん':
        word.romaji = 'nan'
    session.add(word)
    session.commit()