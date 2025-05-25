GROUP_1_MAPPINGS = {
    'い': 'わ',
    'ち': 'た',
    'り': 'ら',
    'び': 'ば',
    'み': 'ま',
    'に': 'な',
    'き': 'か',
    'ぎ': 'が',
    'し': 'さ'
}

def ない_form(input_verb):
    verb = input_verb.copy()
    if verb['kana'][-2:] != 'ます':
        raise TypeError('Input verb is not in ます form.')
    if verb['kanji'][:-4] == '来ます':
        verb['kanji'] = '来ない'
        verb['kana'] = 'こない'
        verb['romaji'] = 'konai'
        return verb
    if verb['group'] == 1:
        for input, output in GROUP_1_MAPPINGS.items():
            splitted_kanji = verb['kanji'].split(input+'ます')
            splitted_kana = verb['kana'].split(input+'ます')
            if splitted_kanji[0] != verb['kanji'] and splitted_kana[0] != verb['kana']:
                verb['kanji'] = splitted_kanji[0] + output + 'ない'
                verb['kana'] = splitted_kana[0] + output + 'ない'
        if verb['kanji'][-3] == 'ち':
            verb['romaji'] = verb['romaji'][:-7] + 'tanai'
        elif verb['kanji'][-3] == 'し':
            verb['romaji'] = verb['romaji'][:-7] + 'sanai'
        else:
            verb['romaji'] = verb['romaji'][:-5] + 'anai'
        return verb
    verb['kanji'] = verb['kanji'].split('ます')[0]+'ない'
    verb['kana'] = verb['kana'].split('ます')[0]+'ない'
    verb['romaji'] = verb['romaji'].split('masu')[0]+'nai'
    return verb