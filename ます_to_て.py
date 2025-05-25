GROUP_1_MAPPINGS = {
    'って': ['い','ち','り'],
    'んで': ['び','み','に'],
    'いて': ['き'],
    'いで': ['ぎ'],
    'して': ['し']
}

def ます_to_て(verb):
    if verb['kana'][-2:] != 'ます':
        raise TypeError('Input verb is not in ます form.')
    if verb['kanji'] == '行きます':
        return 'いって'
    if verb['group'] == 1:
        static = verb['kana'][:-3]
        variable = verb['kana'][-3]
        for output, input in GROUP_1_MAPPINGS.items():
            if variable in input:
                return static + output
    return verb['kana'][:-2] + 'て'