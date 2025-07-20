def present_form(input_adj):
    output_adj = input_adj.copy()
    if output_adj.group == 'な':
        output_adj.kanji += 'です'
        output_adj.kana += 'です'
        output_adj.romaji += 'desu'
    return output_adj