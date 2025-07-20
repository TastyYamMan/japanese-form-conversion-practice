import yaml
from itertools import chain
import json
import pandas as pd

MAX_LESSON = 24

GROUP_EXCEPTIONS = {
    '1': ['伸ばします', '思い出します'],
    '2': ['起きます', 'できます']
}

VERB_EXCEPTIONS = []

manual_verbs_kanji = [
    '飛びます', '登ります', '走ります', 'もぐります', '飛び込みます', '逆立ちます', 'ほいます', 'けります', 
    '振ります', '持ち上げます', '投げます', 'たたきます', '引きます', '押します', '曲げます', '伸ばします', '転びます', 
    '振り向きますます'
]
manual_verbs_kana = [
    'とびます', 'のぼります', 'はしります', 'もぐります', 'とびこみます', 'さかだちます', 'ほいます', 'けります', 'ふります', 
    'もちあげます', 'なげます', 'たたきます', 'ひきます', 'おします', 'まげます', 'のばします', 'ころびます', 'ふりむきます'
]
manual_verbs_romaji = [
    'tobimasu', 'noborimasu', 'hashirimasu', 'mogurimasu', 'tobikomimasu', 'sakadachimasu', 'hoimasu', 'kerimasu',
    'furimasu', 'mochiagemasu', 'nagemasu', 'tatakimasu', 'hikimasu', 'oshimasu', 'magemasu', 'nobashimasu',
    'korobimasu', 'furimukimasu'
]

def group(verb):
    for group_num, exception_verbs in GROUP_EXCEPTIONS.items():
        if verb['kanji'] in exception_verbs:
            return int(group_num)
    if (verb['kanji'][-3:] == 'します' and len(verb['kanji']) > 4) or verb['kanji'][-3:] == '来ます':
        return 3
    elif verb['romaji'][-5] == 'e' or len(verb['kana']) == 3 or len(verb['kanji']) == 3:
        return 2
    elif verb['romaji'][-5] == 'i':
        return 1

def get_verbs(lesson):
    verbs = []
    for word in lesson:
        if 2 not in word['edition']:
            continue
        if word['kanji'] is None:
            word['kanji'] = word['kana']
        if 'を' in word['kana']:
            continue
        if word['kanji'] in VERB_EXCEPTIONS:
            continue
        if word['kana'][-2:] == 'ます':
            if 'ū' in word['romaji']:
                word['romaji'] = word['romaji'].replace('ū', 'uu')
            if 'ō' in word['romaji']:
                word['romaji'] = word['romaji'].replace('ō', 'ou')
            for kanji in word['kanji'].split('、'):
                cleaned = {
                    'kanji': kanji.replace(' ',''), 
                    'kana' : word['kana'].replace(' ',''), 
                    'romaji' : word['romaji'].replace(' ',''), 
                    'group': group(word)
                }
                verbs.append(cleaned)
    return verbs

with open("minna-no-ds.yaml", "r", encoding="utf-8") as f:
    ds = yaml.load(f, Loader=yaml.FullLoader)

lessons = [ds[f'lesson-{str(i+1).zfill(2)}'] for i in range(MAX_LESSON)]

verbs = list(chain.from_iterable([get_verbs(lesson) for lesson in lessons]))

manual_verbs = [{'kanji': manual_verbs_kanji[i], 'kana': manual_verbs_kana[i], 'romaji': manual_verbs_romaji[i]} for i in range(len(manual_verbs_kana))]
for verb in manual_verbs:
    verb['group'] = group(verb)

verbs_complete = verbs + manual_verbs

with open("src/verbs/verbs.json", "w") as outfile:
    json.dump(verbs, outfile)

pd.DataFrame(verbs_complete).to_excel('src/verbs/verbs.xlsx', index=False)