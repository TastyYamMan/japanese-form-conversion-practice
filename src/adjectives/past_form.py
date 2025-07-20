def past_form(input_adj):
    output_adj = input_adj.copy()
    if output_adj.group == 'な':
        output_adj.kanji += 'でした'
        output_adj.kana += 'でした'
        output_adj.romaji += 'deshita'
    if output_adj.group == 'い':
        output_adj.kanji = output_adj.kanji[:-1] + 'かった'
        output_adj.kana = output_adj.kana[:-1] + 'かった'
        output_adj.romaji = output_adj.romaji[:-1] + 'katta'
    return output_adj