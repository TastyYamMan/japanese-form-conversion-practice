from verbs.て_form import て_form

def た_form(input_verb):
    verb = て_form(input_verb.copy())
    if verb['kanji'][-1] == 'て':
        verb['kanji'] = verb['kanji'][:-1] + 'た'
        verb['kana'] = verb['kana'][:-1] + 'た'
        verb['romaji'] = verb['romaji'][:-2] + 'ta'
    else:
        verb['kanji'] = verb['kanji'][:-1] + 'だ'
        verb['kana'] = verb['kana'][:-1] + 'だ'
        verb['romaji'] = verb['romaji'][:-2] + 'da'
    return verb