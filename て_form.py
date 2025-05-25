GROUP_1_MAPPINGS = {
    'kana/kanji':{
        'って': ['い','ち','り'],
        'んで': ['び','み','に'],
        'いて': ['き'],
        'いで': ['ぎ'],
        'して': ['し']
    },
    'romaji':{
        'nde': ['bi','mi','ni'],
        'ite': ['ki'],
        'ide': ['gi'],
        'shite': ['shi'],
        'tte': ['chi','ri','i']
    }
}

def て_form(input_verb):
    verb = input_verb.copy()
    if verb['kana'][-2:] != 'ます':
        raise TypeError('Input verb is not in ます form.')
    if verb['kanji'][:-4] == '行きます':
        verb['kanji'] = '行って'
        verb['kana'] = 'いって'
        verb['romaji'] = 'itte'
        return verb
    if verb['group'] == 1:
        for output, inputs in GROUP_1_MAPPINGS['kana/kanji'].items():
            for input in inputs:
                splitted_kanji = verb['kanji'].split(input+'ます')
                splitted_kana = verb['kana'].split(input+'ます')
                if splitted_kanji[0] != verb['kanji'] and splitted_kana[0] != verb['kana']:
                    verb['kanji'] = splitted_kanji[0] + output
                    verb['kana'] = splitted_kana[0] + output
        for output, inputs in GROUP_1_MAPPINGS['romaji'].items():
            for input in inputs:
                splitted_romaji = verb['romaji'].split(input+'masu')
                if splitted_romaji[0] != verb['romaji']:
                    verb['romaji'] = splitted_romaji[0] + output
        return verb
    verb['kanji'] = verb['kanji'].split('ます')[0]+'て'
    verb['kana'] = verb['kana'].split('ます')[0]+'て'
    verb['romaji'] = verb['romaji'].split('masu')[0]+'te'
    return verb