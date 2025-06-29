import yaml
from itertools import chain
import pandas as pd

MAX_LESSON = 26

def get_words(lesson):
    words = []
    for word in lesson:
        if 2 not in word['edition']:
            continue
        if word['kanji'] is None:
            word['kanji'] = word['kana']
        if 'ū' in word['romaji']:
            word['romaji'] = word['romaji'].replace('ū', 'uu')
        if 'ō' in word['romaji']:
            word['romaji'] = word['romaji'].replace('ō', 'ou')
        for kanji in word['kanji'].split('、'):
            cleaned = {
                'kanji': kanji.replace(' ',''), 
                'kana' : word['kana'].replace(' ',''), 
                'romaji' : word['romaji'].replace(' ',''),
                'meaning' : word['meaning']['en'],
                'lesson' : word['id'][0]
            }
            words.append(cleaned)
    return words

with open("minna-no-ds.yaml", "r", encoding="utf-8") as f:
    ds = yaml.load(f, Loader=yaml.FullLoader)

lessons = [ds[f'lesson-{str(i+1).zfill(2)}'] for i in range(MAX_LESSON)]

words = list(chain.from_iterable([get_words(lesson) for lesson in lessons]))

manual = pd.read_excel('src/words/words_manual.xlsx')

pd.concat([pd.DataFrame(words), manual]).to_excel('src/words/words.xlsx', index=False)