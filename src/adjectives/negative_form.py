def negative_form(input_adj):
    output_adj = input_adj.copy()
    if output_adj.group == 'な':
        output_adj.kanji += 'じゃありません'
        output_adj.kana += 'じゃありません'
        output_adj.romaji += 'jyaarimasen'
    if output_adj.group == 'い':
        output_adj.kanji = output_adj.kanji[:-1] + 'くない'
        output_adj.kana = output_adj.kana[:-1] + 'くない'
        output_adj.romaji = output_adj.romaji[:-1] + 'kunai'
    return output_adj
