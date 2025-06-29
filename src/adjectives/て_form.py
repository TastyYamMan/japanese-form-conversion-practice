def て_form(input_adj):
    output_adj = input_adj.copy()
    if output_adj.group == 'な':
        output_adj.kanji += 'で'
        output_adj.kana += 'で'
        output_adj.romaji += 'de'
    if output_adj.group == 'い':
        output_adj.kanji = output_adj.kanji[:-1] + 'くて'
        output_adj.kana = output_adj.kana[:-1] + 'くて'
        output_adj.romaji = output_adj.romaji[:-1] + 'kute'
    return output_adj
