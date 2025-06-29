GROUP_1_MAPPINGS = {
    'い': 'う',
    'ち': 'つ',
    'り': 'る',
    'び': 'ぶ',
    'み': 'む',
    'に': 'ぬ',
    'き': 'く',
    'ぎ': 'ぐ',
    'し': 'す'
}

def う_form(input_verb):
    verb = input_verb.copy()
    if verb['kana'][-2:] != 'ます':
        raise TypeError('Input verb is not in ます form.')
    if verb['kanji'][-3:] == 'します' and verb['group'] == 3:
        verb['kanji'] = verb['kanji'][:-3] + 'する'
        verb['kana'] = verb['kana'][:-3] + 'する'
        verb['romaji'] = verb['romaji'][:-7] + 'suru'
        return verb
    if verb['group'] == 1:
        for input, output in GROUP_1_MAPPINGS.items():
            splitted_kanji = verb['kanji'].split(input+'ます')
            splitted_kana = verb['kana'].split(input+'ます')
            if splitted_kanji[0] != verb['kanji'] and splitted_kana[0] != verb['kana']:
                verb['kanji'] = splitted_kanji[0] + output
                verb['kana'] = splitted_kana[0] + output
        if input_verb['kanji'][-3] == 'ち':
            verb['romaji'] = verb['romaji'][:-7] + 'tsu'
        elif input_verb['kanji'][-3] == 'し':
            verb['romaji'] = verb['romaji'][:-7] + 'su'
        else:
            verb['romaji'] = verb['romaji'][:-5] + 'u'
        return verb
    verb['kanji'] = verb['kanji'].split('ます')[0]+'る'
    verb['kana'] = verb['kana'].split('ます')[0]+'る'
    verb['romaji'] = verb['romaji'].split('masu')[0]+'ru'
    return verb