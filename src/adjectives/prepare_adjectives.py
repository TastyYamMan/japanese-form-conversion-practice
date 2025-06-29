import yaml
from itertools import chain
import json
import pandas as pd

with open("minna-no-ds.yaml", "r", encoding="utf-8") as f:
    ds = yaml.load(f, Loader=yaml.FullLoader)

lessons = [ds[f'lesson-{str(i+1).zfill(2)}'] for i in range(24)]

TYPE_EXCEPTIONS = {
    'な': [],
    'い': []
}

ADJ_EXCEPTIONS = ['はい', 'おととい', 'だいたい', '～ぐらい', 'どのくらい']

def type(adj):
    for type, exception_adjs in TYPE_EXCEPTIONS.items():
        if adj['kanji'] in exception_adjs:
            return
    if adj['kanji'][-1] == 'い':
        return 'い'
    elif adj['kanji'][-3:] == '［な］':
        return 'な'

def remove(string, substrings):
    for substring in substrings:
        string = string.replace(substring, '')
    return string
    

def clean(adj, kanji):
    cleaned = {
        'kanji': remove(kanji, [' ', ')', '［な］']), 
        'kana' : remove(adj['kana'], [' ', ')', '［な］']), 
        'romaji' : remove(adj['romaji'], [' ', ')', '[na]']), 
        'group': type(adj)
    }
    return cleaned

def get_adjs(lesson):
    adjs = []
    for word in lesson:
        if 2 not in word['edition']:
            continue
        if word['kanji'] is None:
            word['kanji'] = word['kana']
        if word['kanji'] in ADJ_EXCEPTIONS:
            continue
        # な-adjs not coming through
        if type(word) is not None:
            if 'ū' in word['romaji']:
                word['romaji'] = word['romaji'].replace('ū', 'uu')
            if 'ō' in word['romaji']:
                word['romaji'] = word['romaji'].replace('ō', 'ou')
            if len(word['kanji'].split('(')) > 1:
                for kanji in word['kanji'].split('('):
                    adjs.append(clean(word,kanji))
            for kanji in word['kanji'].split('、'):
                adjs.append(clean(word,kanji))
    return adjs

adjs = list(chain.from_iterable([get_adjs(lesson) for lesson in lessons]))

df_manual = pd.read_excel('src/adjectives/adjs_manual.xlsx')
df_adjs = pd.concat([pd.DataFrame(adjs),df_manual])

df_adjs.to_excel('src/adjectives/adjs.xlsx', index=False)